import json
import requests

cookies = None

with open("cookies.json") as f:
    cookies = json.load(f)

session = requests.session()

res = session.get("http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index", cookies=cookies)

if res.status_code==200 and res.url=="http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index" and "2017141461248" in res.text:
    print("logged in ")
res = requests.get("http://zhjw.scu.edu.cn/", cookies=cookies)

