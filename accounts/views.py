from django.shortcuts import render, redirect # redirect 추가
from .models import AccountModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth

# Create your views here.

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return HttpResponse(f"{me.username}가 로그인에 성공!")
        else:
            return redirect('/sign-in')
    
    elif request.method == 'GET':
        return render(request, 'accounts/sign_in.html')
    

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if password != password2:
            return render(request, 'accounts/sign_up.html', {'error':'비밀번호가 다릅니다.'})
        else:
            if username == '' or password =='':
                return render(request, 'accounts/sign_up.html',{'error':'ID와 비밀번호를 입력해주세요'})
            
            exist_account = get_user_model().objects.filter(username=username) # get_user_model()은 장고의 auth기본제공함수
            if exist_account: # 1시간 고민 근데 또 회원가입시 저장 안되는 것 같다.. 어디서 오류인지도 모르겠음
                return render(request, 'accounts/sign_up.html', {'error':'같은 ID가 존재합니다.'}) # 여기 부분이 문제임 비밀번호 다르게해도 이 멘트가 뜸
            else:
                AccountModel.objects.create_user(username=username, password=password, email=email, name=name) # create_user도 장고의 auth기본제공함수
                return redirect('/sign-in') # render랑 redirect랑 어떤식으로 다른건지.?
