from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/result/<int:score>')
def show_result(score):
    return render_template('result.html',marks = score)

@app.route('/marks')
def show_marks():
    dict = {'Physics':65, 'Chemistry':67, 'Biology':78}
    return render_template('marks.html', marks = dict)

if __name__=='__main__':
    app.run(debug = True)