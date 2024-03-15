from flask import Flask
home= Flask(__name__)
@home.route('/')
def display_data():
    return 'hello nidhi'

@home.route('/<value>/')
def data(value):
    return '<h1>'+value+'</h1>'
if __name__ == '__main__':
    home.run()