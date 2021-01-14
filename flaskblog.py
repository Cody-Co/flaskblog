from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '9908084e3a452d7b82e9636b14f67233'

posts = [
	{
		'author': 'Cody-Co',
		'title': 'Blog 1',
		'content': 'First post',
		'date_posted': 'January 13, 2021'
	},
	{
		'author': 'Jango Fett',
		'title': 'Blog 2',
		'content': 'The lore of Mando',
		'date_posted': 'January 14, 2021'
	}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login failed. Please check username and password', 'danger')
	return render_template('login.html', title='login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
