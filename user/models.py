from django.db        import models

class User(models.Model):
    fullname    = models.CharField(max_length=20)
    email       = models.EmailField()
    password    = models.CharField(max_length=200)
    event_code  = models.CharField(max_length=6)
    maker_info  = models.ForeignKey('MakerInfo', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'users'

class MakerInfo(models.Model):
    name                 = models.CharField(max_length=20)
    reputation_level     = models.DecimalField(max_digits=2, decimal_places=1) 
    communication_level  = models.DecimalField(max_digits=2, decimal_places=1)
    popularity_level     = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        db_table = 'makers_info'
