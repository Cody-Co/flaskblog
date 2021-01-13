from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)
