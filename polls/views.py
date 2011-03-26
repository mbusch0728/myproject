# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Ambrosia I like your body. You're at the poll index.")
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % (poll_id,))

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % (poll_id,))

def vote(request, poll_id):
    return HttpResponse("<strong>You're voting on poll %s.</strong>" % (poll_id,))

from django.http import HttpResponseRedirect
def redirect_to_polls(request):
    return HttpResponseRedirect('/polls/')
