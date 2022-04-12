from django.db import models

from restaurants_db.models import Restaurant
import uuid


class User (models.Model):
    name = models.CharField(max_length = 50)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    country_code = models.CharField(default='852', max_length = 10)
    phone_number = models.CharField(max_length = 20, default='')
    g_cash = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Record (models.Model):
    RECORD_TYPE_CHOICES = [('B','BORROW'),('R','RETURN'),('T','TOP UP')]

    user = models.ForeignKey(User, on_delete =models.CASCADE, null = True)
    record_type = models.CharField(max_length=1, choices=RECORD_TYPE_CHOICES, null =True)

    date_time = models.DateTimeField('Completed time')
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE, null=True)

    balance_delta = models.IntegerField('value change on balance',default = 10)
    g_cash_delta = models.IntegerField('value change on g-cash',default = 0)

    def __str__(self):
        return self.date_time.strftime("%m/%d/%Y, %H:%M:%S")+' '+self.user.name


    class Meta:
        ordering = ["date_time"]




    
