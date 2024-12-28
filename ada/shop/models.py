from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class item(models.Model):
    title = models.CharField(max_length=200,unique=True)
    body = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name= "author_User")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-price',)
    
