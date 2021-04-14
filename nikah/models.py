from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class post(models.Model):
    id=models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=40,default=" ")
    details = models.CharField(max_length=230,default=" ")
    creatDate = models.DateField(auto_now_add=True)
    updateDate = models.DateField(auto_now=True)
    creatTime = models.DateTimeField(default=now)
    def __str__(self):
        return self.title + " by : " + self.author.username
    class Meta:
        ordering = ['-creatTime',]
