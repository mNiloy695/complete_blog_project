from django.db import models
from  django.contrib.auth.models import User
from category.models import Category

# Create your models here
class PostModel(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=20000000)
    author=models.ForeignKey(User,models.SET_NULL,null=True)
    category=models.ManyToManyField(Category)
    def __str__(self) -> str:
        return self.title


