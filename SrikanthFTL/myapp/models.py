from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=10,unique=True)
    real_name = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User,related_name='activities', on_delete=models.CASCADE)
    start_time= models.DateTimeField()
    end_time = models.DateTimeField()


