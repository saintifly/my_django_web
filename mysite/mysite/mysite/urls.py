# -*- coding: utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import settings
import os
from myapp import views
from mybook import views1
from mysite.view import hello, current_datetime,hours_ahead, \
play, main_in, test, hours_ahead11


from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url('^hello/$', hello),
	url('^time/$', current_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^pay/$', play),
    url(r'^test/$', test),
#     url(r'', main_in),
    url(r'^table/$', views.table),
    url(r'^book/$', views1.booklist),
    url(r'^insert/$',views.insert),
    url(r'^tableadd/$',views.tableadd),
    url(r'time/plusup/(\d{1,2})/$', hours_ahead11),
    url(r'^favicon.ico',RedirectView.as_view(url=r'/static/images/favicon.ico')),
    url(r'^qiong2_new1.jpg',RedirectView.as_view(url=r'/static/images/qiong2_new1.jpg')),
    url(r'^qiong1_new.jpg',RedirectView.as_view(url=r'/static/images/qiong1_new.jpg')),
]