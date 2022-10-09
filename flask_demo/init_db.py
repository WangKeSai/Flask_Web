import pymysql


class InitDB:
    def init_db(self):
        try:
            db = pymysql.connect(
                host="localhost",
                user="root",
                passwd="123456",
                db="movies",
            )
            return db
        except Exception:
            raise Exception("数据库连接失败！")