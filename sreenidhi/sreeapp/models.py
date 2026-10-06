from django.db import models
from django.contrib import admin
class vehicle_py(models.Model):
    vehicle_number=models.CharField(max_length=10)
    vehicle_model=models.CharField(max_length=15)
    date=models.DateField()
    day=models.CharField(max_length=10)
    owner_name=models.CharField(max_length=15)
    owner_num=models.IntegerField()
    owner_address=models.TextField()
    amount=models.IntegerField()
class vehicleAdmin(admin.ModelAdmin):
    list_display=["vehicle_number","vehicle_model","date","day","owner_name","owner_num","owner_address","amount"]
