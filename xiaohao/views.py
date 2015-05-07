# coding=utf-8
from django.http import HttpResponse
import time
from models import UserAccount, TaobaoAccount


def get(request):
    error1_response = HttpResponse('error:用户名或密码不正确')
    error1_response['Access-Control-Allow-Origin'] = '*'
    
    error2_response = HttpResponse('error:淘宝账号不正确')
    error2_response['Access-Control-Allow-Origin'] = '*'
 
    username = request.GET.get('username')  # 用户账号
    password = request.GET.get('password')  # 用户密码
    taobao_username = request.GET.get('taobao_username')  # 该用户的淘宝账号
    try:
        useraccount = UserAccount.objects.get(username=username)
        if useraccount.password != password:
            return error1_response
    except:
        return error1_response

    taobao_accounts = TaobaoAccount.objects.filter(user_account=useraccount)
    for taobao_account in taobao_accounts:
        if taobao_account.taobao_username == taobao_username:
            success_response = HttpResponse('success:' + taobao_account.taobao_password)
            success_response['Access-Control-Allow-Origin'] = '*' 
            return success_response
    return error2_response
    
