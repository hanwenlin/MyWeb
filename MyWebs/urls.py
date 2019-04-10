"""MyWebs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from MySite import views as siteviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'index/',siteviews.index),
    path(r'news_list/<str:news_type>/',siteviews.news_list),
    path('filter/',siteviews.filter_test),
    path('index_goods/',siteviews.index_goods),
    path('all/',siteviews.searchall),
    path('search_name/',siteviews.searchname),
    path('search_price/',siteviews.searchprice),
    path('search_sort/',siteviews.searchsort),
    path('reg/',siteviews.reg),
    path('register/',siteviews.register),
    path('check/',siteviews.check),
    path('change/',siteviews.change),
    path('changepass/',siteviews.changepass),
    path('goods_list/',siteviews.goodslist),
    path('goodsSearchprice/',siteviews.goodsSearchprice),
    path('adds/',siteviews.adds),
    path('del/',siteviews.dels),
]
