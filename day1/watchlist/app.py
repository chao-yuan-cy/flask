from flask import Flask
app = Flask(__name__)
# print('nihao')
@app.route('/')

@app.route('/home')
def index():
    return "<h1>Hello，Flask</h1>"
#动态url
@app.route('/index/<name>')
def home(name):
   
    return '<h1>hello,%s</h1>'%name