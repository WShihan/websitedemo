"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from myapp import views as sub_views
urlpatterns = [
    path('' , sub_views.index) ,
    path('books/' , sub_views.book) ,
    path('contact/' , sub_views.contact ,name='contact') ,
    path('about/' ,sub_views.about ,name='about') ,
    path('images/' , sub_views.showImage) ,
    # 图片url
    path('images/m1' , sub_views.img1) ,
    path('info/' , sub_views.getData) ,
    path('pack/' ,sub_views.pack ,name='patchBox') ,
    path("takeOut/" ,sub_views.takeOUt ,name = "takeOut") ,
    path('soft/' ,sub_views.soft ,name = "soft") ,
    path('img/' ,sub_views.returnImg ,name="returnImg") ,
    path('saying/' ,sub_views.returnSaying ,name='one') ,
    path('day/' ,sub_views.returnDay) ,
    path('date/' , sub_views.returnDate) ,
    path('url/' , sub_views.returnUrl) ,
    path('claim' ,sub_views.returnClaim ,name='claim') ,
    path('feedback/' , sub_views.getFeedBack ,name='feedback') ,
    path('data/' ,sub_views.showData),
    path('test/' ,sub_views.test) ,
    path('update/' ,sub_views.updateInfo) ,
    path('getId/' ,sub_views.getId) ,# 获取用户id
    path('admin/', admin.site.urls),
]
