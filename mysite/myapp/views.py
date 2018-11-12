# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from django.shortcuts import render
from myapp.models import Goods  #insert
from myapp import forms
from django.shortcuts import render_to_response
# Create your views here.
def table(request):
#     table_form=forms.Formgood()    #web
#     for i in table_form:
#         print i   
    
    good_list=Goods.objects.all()      #message
    
    if request.method == "POST":
        for key in request.POST:
            if key.isdigit():
                Goods.objects.filter(id=key).delete() 
        tableid = request.POST.get("id", None)
        tabletitle = request.POST.get("title", None)
        tableprice = request.POST.get("price", None)
        tabledesc = request.POST.get("desc", None)
        tableunit = request.POST.get("unit", None)
        tablepicture = request.POST.get("picture", None)
        tabledetailt = request.POST.get("detail", None)
        tableisdelete = request.POST.get("isdelete", None)
        twz = Goods.objects.create(id=tableid, title=tabletitle, \
           price=tableprice, desc=tabledesc, unit=tableunit,\
           picture=tablepicture, detail=tabledetailt, isdelete=tableisdelete)
        twz.save()
#     good_list=[{"name":"fadfa", "number":"fdasfa","adf":"ads"}]
    return render_to_response("table.html",{"Goods":good_list})
#     return render_to_response("table.html",locals())

def insert(request):
    if request.method == "POST":
        tableid = request.POST.get("id", None)
        tabletitle = request.POST.get("title", None)
        tableprice = request.POST.get("price", None)
        tabledesc = request.POST.get("desc", None)
        tableunit = request.POST.get("unit", None)
        tablepicture = request.POST.get("picture", None)
        tabledetailt = request.POST.get("detail", None)
        tableisdelete = request.POST.get("isdelete", None)
        twz = Goods.objects.create(id=tableid, title=tabletitle, \
           price=tableprice, desc=tabledesc, unit=tableunit,\
           picture=tablepicture, detail=tabledetailt, isdelete=tableisdelete)
        twz.save()
    return render(request,'insert.html')

def tableadd(request):
    if request.method == "POST":
        tableid = request.POST.get("id", None)
        tabletitle = request.POST.get("title", None)
        tableprice = request.POST.get("price", None)
        tabledesc = request.POST.get("desc", None)
        tableunit = request.POST.get("unit", None)
        tablepicture = request.POST.get("picture", None)
        tabledetailt = request.POST.get("detail", None)
        tableisdelete = request.POST.get("isdelete", None)
        twz = Goods.objects.create(id=tableid, title=tabletitle, \
           price=tableprice, desc=tabledesc, unit=tableunit,\
           picture=tablepicture, detail=tabledetailt, isdelete=tableisdelete)
        twz.save()
    return render(request,'table.html')