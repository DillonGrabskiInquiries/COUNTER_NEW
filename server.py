from flask import Flask, session, render_template, url_for, request, redirect
app = Flask(__name__)
app.secret_key = 'this is the secret key'


def SessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1


@app.route('/')
def index():
    SessionCounter()
    return render_template('index.html')

@app.route('/destroy')
def destroy():
    session.destroy()
    return render_template('index.html')




app.run(debug=True)