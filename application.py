from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'testing cicd'

if __name__ == "__main__":
    application.run()
