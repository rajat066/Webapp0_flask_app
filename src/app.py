from flask import Flask
proj = Flask(__name__)

@proj.route('/')
def index():
    return 'Welcome to flask login application'

if __name__ == "__main__":
    proj.run(debug = True, port=701)