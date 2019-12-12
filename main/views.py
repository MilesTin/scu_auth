from django.shortcuts import render
import django
import urllib.request
import urllib
import platform
from django.conf import settings
import json
import requests
from PIL import Image
import os

import os
import logging
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder

logger = logging.getLogger(__name__)
#rest framework
from rest_framework.response import Response
from rest_framework.status import *
from django.http import JsonResponse
from .models import student
from hashlib import sha256
from django.views.decorators import csrf
from django.conf import settings
from hashlib import md5
# Create your models here.
class sculogin(object):
    url = "http://zhjw.scu.edu.cn/j_spring_security_check"
    img_url = "http://zhjw.scu.edu.cn/img/captcha.jpg"
    is_updated = False

    #验证码地址
    #ip + 'static/' + 'account/img/login.txt'
    cookies = None


    def getCapatcha(self, cookies=None):
        """
        :return 图片的url:
        """
        self.session = requests.Session()

        ir = self.session.get(sculogin.img_url, cookies=cookies)
        # print(ir.text)
        rel_pos = ""
        rel_url = ""
        if ir.status_code == 200:
            sha = sha256()
            sha.update(ir.content)
            front_name = sha.hexdigest()
            rel_pos = os.path.join(settings.MEDIA_ROOT, front_name+".jpg")
            rel_url = settings.MEDIA_URL + front_name + ".jpg"
            open(rel_pos, 'wb').write(ir.content)
        self.cookies = self.session.cookies
        return rel_url

    def login(self,username,password,captcha:str,cookies)->bool:
        encoder = md5()
        encoder.update(password.encode('utf-8'))
        password = encoder.hexdigest()
        """
        :param captcha:
        :param username:
        :param password:
        :return bool:
        """
        self.session = requests.session()
        data = {
            'j_username':username,
            'j_password':password,
            'j_captcha':captcha,
        }
        # print(cookies)
        res = self.session.post(self.url,data=data,cookies=cookies)
        print(res.status_code)

        print("data:{}".format(data))
        # print("server request j_spring_security request url: "+res.url)

        res = self.session.get("http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index",cookies=cookies)

        if res.status_code==200 and res.url=="http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index" and username in res.text:
            return True
        print(res.url)

        return False


@csrf_exempt
def login(request):
    scuLoginer = sculogin()

    stuId = request.POST.get("stuId","")
    passwd = request.POST.get("passwd", "")
    captcha = request.POST.get("captcha", "")
    is_updated = request.session.get("is_updated",False)

    cookies = request.session.get("cookies")
    # print(stuId,passwd,captcha)
    # print(cookies)
    if not is_updated:
        return JsonResponse({"msg":"验证码未更新"}, status=HTTP_400_BAD_REQUEST)

    result = scuLoginer.login(username=stuId,password=passwd,captcha=captcha,cookies=cookies)
    request.session["is_updated"] = False
    print(result)
    if result:
        stu, _ = student.objects.get_or_create(id=stuId)
        md5_encoder = md5()
        md5_encoder.update(passwd.encode('utf-8'))
        passwd = md5_encoder.hexdigest()
        stu.password = passwd
        stu.save()
        request.session['zhjw_cookies'] = dict(scuLoginer.session.cookies)
        return JsonResponse({"msg":"绑定成功"})

    else:
        return JsonResponse({"msg":"绑定失败"}, status=HTTP_400_BAD_REQUEST)


def getCaptcha(request):
    scuLoginer = sculogin()

    rel_url = scuLoginer.getCapatcha()
    request.session["is_updated"] = True
    request.session["cookies"] = dict(scuLoginer.cookies)
    print(request.session['cookies'])
    return JsonResponse({"msg":"获取验证码成功", 'img_url': rel_url})


def get_cookies(request):
    return JsonResponse(dict(request.session['cookies']))

def logout(request):
    request.session['is_updated'] = False
    del request.session['cookies']

    return JsonResponse(data={"msg":"登出成功"})
