from flask import Flask
 
display = Flask(__name__)

@display.route('/')
def index():
    return 'hello world'

@display.route('/<name>/')
def hello(name):
    return 'Hello '+ name

@display.route('/')
def image():
    return download.jpg

if __name__ == '__main__':  

   display.run(debug=True)