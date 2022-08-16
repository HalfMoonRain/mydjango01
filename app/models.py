from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)  # 길이 제한이 있는 문자열
    content = models.TextField()  # 길이 제한이 없는 문자열
