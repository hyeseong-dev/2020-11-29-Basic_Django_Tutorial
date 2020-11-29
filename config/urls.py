from django.contrib import admin
from django.urls import path, include
from myuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myuser/', include('myuser.urls')),
    path('board/', include('board.urls')),
    path('', home),
]
