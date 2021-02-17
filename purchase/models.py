from django.db      import models
from product.models import Reward
from user.models    import User

class Address(models.Model):
    address           = models.CharField(max_length=250)
    user              = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True) # 회사 : 탈퇴한 회원의 배송 주소는 보여줘야 한다

    class Meta:
        db_table = 'addresses'

class Order(models.Model):
    fullname          = models.CharField(max_length=45) #POST FULL NAME
    contact_number    = models.CharField(max_length=20)
    delivery_note     = models.CharField(max_length=50, null=True)
    delivery_fee      = models.DecimalField(max_digits=10, decimal_places=2, default=2500) 
    donation          = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    address           = models.ForeignKey('Address', on_delete=models.PROTECT) #exists -> get or create
    order_status      = models.CharField(max_length=45, default='결제완료') # 이거 꼭 해야 함?
    reward            = models.ManyToManyField('product.Reward', through='RewardOrder') 
    user              = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'

class RewardOrder(models.Model): # 펀딩하기 아이템/주문하기 - 수량 체크 펀딩
    reward      = models.ForeignKey('product.Reward', on_delete=models.PROTECT) 
    order       = models.ForeignKey('Order', on_delete=models.PROTECT) 
    quantity    = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'rewards_orders'

