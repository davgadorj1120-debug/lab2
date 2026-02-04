from django.urls import path
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>POLL APP</h2><a href='/'>Буцах</a>")

urlpatterns = [
    path('', index),
]