from django.shortcuts import render,redirect
from .forms import PostForm
from .models import PostModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def add_post(request):
    if request.user.is_authenticated:
        if request.method ==  'POST':
           form=PostForm(request.POST)
           if form.is_valid():
                form.instance.author=request.user
                form.save()
                return redirect('home')
        else:
            form=PostForm()
        return render(request,'post.html',{'form':form})
    else:
        return redirect('signup')
        
def edit_post(request,id):
    if request.user.is_authenticated:
        post=PostModel.objects.all().get(pk=id)
        if request.method ==  'POST':
           form=PostForm(request.POST,instance=post)
           if form.is_valid():
                form.instance.author=request.user
                messages.success(request,'Your Post Updated Successfully')
                form.save()
                return redirect('home')
        else:
            form=PostForm(instance=post)
        return render(request,'post.html',{'form':form})
    else:
        return redirect('signup')
@login_required
def delete_post(request,id):
    post=PostModel.objects.all().get(pk=id).delete()
    return redirect('profile')

