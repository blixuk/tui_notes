import os

from flask import Flask, request, render_template
app = Flask(__name__)

title = 'Notes'
text = ''

@app.route('/')
def index():
	return render_template('/index.html', title=title)

@app.route('/submit', methods=['POST'])
def submit():
	print(request.form['text'])
	return 'You entered: {}'.format(request.form['text'])

@app.route('/open', methods=['POST'])
def open():
	if request.method == 'POST':
		f = request.files['file']
		#f.save(f.filename)
	text = f.save(f.filename)
	return render_template('/index.html', title=title, text=text)

def openNote():
	notePath = os.getcwd() + 'notes/test.txt'
	note = open(notePath, 'r')
	return note

if __name__ == '__main__':
	app.run()