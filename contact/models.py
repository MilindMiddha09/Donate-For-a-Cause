from django.db import models

class Contact(models.Model):
    Name = models.TextField(blank=False,null=True,max_length=20);
    Email = models.EmailField(blank=False,null=True,max_length=20);
    Subject = models.TextField(blank=False,null=True,max_length=30);
    Message = models.TextField(blank=False,null=True,max_length=100);
