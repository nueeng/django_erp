from django.db import models


# Create your models here.
class Product(models.Model):
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    class Meta:
        db_table = "product"

    SIZES = ( # 이런 상수는 대문자로도 많이 씀
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    code = models.CharField("코드", max_length=20, unique=True) # 상품 코드는 unique True로 지정!
    name = models.CharField("상품이름", max_length=20) # 한글로된 str은 verbose name이라고함 없어도 되는데 있으면 admin에서 한글로 보여서 편함
    description = models.TextField("상품설명")
    price = models.IntegerField() # PositiveIntegerField로 하면 양수로 가능
    size = models.CharField(choices=SIZES, max_length=10) # XL 추가 시 에러나니까 넉넉하게 잡아줘도 됨
    """
    choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로 
    해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다. 
    변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
    두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.
    """

    # def __str__(self):
    #     pass
    #     return self.code

    # def save(self, *args, **kwargs):
    #     pass
    #     # 생성될 때 stock quantity를 0으로 초기화 로직

class Inventory(models.Model):
    """
    창고의 제품과 수량 정보를 담는 모델입니다.
    상품, 수량 필드를 작성합니다.
    작성한 Product 모델을 OneToOne 관계로 작성합시다.
    """ # 노션 코드복사할 때 조심하자 탭으로 되어있었음
    class Meta:
        db_table = "inventory"

    product = models.OneToOneField(Product, on_delete=models.CASCADE) #  원래는 related_name= 지정해줘야함 역참조?? CASCADE는 product가 사라지면 이거도 날려버리겠다. 삭제되더라도 유지해야할 경우에는 setNULL을 사용
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True) # 이 코드가 위의 코드랑 같은 코드임!
    amount = models.PositiveIntegerField("상품수량") # 이것도 verbose 네임

class Inbound(models.Model):
    """
    입고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    class Meta:
        db_table = "inbound"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField("입고수량")
    created_at = models.DateTimeField(auto_now_add=True) # 데이터가 생성된 순간을 기록하겠다고 이해하면 . 
    # updated_at = models.DateTimeField(auto_now=True) # add가 빠지면 수정할 때도 같이 기록됨
    price = models.PositiveIntegerField("입고가격")
    
class Outbound(models.Model):
    """
    출고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
    class Meta:
        db_table = "outbound"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField("출고수량")
    created_at = models.DateTimeField(auto_now_add=True) # 데이터가 생성된 순간을 기록하겠다고 이해하면 . 
    # updated_at = models.DateTimeField(auto_now=True) # add가 빠지면 수정할 때도 같이 기록됨
    price = models.PositiveIntegerField("출고가격")
