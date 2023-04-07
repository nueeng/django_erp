from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/product_list')
    else:
        return redirect('/sign-in')

def product_list(request): # 리스트
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/product_list.html')
        else:
            return redirect('/sign-in')

def product_create(request): # 상품등록
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/product_create.html')
        else:
            return redirect('/sign-in')
        
def inbound_create(request): # 입고
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/inbound_create.html')
        else:
            return redirect('/sign-in')
        
def outbound_create(request): # 출고
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/outbound_create.html')
        else:
            return redirect('/sign-in')
        
def inventory(request): # 재고현황
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/inventory.html')
        else:
            return redirect('/sign-in')