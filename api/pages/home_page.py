# coding:utf-8

import unittest, re, json, cx_Oracle, urllib3, os, warnings, requests

warnings.filterwarnings("ignore")

urllib3.disable_warnings()

s = requests.session()

token = 'Bearer 82beccbb-cd3a-4e9e-bf52-3036b8a3e1f1'
host = 'https://jwc1.yos168.com'
phone = '17267088535'


class Login(unittest.TestCase):

    def login(self):
        """登录"""

        url = host + "/auth/api/auth2u/token"

        payload = 'grant_type=password&client_type=h5'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ODMzNDUwOjk2ZTc5MjE4OTY1ZWI3MmM5MmE1NDlkZDVhMzMwMTEy'
        }

        response = s.post(url, headers=headers, data=payload)
        print(response.text)
        self.get_access_toke = re.findall('"access_token":"(.+?)","token_type', response.content.decode("utf-8"))[0]
        print(self.get_access_toke)

    def get_tu(self):
        '''修改头像'''
        url = host + "/apis/common/v1/users/uploadTopPicture?_t=1652231788129 "
        parpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 定位当前文件夹
        jpgpath = os.path.join(parpath, 'imges', 'yy.png')  # “testdata”：存放文件的文件夹名，“1.jpg”：文件名
        img_name = 'yy.png'
        payload = {}
        files = [
            ('topPicture', ('yy.png', open(jpgpath, 'rb'), 'image/png'))
        ]
        # with open(jpgpath,'rb') as f_abs:# 以2进制方式打开图片
        #     files = {'topPicture':f_abs}

        headers = {
            # 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryMrbBABmbp0n5bw2u',
            'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        warnings.simplefilter('ignore', ResourceWarning)
        print(response.text)

    def get_code(self):
        '''获取验证码'''
        url = host + "/apis/common/v1/sms/verifycode?phone=" + phone + "&type=2&_t=1653111871307"

        payload = {}
        headers = {
            'Authorization': token,
            'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)

        '''查询数据库的验证码'''
        connection = cx_Oracle.connect('query_user', 'query_user', '172.16.100.74:1521/lotsdb')
        cur = connection.cursor()

        sql = "select securitycode from lots.CONFIG_SYS_PHONECHECK WHERE PHONENUMBER=" + phone + " ORDER BY securitycodesendtime desc".format(
            ['securitycode'])
        cur.execute(sql)
        result = cur.fetchone()

        self.str = ''.join(result)

        print("验证码为%s" % self.str)

    def change_password(self):
        '''重置密码'''
        url = host + "/apis/common/v1/users/updateUserPwd?_t=1653123127465"

        payload = json.dumps({
            "pwd": "96e79218965eb72c92a549dd5a330112",
            "code": self.str
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)

    def change_contact(self):
        '''修改联系人'''
        url = host + "/apis/common/v1/users/updateUserLinkMan"

        payload = json.dumps({
            "linkMan": "斑马"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)
