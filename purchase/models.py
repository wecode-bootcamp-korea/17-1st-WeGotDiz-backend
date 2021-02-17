from django.db      import models
from product.models import Reward
from user.models    import User

class Address(models.Model):
    address           = models.CharField(max_length=250)
    user              = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True) # 회사 : 탈퇴한 회원의 배송 주소는 보여줘야 한다

    class Meta:
        db_table = 'addresses'

class Order(models.Model):
    order_number      = models.CharField(max_length=150)
    fullname          = models.CharField(max_length=45)
    contact_number    = models.CharField(max_length=20)
    delivery_note     = models.CharField(max_length=50, null=True)
    card_number       = models.CharField(max_length=250) # 멘토님께 여쭤보기
    card_password     = models.CharField(max_length=250)
    card_expire       = models.CharField(max_length=5)
    delivery_fee      = models.DecimalField(max_digits=10, decimal_places=2)
    donation          = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    date_of_birth     = models.DateTimeField()
    created_at        = models.DateTimeField(auto_now_add=True)
    address           = models.ForeignKey('Address', on_delete=models.PROTECT) #exists -> get or create
    order_status      = models.CharField(max_length=45, default='배송준비중')
    reward            = models.ManyToManyField('product.Reward', through='RewardOrder', through_fields=('reward', 'order'))

    class Meta:
        db_table = 'orders'
    
class RewardOrder(models.Model): # 펀딩하기 아이템/주문하기 - 수량 체크 펀딩
    reward      = models.ForeignKey('product.Reward', on_delete=models.PROTECT) # 내일 생각하기
    order       = models.ForeignKey('Order', on_delete=models.PROTECT) # 내일 생각하기
    quantity    = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'rewards_orders'


