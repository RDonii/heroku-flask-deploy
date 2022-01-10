from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '<h1>I want to deploy on Heroku!</h1>'


if __name__ == '__main__':
  app.run(host='https://flask-heroku-deploy-10-01.herokuapp.com', port=80, debug=True, use_reloader=True)
