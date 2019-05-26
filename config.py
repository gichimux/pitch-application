import os

class Config:
    '''
    general configuration parent class
    '''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gichimu:trio.com@localhost/pitch2'
    SECRET_KEY = "secret key"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")





class ProdConfig(Config):
'''
    production configuration child class

    Args:
        Config: the parent configuration class with general configuration settings
    '''    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")#for heroku purposes

class DevConfig(Config):
'''
    development configuration child class

    Args:
        Config: the parent configuration class with general configuration settings 
    '''    
    DEBUG = True


config_options ={
    'development' :DevConfig,
    'production' :ProdConfig,
    'test' :TestConfig
}