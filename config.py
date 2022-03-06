import os


class Config(object):
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'