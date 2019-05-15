from app_base import app
from lib.oauth import OAuth
from config import oauth_config

oauth = OAuth(app, oauth_config, rbac=None)