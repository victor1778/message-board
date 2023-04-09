from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)