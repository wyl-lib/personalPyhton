from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = TextField('your username',validators = [DataRequired()])
#	password = PasswordField("password",validators = [DataRequired()])
	password = PasswordField('your password',[validators.DataRequired(),validators.EqualTo('confirm',message = 'password must match')])
	confirm = PasswordField('Repeat password')
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

#class mineForm(FlaskForm):
#	username = StringField('username',validators = [DataRequired()])
#	print("hello,master.{}",username)
	