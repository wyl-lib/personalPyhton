from flask import render_template
from flask import make_response
from flask import request
from app import app
from flask import Flask,url_for
from app.forms import LoginForm
from app.mineForm import mineForm
#from flask_bootstrap import Bootstrap

#url_for('static',filename = "style.css")

@app.route('/')
def hi_index():
	user = {'username':'Yulin.Wang'}
	username = request.cookies.get('username')
	resp = make_response(render_template('index.html'))
	resp.set_cookie('username','I am cookie')
	return resp
	#return '<h1>This is app.route() of def hi_index.So hello man^_^</h1>'

@app.route("/register",methods=["GET"])
def register():
	return render_template("/register.html")
@app.route("/register",methods=["Post"])
def registerPost():
	user=User();
	user.username=request.form.get("username","")
	user.password = request.form.get("password", "")
	user.birthday = request.form.get("birthday", "")
	user.email = request.form.get("email", "")
	user.gender = request.form.get("gender", "")
	user.nickname = request.form.get("nickname", "")
	user.role_id = 1 #暂时约定公开用户角色为1
	#判断,其中用户名,密码,昵称不能为空
	if(len(user.username.strip())==0):
		flash("用户名不能为空")
		return render_template("register.html")
	if(len(user.password.strip())==0):
		flash("用户密码不能为空")
		return render_template("register.html")
	if (len(user.nickname.strip()) == 0):
		flash("用户昵称不能为空")
		return render_template("register.html")
	db.session.add(user);
	flash("您已注册成功")
	return render_template("register.html")

##index.html
@app.route('/index')
def index():
	user = {'username':'Yulin.Wang'}
	post_blog = [
		{
			'author' : {'username' : 'John'},
			'body' : 'The dark and cold day in Yantai'

		},
		{
			'author' : {'username' : 'Marry'},
			'body' : 'I have a beautifulsoup,so cool!'	
		}
	]
	return render_template('index.html',title='Home',user=user,posts=post_blog)

##login.html
@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	#user = {'username':'Yulin.Wang'}
	#username = request.cookies.get('username')
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html',title='Sign In', form=form)
	#return render_template('login.html',title = 'Login In',form = form)

##mine.html
@app.route('/Feedback')
def Feedback():
	form = mineForm()
	user = {'username':'Yulin.Wang'}
	return render_template('Feedback.html',user = user,title = 'Fill in the informations!',form = form)

#@app.route('/setting')
#def setting():
if __name__=="__main__":
	app.run(debug=Ture)

'''
<html>
	<head>
		<title>Home Page - Microblog</title>
	</head>
	<body>
		<h1>Hello, \''' + user['username'] + \'''!</h1>
	</body>
</html>
'''