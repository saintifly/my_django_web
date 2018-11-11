# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from myapp.models import book_info

#数据表操作-增

test1 = book_info(fromuser='testuser',fromsite='testsite',bookname='testbookname')
test1.save()

# or
# book_info.objects.create(fromuser='testuser',fromsite='testsite',bookname='testbookname')

###删除

test1 = book_info.objects.get(bookname='testbookname')
test1.delete()

# book_info.objects.filter(bookname='testbookname').delete()
# book_info.objects.all().delete()


####修改
test1 = book_info.objects.get(bookname='testbookname')
test1.bookname = 'book1'
test1.fromuser = 'user1'
test1.save

# book_info.objects.filter(bookname='testbookname').update(fromuser='user1')
# book_info.objects.all().update(fromuser='user1')

####数据库操作-查

Databaselist = book_info.objects.all()
for i in Databaselist:
    print(i.book_name)
# list = book_info.objects.filter(bookname='testbookname'， fromuser='testuser')  #类似于SQL中的WHERE
# list = book_info.objects.filter( fromuser__contains='testuser')  #注意中间是双下划线，类似于SQL中的where fromuser like "%testuser%" 
# #此外还有icontains(大小写无关的like),startswith和endswith, 还有range(SQL BETWEEN查询）
# list = book_info.objects.get(bookname='testbookname')  #返回单条记录，不需要for直接list.bookname使用
# list = book_info.objects.filter().exclude().filter() #可无限嵌套
# book_info.object.all()[:5]  #前5条记录
# book_info.object.order_by(bookname)[2:5]  #排序后的第3、4、5条记录
# book_info.object.order_by(bookname)[0]  #排序后的第1条记录
# book_info.object.order_by(bookname)[0:1].get() #排序后的第1条记录
# book_info.object.all()[:10:2]  #从第1条记录到第11条记录步长为2的数据集

