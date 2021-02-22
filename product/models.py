from django.db         import models
from user.models       import (
    User, 
    MakerInfo
)

class Category(models.Model):
    name    = models.CharField(max_length=45)
    product = models.ManyToManyField('Product')
    image   = models.URLField(max_length=2000)

    class Meta:
        db_table = 'categories'

class Product(models.Model): # 탭 전환 reference_table 
    title              = models.CharField(max_length=150)
    thumbnail_url      = models.URLField(max_length=2000)
    description        = models.TextField()
    goal_amount        = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount       = models.DecimalField(max_digits=10, decimal_places=2)
    achieved_rate      = models.DecimalField(max_digits=10, decimal_places=2)
    total_supporters   = models.IntegerField()
    total_likes        = models.PositiveIntegerField()
    opening_date       = models.DateTimeField()
    closing_date       = models.DateTimeField()
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)
    maker_info         = models.ForeignKey('user.MakerInfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Reward(models.Model):
    name               = models.CharField(max_length=150)
    price              = models.DecimalField(max_digits=10, decimal_places=2)
    combination        = models.CharField(max_length=100, null=True)
    stock              = models.IntegerField()
    quantity_sold      = models.PositiveIntegerField(max_length=10)
    product            = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'rewards'

class Collection(models.Model):
    name       = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date   = models.DateTimeField()
    product    = models.ManyToManyField('Product')

    class Meta:
        db_table = 'collections'

class LikeUser(models.Model):
    user      = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes_users'

class ProductContent(models.Model):
    name        = models.CharField(max_length=100)
    content     = models.TextField()  # BLOB DATA
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_contents'
    