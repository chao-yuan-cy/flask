from flask import Flask,url_for,render_template
app = Flask(__name__)
# print('nihao')
@app.route('/')

@app.route('/home')
def index():
    name = '你好'
    movies = [
        {'title':'大赢家','year':'2020'},
        {'title':'囧妈','year':'2020'},
        {'title':'战狼','year':'2018'},
        {'title':'心花路放','year':'2014'},
        {'title':'速度与激情','year':'2018'},
        {'title':'港囧','year':'2016'},
    ]
    return render_template('index.html',name=name,movies=movies)
#动态url
@app.route('/index/<name>')
def home(name):
    print(url_for('home',name='hi'))
    return '<h1>hello,%s</h1>'%name