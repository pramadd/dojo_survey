from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def Name():
    name = request.form['name']
    dojolocation = request.form['dojolocation']
    language = request.form['language']
    comment =request.form['comment']
    return render_template("result.html", name = name,dojolocation=dojolocation,language=language,comment=comment)
    return redirect("/")


app.run(debug = True)