WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'gjapp.db')
else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	
# SQLALCHEMY_DATABASE_URI = 'mysql://app:app@localhost/app'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
