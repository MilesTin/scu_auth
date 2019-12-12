# scu_auth
四川大学教务处学号验证

<h4>主要功能</h4>
验证四川大学学生身份
<h5>django开发</h5>
<h5> python3.x </h5>
<h4>运行步骤</h4>
<ol>
  <li>python -m pip install -r requirements.txt</li>
  <li>python manage.py runserver </li>
</ol>

<h3>实例</h3>
已经部署在服务器上
<text style="font-weight:bold">https://milestin.xyz:83</text>
<h4>调用步骤</h4?
<ol>
  <li style="margin-top:10px;">获取验证码 https://milestin.xyz:83/auth/getCaptcha</li>

  <img src="https://github.com/MilesTin/scu_auth/blob/master/md_images/step1.PNG" style="margin-top:10px;"/>
  <li>登录 https://milestin.xyz:83/auth/login?stuId=*&passwd=*&captcha=* </li>
  <img src="https://github.com/MilesTin/scu_auth/blob/master/md_images/step2.png" style="margin-top:10px;"/img>
  <li> 登出 https://milestin.xyz:83/auth/logout</li>
  <img src="https://github.com/MilesTin/scu_auth/blob/master/md_images/step3.PNG" /img>

</ol>

