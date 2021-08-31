from django.urls import path
from django.contrib.auth  import views  as auth_views

from . import views


urlpatterns=[
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit_vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),

]