from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/users/<id>")
def users(id):
	users = [
		{"name": "Jon"},
		{"name": "Mandy"}
	]
	return str(users[int(id)])

@app.route("/form", methods = ['GET', 'POST'])
def form():
	if request.method == "GET":
		return render_template('form.html', name = session.get('name', ""))
	else:
		session['name'] = request.form['name']
		return "Your name is " + request.form['name'] + " and it has been stored in the session"

@app.route("/login", methods = ['GET', 'POST'])
def login():
  if request.method == "GET":
    return render_template('login.html')
  else:
    session['name'] = request.form['name']
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
