import jieba    # 分词

from matplotlib import pyplot as plt   # 绘图，数据可视化
from wordcloud import WordCloud       # 词云
from PIL import Image        # 图片处理
import numpy as np      # 矩阵运算
import pymysql

from flask_demo.init_db import InitDB


word_str = ''

# 初始化数据库
initdb = InitDB()
db = initdb.init_db()
cursor = db.cursor()

# sql语句
sql = """select instroduction from movies250"""
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    word_str += i[0].replace("。", '').replace("，",'').replace(" ",'').replace("的",'')
cursor.close()
db.close()

# 生成词组
cut = jieba.cut(word_str)
string = ' '.join(cut)

# 处理图片
img = Image.open(r'wc_img.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="STXINGKA.TTF"
)
wc.generate_from_text(string)


# 生成词云图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

# 展示图片
# plt.show()

# 保存图片
plt.savefig("static\img\word_img.jpg", dpi=1500)