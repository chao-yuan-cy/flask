from flask import render_template
from watchlistapp import app
# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    #返回模板和源码
    return render_template('errors/404.html'),404
@app.errorhandler(500)
def page_error(e):
    # user = User.query.first()
    return render_template('errors/500.html'),500