# from django.shortcuts import render,redirect
# # Create your views here.
# from .models import Category
# from .forms import CategoryForm
# def add_category(request):
#     if request.user.is_authenticated:
#         if request.method=='POST':
#             form=CategoryForm(request.POST)
#             if form.is_valid():
#                form.save()
#                return redirect('add_category')
#         else:
#             form=CategoryForm()
#         return render(request,'category.html',{'form':form})
#     else:
#         return redirect('signup')

