from django.db      import models
# from product.models import Product
from user.models    import User

class Comment(models.Model):
    user       = models.ForeignKey('user.User', on_delete=models.CASCADE)
    text       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent     = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='reply')

    class Meta:
        db_table = 'comments'
    
