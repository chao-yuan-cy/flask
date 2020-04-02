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
#models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


#模板上下文处理函数
@app.context_processor
def common_user():
    user = User.query.first()
    return dict(user=user)
#views
@app.route('/')
@app.route('/home')

def index():
 
    # user = User.query.first()
    movies = Movie.query.all()

    return render_template('index.html',movies=movies)
#动态url
@app.route('/index/<name>')
def home(name):
    print(url_for('home',name='hi'))
    return '<h1>hello,%s</h1>'%name

#自定义命令
#新建data.db的数据库初始化命令
@app.cli.command()#装饰器。注册命令
@click.option('--drop',is_flag=True,help='删除后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库完成')

# 项data.db中写入数据的命令
@app.cli.command()
def forge():
    name = '你好'
    movies = [
        {'title':'大赢家','year':'2020'},
        {'title':'囧妈','year':'2020'},
        {'title':'战狼','year':'2018'},
        {'title':'心花路放','year':'2014'},
        {'title':'速度与激情','year':'2018'},
        {'title':'港囧','year':'2016'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movies = Movie(title=m['title'],year=m['year'])
        db.session.add(movies)
    db.session.commit()
    click.echo('插入数据完成')


# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    #返回模板和源码
    return render_template('404.html'),404
@app.errorhandler(500)
def page_error(e):
    # user = User.query.first()
    return render_template('500.html'),500

