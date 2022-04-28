from email import message
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1,'ADMIN'),
        (2,'HOUSEKEEPER'),
        (3,'CUSTOMER'),


    )
        
    
    user_type =models.CharField(choices=USER,max_length=50,default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    
class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/service_image')
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class Housekeeper(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE,)
    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    id_proof = models.ImageField(upload_to='media/id_pic')
    service_id = models.ForeignKey(Service,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.first_name + ' ' + self.admin.last_name
class Customer(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE,)
    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
class Housekeeper_Notification(models.Model):
    housekeeper_id = models.ForeignKey(Housekeeper,on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.housekeeper_id.admin.first_name
class Housekeeper_Leave(models.Model):
    housekeeper_id = models.ForeignKey(Housekeeper,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    leave_message = models.TextField()
    status = models.IntegerField(null=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.housekeeper_id.admin.first_name +  self.housekeeper_id.admin.last_name
    
class Housekeeper_Feedback(models.Model):
    housekeeper_id = models.ForeignKey(Housekeeper,on_delete=models.CASCADE)
    housekeeper_feedback = models.TextField()
    housekeeper_feedback_reply = models.TextField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.housekeeper_id.admin.first_name + ' ' + self.housekeeper_id.admin.last_name
    