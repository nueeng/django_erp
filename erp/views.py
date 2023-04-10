from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # form?
from django.http import HttpResponse

from erp.models import Product, Inbound, Outbound, Inventory

# Create your views here.
def home(request): # 유저 검증해서 상품리스트로 우선 보내기? 따라해놨음 없애도 되는건지 잘 모르겠다.
    user = request.user.is_authenticated
    if user:
        return redirect('/product_list')
    else:
        return redirect('/sign-in')

@login_required
def product_list(request): # 상품리스트
    if request.method == 'GET':
        """상품 조회"""
        products = Product.objects.all()
        data = []

        for product in products:
            data.append({
                "코드": product.code,
                "상품명": product.name,
                "상품설명": product.description,
                "가격": product.price,
                "사이즈": product.size,
            })
        """
        django rest framework 사용 시
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
        """
        # return HttpResponse(data)
        
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
        code = request.POST.get("code","")
        name = request.POST.get("name","")
        description = request.POST.get("description","")
        price = request.POST.get("price", 0) # 기본값 지정, 가격은 0으로
        size = request.POST.get("size","")

        if Product.objects.filter(code=code).exists(): # 새로운 상품코드를 써도 이미 존재한다고 뜨는 버그..
            return HttpResponse("이미 존재하는 상품코드 입니다.") # 또 input tag에 name이 빠져서 안됬었다.

        if size == "Size": # 지금은 선택방식이니까 가능하지, 더 좋은 코드 찾아보기
            return HttpResponse("Size를 골라주세요.")

        product = Product.objects.create(
            code = code,
            name = name,
            description = description,
            price = price,
            size = size,
        )

        Inventory.objects.create(
            product = product,
            amount = 0,
        )

        return HttpResponse("상품이 생성되었습니다.")
        
@login_required
# @transaction.atomic 나중에 공부..
def inbound_create(request): # 입고
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'erp/inbound_create.html')
        else:
            return redirect('/sign-in')
    
    # elif request.method == 'POST':

    code = request.POST.get("code", "")

    try:
        product = Product.objects.get(code=code)
    except Product.DoesNotExist:
        return HttpResponse("존재하지 않는 상품코드 입니다.")
    
    amount = request.POST.get("amount", 0) # 밑에서 += 할꺼니까 정수처리
    if not amount.isdigit():
        return HttpResponse("잘못 된 수량을 입력했습니다.")
    
    amount = int(amount)

    price = int(request.POST.get("price", 0))

    Inbound.objects.create(
        product=product,
        amount=amount,
        price=price,
    )

    product.inventory.amount += amount # 이게 역참조 OnetoOne
    product.inventory.save()

    return HttpResponse("입고 완료")
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

    code = request.POST.get("code", "")
    amount = int(request.POST.get("amount", 0)) # 아래 음수 조건문 확인하기 위해 입고와 달리 먼저 선언해줘야했음 ....  

    try:
        product = Product.objects.get(code=code)
    except Product.DoesNotExist:
        return HttpResponse("존재하지 않는 상품코드 입니다.")
    
    if product.inventory.amount < amount:
        return HttpResponse("출고 수량은 현재 수량보다 많을 수 없습니다.")

    price = int(request.POST.get("price", 0))

    Outbound.objects.create(
        product=product,
        amount=amount,
        price=price,
    )

    product.inventory.amount -= amount # 이게 역참조 OnetoOne
    product.inventory.save()

    return HttpResponse("출고 완료")

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
