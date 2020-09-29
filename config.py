import os 
class Config :
    '''General config parent class'''
    SECRET_KEY="powerful secretkey"
    QUOTES_URL='http://quotes.stormconsultancy.co.uk/random.json'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config): 
    '''productio config  child class
        arg: 
            config: parent config class

        '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):
    '''Development configuration child class
    arg:
        Config: parent configurations class
        '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
