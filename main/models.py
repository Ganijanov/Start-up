from django.db import models
from django.contrib.auth.models import User


class City(models.Model): 
    city = models.CharField(max_length=255) 
 
 
class Clinic(models.Model): 
    admin = models.OneToOneField(User, on_delete=models.CASCADE) 
    logo = models.ImageField(upload_to='company_logo/') 
    about = models.TextField(blank=True, null=True) 
 
 
class Group(models.Model): 
    admin = models.ForeignKey(Clinic, on_delete=models.CASCADE) 
    title = models.CharField(max_length= 255) 
    about = models.TextField(blank=True, null=True) 
 
 
class Valantior(models.Model): 
    admin = models.OneToOneField(User, on_delete=models.CASCADE) 
    phone = models.CharField(null=True, blank=True) 
    img = models.ImageField(upload_to='account_photo/') 
    age = models.PositiveIntegerField() 
    gender = models.IntegerField(choices=((1 , 'female'),(2 , 'male')), null=True, blank=True)  
    about = models.TextField(null=True, blank=True) 
    help_count = models.PositiveIntegerField(default=0) 
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True) 
    group = models.ManyToManyField(Group, on_delete=models.SET_NULL, null=True, blank=True) 
 
 
class Category(models.Model): 
    title = models.CharField(max_length=255) 
    about = models.TextField(blank=True, null=True)  
 
 
class Helpless(models.Model): 
    admin = models.OneToOneField(User, on_delete=models.CASCADE) 
    img = models.ImageField(upload_to='account_photo/') 
    age = models.PositiveIntegerField() 
    gender = models.IntegerField(choices=((1 , 'female'),(2 , 'male')), null=True, blank=True) 
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True) 
    about = models.TextField(blank=True, null=True) 
    phone = models.CharField(null=True, blank=True) 
    category = models.ManyToManyField(Category, null=True, blank=True) 
 
 
class Degree(models.Model): 
    putter = models.ForeignKey(Helpless, related_name='elderly', on_delete=models.SET_NULL, null=True) 
    valantior = models.ForeignKey(Valantior, related_name='valantior', on_delete=models.CASCADE) 
    value = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 10)]) 
    timestamp = models.DateTimeField(auto_now_add=True) 
 
 
class Chat(models.Model): 
    first_person = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='first_person') 
    second_person = models.ForeignKey(User,on_delete=models.CASCADE, related_name='second_person') 
    created = models.DateTimeField(auto_now_add=True) 
 
 
class Message(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages') 
    created = models.DateTimeField(auto_now_add=True) 
    text = models.TextField()  
 
 
class Blog(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    about = models.TextField() 
    title = models.CharField(max_length=100) 
 
 
class Service(models.Model): 
    type = models.CharField(max_length=255) 
    clinic = models.ForeignKey(Clinic, blank=True, null=True)


class Staff(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    image = models.ImageField()
    

class ImageClinic(models.Model):
    image = models.ImageField()
    clinic = models.ForeignKey(Clinic, blank=True, null=True, related_name='image_clinic')


class ImageBlog(models.Model):
    image = models.ImageField()
    blog = models.ForeignKey(Blog, blank=True, null=True)