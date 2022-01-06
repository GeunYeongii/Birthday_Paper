from application import app;

if not app.debug:   # debug=False 모드 일 때 Product Mode 전환 후 로그 기록
    import logging
    from logging.handlers import RotatingFileHandler  # logging 핸들러 이름
    file_handler = RotatingFileHandler(
        'dave_server.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)  # WARNING 단계까지 로깅
    # app.logger.addHandler() 에 등록시켜줘야 app.logger 로 사용 가능
    app.logger.addHandler(file_handler)
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug=True)
    
