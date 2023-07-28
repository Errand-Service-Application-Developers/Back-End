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
    
    PENDING = 'PENDING'
    IN_PROGRESS = 'IN PROGRESS'
    COMPLETED = 'COMPLETED'
    
    TASK_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(ItemCategory, on_delete=models.PROTECT, related_name='items')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='items')
    date_created = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500, default="https://res.cloudinary.com/dagfqp7qa/image/upload/v1688892172/samples/cloudinary-icon.png")
    task_status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default=PENDING)

    

    def __str__(self) -> str:
        return self.title



class ItemReview(models.Model):
    message = models.CharField(max_length=500)
    item = models.ForeignKey(ListItem, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reviews')
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user} {self.message}"
    

class ReviewReply(models.Model):
    review = models.ForeignKey(ItemReview,on_delete=models.CASCADE,related_name='replies')
    reply = models.CharField(max_length= 500, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='replier',null = False)
    date_created = models.DateTimeField(auto_now_add= True)
    task = models.ForeignKey(ListItem,on_delete=models.CASCADE,related_name='replies')
    

class Request(models.Model):
    ACCEPTED = 'ACCEPTED'
    PENDING = 'PENDING'
    DECLINED = 'DECLINED'
    
    REQUEST_STATUS = [
        (ACCEPTED,"Accepted"),
        (PENDING,'Pending'),
        (DECLINED,"Declined")
    ]
    task = models.ForeignKey(ListItem,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=REQUEST_STATUS,default=PENDING)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='request_received')
    requester  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='request_sent')
    date_created = models.DateTimeField(auto_now_add=True)