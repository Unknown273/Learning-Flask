from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def root():
  return render_template('home.html')

@app.route('/login_signup')
def index():
  return render_template("login_signup.html")

if __name__ == "__main__":
  app.run()
