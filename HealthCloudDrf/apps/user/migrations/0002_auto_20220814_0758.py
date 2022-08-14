# Generated by Django 3.2.15 on 2022-08-14 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='用户名')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号码')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('sex', models.IntegerField(blank=True, choices=[(0, '男'), (1, '女')], null=True, verbose_name='性别')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]