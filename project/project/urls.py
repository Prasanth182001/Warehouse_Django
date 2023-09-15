"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('pdt/',views.product,name='PDT'),
    path('lct/',views.Location,name='LCT'),
    path('tfr/',views.transfer,name="TFR"),
    path('editp/<id>',views.edit_p),
    path ('editl/<id>',views.edit_l),
    path('delp/<id>',views.delete_p),
    path('deletl/<id>',views.delet_l),
    re_path('adl/',views.add_l),
    re_path('adp/',views.add_p),
    re_path('adt/',views.add_t),
    
]
