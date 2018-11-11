# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from mybook.models import Books  
from django.shortcuts import render_to_response
# Create your views here.
def booklist(request):
#     table_form=forms.Formgood()    #web
#     for i in table_form:
#         print i   
    
    good_list=Books.objects.all()      #message
    if request.method == "POST":
        for key in request.POST.values():
            print key
        
        for key in request.POST:
            print key
            if key.isdigit():
                Books.objects.filter(id=key).delete()
                return render_to_response("book.html",{"Goods":good_list})
            if key=="id_add":
                tableid = request.POST.get("id_add", None)
                tabletitle = request.POST.get("bookname", None)
                tableprice = request.POST.get("bookstarttime", None)
                tabledesc = request.POST.get("bookinfo", None)
                tableunit = request.POST.get("booktype", None)
                tableendtime = request.POST.get("bookendtime", None)
                tablepicture = request.POST.get("bookremark", None)
                twz = Books.objects.filter(id=tableid).update(bookname=tabletitle, \
                   bookstarttime=tableprice, bookinfo=tabledesc, booktype=tableunit,\
                   bookendtime=tableendtime, bookremark = tablepicture)
                print "333333333333",tabletitle
                #twz.save()           
            if key=="id":
                tableid = request.POST.get("id", None)
                tabletitle = request.POST.get("bookname", None)
                tableprice = request.POST.get("bookstarttime", None)
                tabledesc = request.POST.get("bookinfo", None)
                tableunit = request.POST.get("booktype", None)
                tableendtime = request.POST.get("bookendtime", None)
                tablepicture = request.POST.get("bookremark", None)
                twz = Books.objects.create(id=tableid, bookname=tabletitle, \
                   bookstarttime=tableprice, bookinfo=tabledesc, booktype=tableunit,\
                   bookendtime=tableendtime, bookremark = tablepicture)
                twz.save()
#     good_list=[{"name":"fadfa", "number":"fdasfa","adf":"ads"}]
    return render_to_response("book.html",{"Goods":good_list})