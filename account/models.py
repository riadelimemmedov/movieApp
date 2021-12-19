from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.
class Auth(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='account',blank=True)
    location = models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return self.user.username
    
    
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Auth.objects.create(user=instance)
post_save.connect(create_user_profile,sender=settings.AUTH_USER_MODEL)