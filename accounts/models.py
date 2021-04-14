from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    dateOfBirth = models.DateField()
    nationality = models.CharField(max_length=100,default="বাংলাদেশী")
    bio = models.CharField(max_length=300,default=" ")
    height = models.CharField(max_length=50,default=" ")
    weight = models.CharField(max_length=50,default=" ")
    religion = models.CharField(max_length=50,default=" ")
    skinTone = models.CharField(max_length=50,default=" ")
    proffession = models.CharField(max_length=200,default=" ")
    profilePicture = models.ImageField(default = 'profilepics/default.jpg', upload_to = 'profilepics')
    galleryPicOne = models.ImageField(default = 'profilepics/default.jpg', upload_to = 'gallerypics')
    galleryPicTwo = models.ImageField(default = 'profilepics/default.jpg', upload_to = 'gallerypics')
    galleryPicThree = models.ImageField(default = 'profilepics/default.jpg', upload_to = 'gallerypics')
    galleryPicFour = models.ImageField(default = 'profilepics/default.jpg', upload_to = 'gallerypics')

    def __str__(self):
        return f'{self.user.username} profile'