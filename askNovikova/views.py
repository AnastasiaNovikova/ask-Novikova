from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def test(request):
	line = request.method + "<br>"
	if request.method == 'GET':
		out = request.GET
	elif request.method == 'POST':
		out = request.post
	for i in out.items():
		line = line + i[0] + " = " + str(i[1]) + "<br>"
	return HttpResponse(line)