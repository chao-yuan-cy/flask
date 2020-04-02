import os
import sys

from flask import Flask,url_for,render_template
import click
from flask_sqlalchemy import SQLAlchemy#导入扩展类

WIN = sys.platform.startswith('win')

if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
print(WIN)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix +os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
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

#自定义命令
@app.cli.command()#装饰器。注册命令
@click.option('--drop',is_flag=True,help='删除后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库完成')