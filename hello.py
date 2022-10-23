from flask import Flask
hello = Flask(__name__)

@hello.route('/')
def hello_world():
    return 'Hello pulung hendro prastyo'
    