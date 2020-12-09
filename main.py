from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello it\'s Home'


@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html',name = user)

if __name__=='__main__':
    app.run(debug = True)