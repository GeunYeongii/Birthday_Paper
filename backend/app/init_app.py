import os
import datetime
from flask import Flask, render_template_string, request
from flask_babelex import Babel
from flask_user import login_required, roles_required, UserManager, UserMixin
from flask_cors import CORS

ORM_type = 'SQLAlchemy'   # SQLAlchemy  or MongoEngine
# ORM_type = 'MongoEngine'   # SQLAlchemy  or MongoEngine

# Setup Flask & cors
app = Flask(__name__)
CORS(app)

# Use a Class-based config to avoid needing a 2nd file
# os.getenv() enables configuration through OS environment variables
class ConfigClass(object):
    # Flask settings
    SECRET_KEY = 'Birthday Paper Project'  # Less than 32 bytes

    # Flask-SQLAlchemy settings
    # type --->  mysql://username:password@localhost/db_name'
    SQLALCHEMY_DATABASE_URI = 'mysql://dave:wnrmsdud12!@localhost:3306/birthday_paper'    # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    MAIL_USERNAME =           os.getenv('MAIL_USERNAME',        'cky0935@gmail.com')
    MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD',        'cshtgm3558')
    MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER',  '"Birthday_paper" <cky0935@gmail.com>')
    MAIL_SERVER =             os.getenv('MAIL_SERVER',          'smtp.gmail.com')
    MAIL_PORT =           int(os.getenv('MAIL_PORT',            '465'))
    MAIL_USE_SSL =            os.getenv('MAIL_USE_SSL',         True)

    # Sengrid settings
    SENDGRID_API_KEY = 'some-bogus-value'

    # Flask-User settings
    USER_APP_NAME = 'TestApp'
    USER_ENABLE_EMAIL = True
    USER_ENABLE_INVITE_USER = True

    # Deliberately test with deprecated v0.6 Flask-User settings
    USER_ENABLE_LOGIN_WITHOUT_CONFIRM_EMAIL = False
    USER_ENABLE_RETYPE_PASSWORD = True
    USER_SHOW_USERNAME_EMAIL_DOES_NOT_EXIST = False
    USER_PASSWORD_HASH = 'bcrypt'

# Read app config from class
app.config.from_object(__name__+'.ConfigClass')

# Setup Flask-BabelEx
babel = Babel(app)

if ORM_type=='SQLAlchemy':
    # Initialize Flask-SQLAlchemy, using SQLALCHEMY_DATABASE_URI setting
    from flask_sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)

    # Define the User data-model. Make sure to add flask_user UserMixin!!
    class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')

        # User authentication information
        username = db.Column(db.String(50), nullable=True, unique=True)
        email = db.Column(db.String(255, collation='utf8mb4_0900_ai_ci'), nullable=True, unique=True)
        
        """ email_confirmed_at = db.Column(db.DateTime()) -->  Need NOT"""
        
        password = db.Column(db.String(255), nullable=False, server_default='')

        # User information
        # first_name = db.Column(db.String(100, collation='utf8mb4_0900_ai_ci'), nullable=False, server_default='')
        # last_name = db.Column(db.String(100, collation='utf8mb4_0900_ai_ci'), nullable=False, server_default='')

        # Relationships
        roles = db.relationship('Role', secondary='user_roles',
                backref=db.backref('users', lazy='dynamic'))

    # Define UserEmail DataModel.
    class UserEmail(db.Model):
        __tablename__ = 'user_emails'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        user = db.relationship('User', uselist=False)

        # User email information
        email = db.Column(db.String(255), nullable=True, unique=True)
        """mail_confirmed_at = db.Column(db.DateTime()) """
        is_primary = db.Column(db.Boolean(), nullable=False, default=False)

    class UserInvitation(db.Model):
        __tablename__ = 'user_invitations'
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(255), nullable=False)
        # save the user of the invitee
        invited_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        invited_by_user = db.relationship('User', uselist=False)
        # token used for registration page to identify user registering
        token = db.Column(db.String(100), nullable=False, server_default='')

    # Define the Role data-model
    class Role(db.Model):
        __tablename__ = 'roles'
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(50), unique=True)

    # Define the UserRoles data-model
    class UserRoles(db.Model):
        __tablename__ = 'user_roles'
        id = db.Column(db.Integer(), primary_key=True)
        user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
        role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


# Define custom UserManager class
class CustomUserManager(UserManager):

    # Install all EmailAdapters to cover their initialization code
    def customize(self, app):
        from flask_user.email_adapters import SendmailEmailAdapter
        from flask_user.email_adapters import SendgridEmailAdapter
        from flask_user.email_adapters import SMTPEmailAdapter
        email_adapter = SendmailEmailAdapter(app)
        email_adapter = SendgridEmailAdapter(app)
        email_adapter = SMTPEmailAdapter(app)


def init_app(app, config=None):                # For automated tests
    # Load local_settings.py if file exists         # For automated tests
    try: app.config.from_object('local_settings')
    except ImportError: pass

    # Load optional test_config                     # For automated tests
    if config:
        app.config.update(config)

    # Setup Flask-User
    if ORM_type == 'SQLAlchemy':
        RoleClass = Role
        user_manager = CustomUserManager(app, db, User, UserInvitationClass=UserInvitation, RoleClass=RoleClass)
    else:
        RoleClass = None
        user_manager = CustomUserManager(app, db, User, RoleClass=RoleClass)

    # Test MAIL_DEFAULT_SENDER parser
    assert user_manager.USER_EMAIL_SENDER_NAME=='Birthday_Paper'
    assert user_manager.USER_EMAIL_SENDER_EMAIL=='cky0935@gmail.com'

    # Reset database by dropping, then creating all tables
    db_manager = user_manager.db_manager
    db_manager.drop_all_tables()
    db_manager.create_all_tables()

    # For debugging purposes
    token = user_manager.generate_token('abc', 123, 'xyz')
    data_items = user_manager.token_manager.verify_token(token, 3600)
    assert data_items is not None
    assert data_items[0] == 'abc'
    assert data_items[1] == 123
    assert data_items[2] == 'xyz'

 # Creating Test
 #---------------------
    # Create regular 'member' user
    user = db_manager.add_user(username='member', email='member@example.com',
            password=user_manager.hash_password('Password1'), email_confirmed_at=datetime.datetime.utcnow())
    db_manager.commit()

    # Create 'user007' user with 'secret' and 'agent' roles
    user = db_manager.add_user(username='user007', email='admin@example.com',
            password=user_manager.hash_password('Password1'))
    db_manager.add_user_role(user, 'secret')
    db_manager.add_user_role(user, 'agent')
    db_manager.commit()

    # The '/' page is accessible to anyone
    @app.route('/')
    def home_page():
        return NotImplementedError

    # The '/profile' page requires a logged-in user
    @app.route('/user/profile')
    @login_required                                 # Use of @login_required decorator
    def user_profile_page():
        return NotImplementedError

    # The '/special' page requires a user that has the 'secret' AND ('sauce' OR 'agent') role.
    @app.route('/special')
    @roles_required('secret', ['sauce', 'agent'])   # Use of @roles_required decorator
    def admin_page():
        return NotImplementedError

    # For testing only
    app.db = db
    if ORM_type == 'SQLAlchemy':
        app.UserEmailClass = UserEmail

    return app

