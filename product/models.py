from django.db        import models
from user.models      import User
from community.models import Comment

class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Reward(models.Model):
    name            = models.CharField(max_length=150)
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    combination     = models.CharField(max_length=100)
    stock           = models.IntegerField()

    class Meta:
        db_table = 'rewards'

class Promotion(models.Model):
    name       = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date   = models.DateTimeField()

    class Meta:
        db_table = 'promotions'

class Product(models.Model):
    title           = models.CharField(max_length=150)
    goal_amount     = models.DecimalField(max_digits=10, decimal_places=2)
    opening_date    = models.DateTimeField()
    closing_date    = models.DateTimeField()
    thumbnail_url   = models.TextField(max_length=2000)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    category        = models.ForeignKey('Category', on_delete=models.CASCADE)
    story           = models.TextField()
    comment         = models.ForeignKey('community.Comment', on_delete=models.CASCADE, null=True)
    reward          = models.ForeignKey('Reward', on_delete=models.CASCADE)
    promotion       = models.ForeignKey('Promotion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class LikeUser(models.Model):
    user      = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes_users'
