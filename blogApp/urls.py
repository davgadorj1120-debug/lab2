from django.urls import path
from django.http import HttpResponse

def blog_home(request):
    # HTML-ийн <a> таг ашиглан үндсэн зам буюу '/' рүү очих линк нэмэв
    return HttpResponse("""
        <h2>BLOG APP</h2>
        <br>
        <a href="/">Буцах</a>
    """)

urlpatterns = [
    path('', blog_home),
]