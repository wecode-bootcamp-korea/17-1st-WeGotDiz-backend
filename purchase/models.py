from django.db      import models
from product.models import Reward
from user.models    import User

class Address(models.Model):
    address           = models.CharField(max_length=250)
    user              = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True) 

    class Meta:
        db_table = 'addresses'

class Order(models.Model):
    fullname          = models.CharField(max_length=45) 
    contact_number    = models.CharField(max_length=20)
    delivery_note     = models.CharField(max_length=50, null=True)
    total_amount      = models.DecimalField(max_digits=10, decimal_places=2) 
    delivery_fee      = models.DecimalField(max_digits=10, decimal_places=2, default=2500) 
    donation          = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    address           = models.ForeignKey('Address', on_delete=models.PROTECT) 
    order_status      = models.CharField(max_length=45, default='결제완료') 
    reward            = models.ManyToManyField('product.Reward', through='RewardOrder') 
    user              = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'orders'

class RewardOrder(models.Model):
    reward      = models.ForeignKey('product.Reward', on_delete=models.PROTECT) 
    order       = models.ForeignKey('Order', on_delete=models.PROTECT) 
    quantity    = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'rewards_orders'

