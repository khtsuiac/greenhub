from django.db import models
from user_db.models import User
from restaurants_db.models import Restaurant
import uuid

# Create your models here

class Reward(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    provider = models.CharField(max_length=100)
    illustration = models.ImageField(upload_to='rewards')
    cost = models.IntegerField('G-cashed needed to redeem',default = 1000)

    def __str__(self):
        return self.name

class Gift(Reward):
    pass

class Coupon(Reward):
    discount = models.IntegerField(default = 3)
    min_consume = models.IntegerField(default = 20)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)

class Reward_Record (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    redeem_id = models.UUIDField()
    status = models.CharField("ACTIVE, USED",default="ACTIVE", max_length= 5)
    redeem_date = models.DateTimeField()
    used_date =models.DateTimeField()

    
    