import json
import requests

cookies = None

with open("cookies.json") as f:
    cookies = json.load(f)

session = requests.session()

res = session.get("http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index", cookies=cookies)

if res.status_code==200 and res.url=="http://zhjw.scu.edu.cn/student/rollManagement/rollInfo/index" and "2017141461248" in res.text:
    print("logged in ")
else:
    print("not logged in")
    exit()

res = session.post("http://zhjw.scu.edu.cn/student/teachingEvaluation/teachingEvaluation/search", cookies=cookies)
data = res.json()
with open("data","w") as f:
    json.dump(data, f)



