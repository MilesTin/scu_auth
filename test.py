import requests
from PIL import Image
import os
import json

stuId = "2017141461248"
password = 'tmzqq520..'
root = 'http://127.0.0.1:8000/'
root_ = 'http://127.0.0.1:8000'
if __name__=="__main__":
    domain = root + "auth/"
    session = requests.session()
    res = session.get(domain+"getCaptcha")
    res_json = res.json()
    print(res_json)

    ir = session.get(root_+res_json['img_url'])
    print("验证码:",ir.status_code)
    if ir.status_code==200:
        open("temp.jpg","wb").write(ir.content)
    else:
        exit()
    img = Image.open("temp.jpg")
    img.show()
    captcha = input("please enter the captcha code:")
    data = {
        'stuId':stuId,
        'passwd':password,
        'captcha':captcha,
    }

    res = session.post(domain+"login", data=data)
    print("login:",res.status_code)
    cookies = session.get(domain+"getCookies")
    print(cookies)
    with open("cookies.json","w") as f:
        f.write(cookies.text)

