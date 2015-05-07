# coding=utf-8
from django.contrib import admin
from models import UserAccount, TaobaoAccount, Settings, BatchImport


# 批量修改淘宝账号密码
def modifyPassword(modeladmin, request, queryset):
    new_password = Settings.objects.get(id=1).taobao_password_modify
    queryset.update(taobao_password=new_password)


# 批量分配给用户
def fenpeiUseraccount(modelamdin, request, queryset):
    new_useraccount = Settings.objects.get(id=1).fenpei_useraccount
    queryset.update(user_account=new_useraccount)

modifyPassword.short_description = u'批量修改密码'
fenpeiUseraccount.short_description = u'把淘宝账号批量分配给用户'


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'createTime', 'lastModifyTime', 'remark')
    ording = ('-createTime',)
    list_per_page = 100
    list_filter = ('createTime',)
    search_fields = ['username', 'remark']


class TaobaoAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'taobao_username', 'taobao_password', 'user_account', 'createTime', 'lastModifyTime', 'remark')
    ording = ('-createTime')
    list_per_page = 100
    list_filter = ('createTime',)
    search_fields = ['taobao_username', 'remark']
    actions = (modifyPassword, fenpeiUseraccount)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'taobao_password_modify')

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(TaobaoAccount, TaobaoAccountAdmin)
admin.site.register(Settings)
admin.site.register(BatchImport)
