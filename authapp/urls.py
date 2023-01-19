from django.urls import include, path

from .views import check_server

urlpatterns = [
  
    path('', include('djoser.urls') ),
    path('', include('djoser.urls.authtoken') ),
    path('check_server/', check_server.as_view(), name="check_server"),
   
]