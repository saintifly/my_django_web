# -*- coding: utf-8 -*-
from django.template import Template, Context
from django.http import Http404, HttpResponse
from django.shortcuts import render,render_to_response
import datetime
# import sys

# default_encoding = 'utf-8'
# if sys.getdefaultencoding() != default_encoding:
#     reload(sys)
#     sys.setdefaultencoding(default_encoding)
#     
def hello(request):
	return HttpResponse("Hello world")
	
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
	
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def play(request):
	return render(request,'index.html')

def main_in(request):
	return render(request,'main.html')

def test(request):
	return render(request,'test.html')

def hours_ahead11(request, offset):
	current_date = datetime.datetime.now()
	return render_to_response('timeoffset.html', locals())