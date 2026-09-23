from django.db import models

# Create your models here.
class ProductModel(models.Model):
    
    name = models.CharField(max_length=100)
    
    description = models.TextField()
    
    price = models.PositiveIntegerField()
    
    production_date = models.DateField()
    
    def __str__(self):
        return f'{self.name} - {self.price} BDT'