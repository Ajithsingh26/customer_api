from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_age = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer_name