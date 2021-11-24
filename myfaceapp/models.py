from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profilemodel(models.Model):
    image = models.ImageField(upload_to="ProfilePics")
    bio = models.CharField(max_length=200)
    followers = models.ManyToManyField(User,related_name='followers',blank=True,null=True)
    following = models.ManyToManyField(User,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")

class Post(models.Model):
    post = models.ImageField(upload_to="posts")
    profileuser = models.ForeignKey(profilemodel,related_name="profile",on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name="likes",blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Register(models.Model):
    mobile_number = models.IntegerField(blank=False, max_length=10)
    name = models.CharField(blank=False, max_length=200)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=20,null=True)
    def __str__(self):
       return str(self.mobile_number)

class Login(models.Model):
    lmobile_number = models.IntegerField(blank=False, max_length=10)
    lpassword = models.CharField(max_length=20,null=True)
    def __str__(self):
       return str(self.lmobile_number)