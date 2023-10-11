from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class City(models.Model):
    title = models.CharField(max_length=255)


class User(AbstractUser):
    img = models.ImageField(upload_to='profile_images/')
    phone = models.CharField(max_length=255, null=True, blank=True, default='000000000000000')
    gender = models.IntegerField(choices = (
        (1, 'male'),
        (2, 'female'),
        (3, 'none')
    ),default=3)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank = True) 
    status = models.IntegerField(
        choices= (
            (1, 'admin'),
            (2, 'valantior')
        ), default=2
    )


class HelpType(models.Model):
    title = models.CharField(max_length=255)


class Helpless(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=255)
    jshshr = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    help_type = models.ManyToManyField(HelpType)
    about = models.TextField()

    def __str__(self) -> str:
        return self.name


class HelplessMedia(models.Model):
    helpless = models.ForeignKey(Helpless, on_delete= models.CASCADE)
    img = models.ImageField(upload_to='helples_img/')


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    about = models.TextField() 
    title = models.CharField(max_length=100) 


class BlogMedia(models.Model):
    image = models.ImageField(upload_to='blog-images/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)

