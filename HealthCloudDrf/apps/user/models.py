from django.db import models

# Create your models here.

class UserInfo(models.Model):
    choice = (
        (0, '男'),
        (1, '女')
    )

    name = models.CharField(null=True, blank=True, verbose_name='用户名', max_length=10)
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    phone = models.CharField(verbose_name='手机号码', max_length=11)
    password = models.CharField(verbose_name='密码', max_length=16)
    sex = models.IntegerField(verbose_name='性别', choices=choice, null=True, blank=True)
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'userinfo'