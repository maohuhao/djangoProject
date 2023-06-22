import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


class Login(View):
    def get(self, request):
        error = request.session.pop('error', '')

        return render(request, 'login.html', context={'error': error})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            auth.login(request, user)
            return redirect('index')

        request.session['error'] = '用户名或密码错误'
        return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login')


def send_email(request):
    email = request.POST.get("email")
    if email:
        import random
        code = str(random.randint(100000,999999)) #生成随机六位数的验证码
        subject = '邮箱验证码'
        message = '你的邮箱验证码是：' + code
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email,]
        send_mail(subject, message, email_from, recipient_list)
        return JsonResponse({'status': 'success', 'msg': '邮件已发送，请注意查收'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '请输入邮箱地址'})

@login_required(login_url='/login/')
def index(request):
    res = request.user

    return HttpResponse('ok')
