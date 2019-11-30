from django.test import TestCase
from PIL import Image
# Create your tests here.
class AccountTestCase(TestCase):


    def setUp(self) -> None:
        self.stuId = "2017141461248"
        self.password = "tmzqq520.."


    def test_get_captcha(self):
        res = self.client.get('/auth/getCaptcha')

        res_json = res.json()
        self.assertTrue(res.status_code==200)
        self.img_url = res_json['img_url']
        self.assertTrue(self.img_url)#假设img_url不为空

    def test_login(self):

        self.test_get_captcha()
        print("img_url: "+self.img_url)

        res = self.client.get(self.img_url)
        print(res.content)
        self.assertTrue(res.status_code==200)

        with open("test_temp.jpg","wb") as fp:
            fp.write(res.content)
        img = Image.open("test_temp.jpg")
        img.show()
        captcha = input("please enter the captcha:")
        self.captcha = captcha

        data = {
            "stuId":self.stuId,
            "password":self.password,
            "captcha":captcha,
        }
        res = self.client.post("/auth/login", data=data)
        print(res.text)
        self.assertTrue(res.status_code==200)

    def test_logout(self):
        pass