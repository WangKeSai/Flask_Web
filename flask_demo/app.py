# coding: utf-8
from flask import Flask, render_template, request
from flask_demo.init_db import InitDB

app = Flask(__name__)


@app.route('/')
def home():
    """首页接口"""

    # 调用初始化数据库方法
    initdb = InitDB()
    db = initdb.init_db()
    cursor = db.cursor()
    # sql语句
    sql = """SELECT count(*) num FROM `movies250`"""
    cursor.execute(sql)
    data = cursor.fetchmany()[0][0]
    return render_template("index.html", num=data)


@app.route('/index')
def index():
    """首页接口"""
    return home()


@app.route('/movie',methods=['GET','POST'])
def movie():
    """电影页接口"""

    # 获取page参数
    if request.method == 'GET':
        if request.args.get('page') == None:
            page = 1
        else:
            page = int(request.args.get('page'))
    elif request.method == 'POST':
        page = request.form.get('page')
    datalist = []

    # 初始化数据库
    initdb = InitDB()
    db = initdb.init_db()
    cursor = db.cursor()

    # sql语句
    sql = """
    select * from movies250 limit %d , %d
    """%((page-1)*25,25)
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        datalist.append(item)
    cursor.close()
    db.close()
    return render_template("movie.html", movies=datalist)


@app.route('/team')
def team():
    """团队页接口"""
    return render_template("team.html")


@app.route('/score')
def score():
    """评分页接口"""
    scorelist = []
    numlist = []

    # 初始化数据库
    initdb = InitDB()
    db = initdb.init_db()
    cursor = db.cursor()

    # sql语句
    sql = """
        SELECT score,count(*) num FROM `movies250` GROUP BY score;
        """
    cursor.execute(sql)
    data = cursor.fetchmany(250)
    for item in data:
        scorelist.append(item[0])
        numlist.append(item[1])
    cursor.close()
    db.close()
    return render_template("score.html", score=scorelist, num=numlist)


@app.route('/word')
def word():
    """词云页接口"""
    return render_template("word.html")


if __name__ == '__main__':
    app.run(debug=True)
