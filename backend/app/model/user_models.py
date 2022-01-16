# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy

from flask_user import UserMixin
from importlib_metadata import method_cache
from app import db


# Define the User data-model. Make sure to add flask_user UserMixin!!
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
    
    # User authentication information
    public_id = db.Column(db.String(50), nullable=True, unique=True)
    username = db.Column(db.String(50), nullable=True, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    admin = db.Column(db.Boolean)
    
    email = db.Column(db.String(255, collation='utf8mb4_0900_ai_ci'), nullable=True, unique=True)
    

