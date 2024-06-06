from django.shortcuts import render ,redirect
from post.models import PostModel
from category.models import Category

def home(request,category_slug=None):
    posts=PostModel.objects.all()
    categorys=Category.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        posts=PostModel.objects.filter(category=category)
    return render(request,'home.html',{'posts':posts,'category':categorys})