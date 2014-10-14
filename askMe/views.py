from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

import datetime
# Create your views here.
def landingPage(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
def signup(request):
	template = loader.get_template('askMe/index.html')
	return HttpResponse(template)
def login(request):
	return HttpResponse("Hello, world. You're at the askMe-> login.")