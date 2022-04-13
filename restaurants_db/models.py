from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
import datetime
import uuid

# Create your models here.   

class Restaurant(models.Model):
    REGION_CHOICES = [("NT","New Territories"),
    ("KLN","Kowloon"),
    ("HK","Hong Kong Island"),]

    DISTRICT_CHOICES =[
        ("CW","Central and Western"),
        ("EA","Eastern"),
        ("IS","Islands"),
        ("KC","Kowloon City"),
        ("KI","Kwai Tsing"),
        ("KU","Kwun Tong"),
        ("NO","North"),
        ("SK","Sai Kung"),
        ("SS","Sham Shui Po"),
        ("ST","Sha Tin"),
        ("SO","Southern"),
        ("TP","Tai Po"),
        ("TW","Tsuen Wan"),
        ("TM","Tuen Mun"),
        ("WC","Wan Chai"),
        ("WT","Wong Tai Sin"),
        ("YT","Yau Tsim Mong"),
        ("YL","Yuen Long")]


    name = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    region = models.CharField(max_length=3,choices=REGION_CHOICES,default="NT")
    district = models.CharField(max_length=2,choices=DISTRICT_CHOICES,default="SK")

    cuisine = models.CharField('cuisine type',max_length=100)

    price_range_low = models.IntegerField(default=0)
    price_range_high = models.IntegerField(default=1000)

    open_rice_url = models.URLField()

    lat = models.FloatField('latitude')
    lng = models.FloatField('longitude')
    point =models.PointField(srid = 4326, null=True)

    business_hours_from = models.TimeField(default=datetime.time(10,0))
    business_hours_to = models.TimeField(default=datetime.time(21,0))

    def save(self,*args,**kwargs):
        self.point = Point(lng,lat)
        super(Restaurant,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
