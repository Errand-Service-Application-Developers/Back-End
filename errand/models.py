from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, default = '##########')

    def __str__(self) -> str:
        return self.username


class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, default='email')
    backgroundColor = models.CharField(max_length=50, default='tomato')
    color = models.CharField(max_length=50, default='white')

    def __str__(self) -> str:
        return self.name


class ListItem(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT, related_name='items')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='items')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title



class ItemReview(models.Model):
    message = models.CharField(max_length=500)
    item = models.ForeignKey(ListItem, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reviews')
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    