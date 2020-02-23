import os
basedir = os.path.abspath(os.path.dirname(__file__))
#密钥配置
class Config(object):
	SQLALCHEMY_DATABASE_URI ='mysql://root:root@127.0.0.1:3306/app'

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-nerver-guess'
	#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	#	'sqlite:///' + os.path.joiin(basedir,'app.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False