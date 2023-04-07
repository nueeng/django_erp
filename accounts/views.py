from django.shortcuts import render, redirect # redirect 추가
from .models import AccountModel
from django.http import HttpResponse

# Create your views here.

def sign_in_view(request):
    if request.method == 'POST':
        account_id = request.POST.get('account_id', None)
        password = request.POST.get('password', None)

        me = AccountModel.objects.get(account_id=account_id)
        if me.password == password:
            request.session['account_id'] = me.account_id
            return HttpResponse(f"{me.account_id}가 로그인에 성공!")
        else:
            return redirect('/sign-in')
    
    elif request.method == 'GET':
        return render(request, 'accounts/sign_in.html')
    
    

def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html')
    elif request.method == 'POST':
        account_id = request.POST.get('account_id', None)
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            return render(request, 'accounts/sign_up.html')
        else:
            exist_account = AccountModel.objects.filter(account_id=account_id)

            if exist_account:
                return render(request, 'accounts/sign_up.html')
            else:
                new_account = AccountModel()
                new_account.account_id = account_id
                new_account.name = name
                new_account.email = email
                new_account.password = password
                return redirect('/sign-in')
