"""test_tric"""
import os


class Config:
    """test_tric"""
    SECRET_KEY = '1d5f85d4f8h9dfdfdsfdsf9sgh4ds9hd'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
