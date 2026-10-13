from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin
from . import views
from .forms import loginForm
urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('login/',auth_views.LoginView.as_view(template_name='market/login.html',authentication_form=loginForm),name='login'),
    path('singup/',views.signup,name='singup'), 
    path('logout/',views.logout_view,name='logout_view'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('browse/', views.browse, name='browse'),

      ]