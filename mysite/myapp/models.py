# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 创建两个表，包括表的
# class book_info(models.Model):
#     fromuser = models.CharField(max_length=30, default='WYS')
#     fromsite = models.CharField(max_length=50)
#     bookname = models.CharField(max_length=50)
#     #updatetime = models.DateTimeField()
#     #lastchapter = models.CharField(max_length=100)
# 
# class site_info(models.Model):
#     sitename = models.CharField(max_length=50)
#     bookname = models.CharField(max_length=50)
#     url = models.CharField(max_length=200)
#     updatetime = models.DateTimeField()
#     lastchapter = models.CharField(max_length=100)

from django.db import models
 
# Create your models here.
# class GoodsType(models.Model):
#     title = models.CharField('分类名称',max_length=30)
#     desc = models.CharField('描述',max_length=200,default='商品描述')
#     isdelete = models.BooleanField('删除',default=False)
#  
#     def __str__(self):
#         return self.title
 
class Goods(models.Model):
    title = models.CharField('商品名称',max_length=30,null=False)
    price = models.DecimalField('商品价格',max_digits=8,decimal_places=2)
    desc = models.CharField('描述', max_length=200)
    unit = models.CharField('单位',max_length=30)
    picture = models.ImageField('商品图片',upload_to='static/images/goods',default='normal.png')
    detail = models.CharField('商品详情',max_length=1000,default='商品详情')
    isdelete = models.BooleanField('删除',default=False)
#     type = models.ForeignKey(GoodsType,on_delete=models.CASCADE)
 
#     def __str__(self):
#         return self.title
