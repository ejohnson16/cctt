
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
<head>
	<title>The Royal Ping Pong Club</title>
	<h1>Welcome fellow ping pong lovers!</h1>
	<h3>Welcome to the homepage of the table tennis club at Columbia College. We welcome players of all levels whether you’re playing for fun, to socialize, or to improve your skills.</h3>
	<img src="http://cctt0.pythonanywhere.com/static/images/cctt.png/" alt="Royal Ping Pong Club Logo" style="width:128px;height:128px;">
</head>
<body>
<br>
	Evan is the supervisor, Ed is the subordinate. <br>
	<b>Sign in Here!</b>
	<form>
		Email:
		<br>
		<input type ='text'>
		<br>
		Password:
		<br>
		<input type ='password'>
		<br>
		<input type="submit">

	</form>
    No account? Click
    <a href="signup">here</a>
    to signup!
    <br>
     <br>
      <br>
       <br>
       Click <a href="http://cctt0.pythonanywhere.com/index">here</a> for the actuall site that also contains the calendar
       <br>
</body>
</html>
'''

@app.route('/signup')
def signup():
    return '''
<html>
	<b>No Account? Create one here!</b>
	<form>
		Email:
		<br>
		<input type ='text'>
		<br>
		Password:
		<br>
		<input type ='password'>
		<br>
		Confirm Password:
		<br>
		<input type ='password'>
		<br>
		First Name:
		<br>
		<input type="text">
		<br>
		Last Name:
		<br>
		<input type="text">
		<br>
		Age:
		<br>
		<input type="text">
		<br>
		<input type="submit">
	</form>
</html>
'''

