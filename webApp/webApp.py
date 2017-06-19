'''
Copyright 2017 Linyi Cheng

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


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