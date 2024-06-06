from django.shortcuts import render,redirect
from .forms import RegistationForm,User_data_change
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from post.models import PostModel
# Create your views here.
def registration(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=RegistationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,message='Your account successfully created')
                return redirect('login')
        else:
            form=RegistationForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('home')
@login_required
def profile(request):
    data=PostModel.objects.filter(author=request.user)
    return render(request,'profile.html',{'posts':data})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                user_pass=form.cleaned_data['password']
                user=authenticate(username=name , password=user_pass)
                if user is  not None:
                    login(request,user)
                    return redirect('home')
        else:
            form=AuthenticationForm()
        return render(request,'login.html',{'form':form ,'type':'Login'})
    else:
        return redirect('signup')
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('login')
def change_password(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(request=request,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('login')
        else:
            form=PasswordChangeForm(request.user)
        return render(request,'login.html',{'form':form,'type':'Change Password'})
    else:
        return redirect('login')
def change_password2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=SetPasswordForm(request=request,data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form=SetPasswordForm(request.user)
        return render(request,'login.html',{'form':form,'type':'Change Password'})
    else:
        return redirect('login')

@login_required
def edit_info(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=User_data_change(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,message='Your account successfully Updated')
                return redirect('edit_info')
        else:
            form=User_data_change(instance=request.user)
        return render(request,'update.html',{'form':form})
    else:
        return redirect('home')



