# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from myapp.models import Goods

admin.site.register(Goods)
# admin.site.site_url = 'www.baidu.com'

# Register your models here.
# from blog.models import Blog
  
#Blog模型的管理器
# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
#     list_display = ('id', 'caption', 'author', 'publish_time')
#     
#     #list_per_page设置每页显示多少条记录，默认是100条
#     list_per_page = 50
#     
#     #ordering设置默认排序字段，负号表示降序排序
#     ordering = ('-publish_time',)
#   
#     #list_editable 设置默认可编辑字段
#     list_editable = ['machine_room_id', 'temperature']
#   
#     #fk_fields 设置显示外键字段
#     fk_fields = ('machine_room_id',)
#     
#     list_filter =('trouble', 'go_time', 'act_man__user_name', 'machine_room_id__machine_room_name') #过滤器
#     search_fields =('server', 'net', 'mark') #搜索字段
#     date_hierarchy = 'go_time'    # 详细时间分层筛选　
    
    
# class MyAdminSite(admin.AdminSite):
#     site_header = '好医生运维资源管理系统'  # 此处设置页面显示标题
#     site_title = '好医生运维'  # 此处设置页面头部标题
#  
# admin_site = MyAdminSite(name='management')