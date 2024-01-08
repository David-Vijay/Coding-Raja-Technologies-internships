from django.db import models
import os, datetime
from django.contrib.auth.models import User
# Create your models here.

def getFilename(request, filename):
    now_time= datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename= "%s%s"%(now_time, filename)
    return os.path.join('uploads/',new_filename)

class cat(models.Model):
    name=models.CharField(max_length=122, null=False, blank=False)
    image=models.ImageField(upload_to=getFilename, null=True, blank=True)
    description=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False, help_text='0-show, 1-Hidden')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name
    
class pro(models.Model):
    category=models.ForeignKey(cat,on_delete=models.CASCADE)
    name=models.CharField(max_length=122, null=False, blank=False)
    vendor=models.CharField(max_length=122, null=False, blank=False)

    product_image=models.ImageField(upload_to=getFilename, null=True, blank=True)
    quantity=models.IntegerField(null=False, blank=False)
    original_price=models.FloatField(null=False, blank=False)
    selling_price=models.FloatField(null=False, blank=False)
    description=models.TextField(max_length=500, null=False, blank=False)
    status=models.BooleanField(default=False, help_text='0-show, 1-Hidden')
    trending=models.BooleanField(default=False, help_text='0-default, 1-Trending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(pro, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False, blank=False)
    
    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price

 