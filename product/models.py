from django.db         import models
from user.models       import (
    User, 
    MakerInfo
)

class Category(models.Model):
    name    = models.CharField(max_length=45)
    product = models.ManyToManyField('Product')

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    title           = models.CharField(max_length=150)
    goal_amount     = models.DecimalField(max_digits=10, decimal_places=2)
    opening_date    = models.DateTimeField()
    closing_date    = models.DateTimeField()
    thumbnail_url   = models.TextField()
    description     = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    story           = models.TextField()
    maker_info      = models.ForeignKey('user.MakerInfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Reward(models.Model):
    name            = models.CharField(max_length=150)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    combination     = models.CharField(max_length=100)
    stock           = models.IntegerField()
    product         = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'rewards'

class Promotion(models.Model):
    name       = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date   = models.DateTimeField()
    product    = models.ManyToManyField('Product')

    class Meta:
        db_table = 'promotions'

class LikeUser(models.Model):
    user      = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes_users'
