from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=255)


    class Meta:
          verbose_name_plural='categories'

    def __str__(self):
          return self.name
         
class product(models.Model):
       name=models.CharField(max_length=255)
       price=models.FloatField()
       description=models.TextField(blank=True,null=True)
       is_sold=models.BooleanField(default=False)
       created_at=models.TimeField(auto_now_add=True)
       created_by=models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
       category=models.ForeignKey(category,related_name='products',on_delete=models.CASCADE)
       image=models.ImageField(upload_to='product_images',blank=True,null=True)
       class Meta:
                 verbose_name_plural='product'
       def __str__(self):
          return self.name