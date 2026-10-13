from django.urls import path
from . import views
app_name='items'
urlpatterns=[
    path('<int:pk>/',views.detail,name='detail'),
    path('new/',views.newp,name='newp'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('purchase/<int:product_id>/', views.purchase_product, name='purchase_product'),]