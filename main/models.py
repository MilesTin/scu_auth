from django.db import models

class student(models.Model):

    id = models.CharField(verbose_name='学号', max_length=100,primary_key=True)
    password = models.CharField(verbose_name='密码', max_length=200)

    class Meta:
        verbose_name = '学生'

