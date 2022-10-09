import re
from urllib import request
import sqlite3
import xlwt
import pymysql
from bs4 import BeautifulSoup


def main():
    """主函数"""

    # 网站路径
    baseurl = 'https://movie.douban.com/top250?start='
    # savepath = '豆瓣电影.xls'
    # dbpath = 'movies.db'

    # 数据库地址、用户名、密码、库名
    host = "localhost"
    user = "root"
    passwd = "123456"
    db = "movies"

    # 调用getDate方法，爬取数据
    datelist = getDate(baseurl)

    # 调用saveDate方法，将爬取到的数据存入MySQL
    saveDate(host, user, passwd, db, datelist)

# 电影链接正则
findLink = re.compile('<a href="(.*?)">', re.S)
# 图片链接正则
findImageSrc = re.compile('<img.*?src="(.*?)"', re.S)
# 电影名称正则
findTitle = re.compile('<span class="title">(.*?)</span>')
# 评分正则
findRating = re.compile('<span class="rating_num" property="v:average">(.*?)</span>')
# 评价人数正则
findJudge = re.compile('<span>(.*)人评价</span>')
# 一句话概述正则
findInq = re.compile('<span class="inq">(.*?)</span>')
# 其他信息正则
findBd = re.compile('<p class="">(.*?)</p>', re.S)


def getDate(baseurl):
    """爬取数据函数"""
    datelist = []
    print("爬取中.....")
    for i in range(0, 10):
        # 拼接url，生成完整url
        url = baseurl + str(i * 25)
        # 调用askUrl函数，爬取网站，并接受
        html = askUrl(url)
        # 使用beautifulsoup方法
        soup = BeautifulSoup(html, 'html.parser')
        # 获取各个字段信息
        for item in soup.find_all('div', class_="item"):
            date = []
            item = str(item)
            link = re.findall(findLink, item)[0]
            date.append(link)
            imageSrc = re.findall(findImageSrc, item)[0]
            date.append(imageSrc)
            title = re.findall(findTitle, item)
            ctitle = title[0]
            date.append(ctitle)
            if len(title) != 1:
                etitle = title[1].replace('/', '').strip()
            else:
                etitle = '  '
            date.append(etitle)
            rating = re.findall(findRating, item)[0].replace('。', '')
            date.append(rating)
            judge = re.findall(findJudge, item)[0]
            date.append(judge)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0]
            else:
                inq = '  '
            date.append(inq)
            bd = re.findall(findBd, item)[0].replace('<br/>', '').replace("\n", "").strip().replace(
                "                           ", "")
            date.append(bd)
            datelist.append(date)
    print("爬取完成！")
    return datelist


def saveDate(host, user, passwd, db, datelist):
    """保存数据到MySQL函数"""

    # 初始化数据库
    db = init_db(host, user, passwd, db)
    cursor = db.cursor()

    # 遍历数据，将数据存储到对应字段
    for data in datelist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        # sql插入语句
        sql = """
                INSERT INTO movies250(
                info_link, pic_link, cname, ename, score, rated, instroduction, info
                )
                VALUES (%s)""" % ",".join(data)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
    db.close()
    print("保存成功！")


def init_db(host, user, passwd, db):
    """初始化数据库函数"""
    try:
        db = pymysql.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=db,
        )
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 如果数据表已经存在使用 execute() 方法删除表。
        cursor.execute("DROP TABLE IF EXISTS movies250")

        # 创建数据表SQL语句
        sql = """CREATE TABLE movies250 (
            mid   int PRIMARY KEY AUTO_INCREMENT,
            info_link  TINYTEXT ,
            pic_link  TINYTEXT,
            cname  TINYTEXT,  
            ename  TINYTEXT,
            score  float ,
            rated  int ,
            instroduction  TINYTEXT ,
            info  TINYTEXT)"""

        cursor.execute(sql)
        return db
    except Exception:
        raise Exception("数据库连接失败！")


def askUrl(baseurl):
    """爬取网站函数"""

    # 头部信息
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
        'Cookie': 'bid=WvgHziOIkAs; __gads=ID=0beac49b99008d71-225c65bbc3d6000b:T=1664537264:RT=1664537264:S=ALNI_MZ5z9MpieFzX7WjYjjEKrREdl0uAg; ll="118094"; dbcl2="263271553:1uW+8vbpDHE"; ck=xnmw; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1664624988%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_id.100001.4cf6=cba76f4481ba9042.1664537262.4.1664624988.1664616094.; _pk_ses.100001.4cf6=*; __gpi=UID=00000a10c83cac7f:T=1664537264:RT=1664624988:S=ALNI_MY40bqOqtXZWfflZimLbW4lHHfm8w='}
    req = request.Request(baseurl, headers=head)
    respond = request.urlopen(req)
    html = respond.read().decode('utf-8')
    # print(html)
    return html


if __name__ == '__main__':
    main()
