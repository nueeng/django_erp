from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request): # 유저 검증해서 상품리스트로 우선 보내기? 홈.. 따라해놨음 없애도 되는건지 잘 모르겠다.
    user = request.user.is_authenticated
    if user:
        return redirect('/product_list')
    else:
        return redirect('/sign-in')

@login_required
def product_list(request): # 상품리스트
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/product_list.html')
        else:
            return redirect('/sign-in')

@login_required
def product_create(request): # 상품등록
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/product_create.html')
        else:
            return redirect('/sign-in')

    if request.method == 'POST':
        """상품 생성"""
        
@login_required
# @transaction.atomic 나중에 공부..
def inbound_create(request): # 입고
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/inbound_create.html')
        else:
            return redirect('/sign-in')
    # 입고 기록 생성

    # 입고 수량 조정
        
@login_required
def outbound_create(request): # 출고
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/outbound_create.html')
        else:
            return redirect('/sign-in')
    # 출고 기록 생성
    
    # 재고 수량 조정

@login_required
def inventory(request): # 재고현황
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/inventory.html')
        else:
            return redirect('/sign-in')
    """
    inbound_create, outbound_create view에서 만들어진 데이터를 합산합니다.
    Django ORM을 통하여 총 수량, 가격등을 계산할 수 있습니다.
    """
    # 총 입고 수량, 가격 계산

    # 총 출고 수량, 가격 계산
