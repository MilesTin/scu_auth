import requests
from PIL import Image
import os
import json

stuId = "*"
password = '*'
root = 'http://127.0.0.1:8000/'

if __name__=="__main__":
    domain = root + "auth/"
    session = requests.session()
    res = session.get(domain+"getCaptcha")
    res_json = json.loads(res.text)


    ir = session.get(root+res_json['img_url'])

    open("temp.jpg","wb").write(ir.content)
    img = Image.open("temp.jpg")
    img.show()
    captcha = input("please enter the captcha code:")
    data = {
        'stuId':stuId,
        'passwd':password,
        'captcha':captcha,
    }

    res = session.post(domain+"login", data=data)
    print(res.status_code)
    res = session.get(domain+"logout")
    print(res.status_code)