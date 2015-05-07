# coding=utf-8
from django.db import models


class UserAccount(models.Model):
    username = models.CharField(u'用户账号', max_length=30, null=True, blank=True, unique=True)
    password = models.CharField(u'用户密码', max_length=30, null=True, blank=True)
    createTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    lastModifyTime = models.DateTimeField(u'最后修改时间', auto_now=True)
    remark = models.CharField(u'备注', max_length=200, blank=True)

    class Meta:
        verbose_name = u'用户账号'
        verbose_name_plural = u'用户账号'

    def __unicode__(self):
        return self.username


class TaobaoAccount(models.Model):
    taobao_username = models.CharField(u'淘宝账号', max_length=30, null=True, blank=True , unique=True)
    taobao_password = models.CharField(u'淘宝密码', max_length=30, null=True, blank=True)
    user_account = models.ForeignKey('UserAccount', verbose_name='所属用户', null=True, blank=True)
    createTime = models.DateTimeField(u'创建时间', auto_now_add=True)
    lastModifyTime = models.DateTimeField(u'最后修改时间', auto_now=True)
    remark = models.CharField(u'备注', max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = u'淘宝账号'
        verbose_name_plural = u'淘宝账号'

    def __unicode__(self):
        return self.taobao_username


class Settings(models.Model):
    taobao_password_modify = models.CharField(u'淘宝密码修改', max_length=30, null=True, blank=True)
    fenpei_useraccount = models.ForeignKey('UserAccount', verbose_name='批量分配给用户', null=True, blank=True)

    class Meta:
        verbose_name = u'设置'
        verbose_name_plural = u'设置'

    def __unicode__(self):
        return str(self.id)


class BatchImport(models.Model):
    batch_import = models.TextField(u'批量导入淘宝账号密码', max_length=2000, help_text=u'允许输入的最大字符数为<em>2000</em><br>请不要重复保存!!')

    def save(self, *args, **kw):
        super(BatchImport, self).save(*args, **kw)
        uname_and_pwds = self.batch_import.split(u'\n')
        for uname_and_pwd in uname_and_pwds:
            uname = uname_and_pwd.split('----')[0].replace(' ', '')
            pwd = uname_and_pwd.split('----')[1].replace(' ', '')
            taobao_account = TaobaoAccount(taobao_username=uname, taobao_password=pwd)
            taobao_account.save()

    class Meta:
        verbose_name = u'批量导入'
        verbose_name_plural = u'批量导入淘宝账号密码'

    def __unicode__(self):
        return u'批量导入'
