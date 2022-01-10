from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def index():
        return '<h1>I want to deploy on Heroku!</h1>'
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
