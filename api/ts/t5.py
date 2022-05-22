# 获取文件路径
import os

parpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 定位当前文件夹
jpgpath = os.path.join(parpath, 'images', '3310.png')    # “testdata”：存放文件的文件夹名，“1.jpg”：文件名
# print(parpath)
print(jpgpath)

cur_path = os.path.dirname(os.path.realpath(__file__))
# print(cur_path)