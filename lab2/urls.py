from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('poll/', include('pollApp.urls')), # pollApp/urls.py-г энд холбож байна
    path('blog/', include('blogApp.urls')), # blogApp/urls.py-г энд холбож байна
]