
from flask import Flask
from flask import render_template # required to return templates
from flask import request # required to receive form data
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/html')
def hello_world_html():
    return '<html><h1>Hello World!</h1><p>This is html</p></html>'

@app.route('/template')
def hello_world_template():
    return render_template('template.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/postForm', methods=['POST'])
def postForm():
    return render_template('thankyou.html',
        firstname=request.form['firstname'],
        lastname=request.form['lastname'],
        address=request.form['address'],
        phone=request.form['phone'])

@app.route('/prettyForm')
def prettyForm():
    return render_template('prettyform.html')

if __name__ == '__main__':
    app.run()