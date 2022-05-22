
import os

import requests

'''修改头像'''
url = "https://jwc1.yos168.com/apis/common/v1/users/uploadTopPicture?_t=1652231788129 "
parpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 定位当前文件夹
jpgpath = os.path.join(parpath, 'imges', '../imges/yy.png')  # “testdata”：存放文件的文件夹名，“1.jpg”：文件名
img_name = 'yy.png'
payload = {}

files = [
    ('topPicture', ('yy.png', open(jpgpath, 'rb'), 'image/png'))

]




# with open((jpgpath, 'rb'), 'image/png') as fo:  # 打开文件，执行完后可自动关闭
#     files = {'topPicture': fo}

headers = {
    # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryMrbBABmbp0n5bw2u',
    'Authorization': 'Bearer 82beccbb-cd3a-4e9e-bf52-3036b8a3e1f1'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)