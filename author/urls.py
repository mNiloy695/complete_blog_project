from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.registration,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('login/',views.user_login,name='login'),
    path('change/',views.change_password,name='change_old'),
    path('change2/',views.change_password2,name='change2'),
    path('logout/',views.log_out,name='logout'),
    path('edit_info/',views.edit_info,name='edit_info'),
]
