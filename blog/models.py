from django.db import models
from django contrib.models import User
from django.utils import timezone

class Post (models.Model):
author = models.ForeignKey(User, on_delete== models.CASCADE, related_name='blog_post')
title = models.charField(max_laugth=200)
text = models.TextField()
created_date = models.DateTimeField(blank=True,null=True)



# Create your models here.
