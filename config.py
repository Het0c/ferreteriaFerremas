import os

class Config:
    CLAVE_SECRETA = os.environ.get('CLAVE_SECRETA') or 'clave-secreta-ferremas'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///ferremas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEBPAY_API_KEY = os.environ.get('WEBPAY_API_KEY')
    URL_BANCO_CENTRAL = 'https://api.bcentral.cl/series/v1'