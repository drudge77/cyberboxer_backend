# users/urls.py
 
from django.conf.urls import url
from .views import CreateUserAPIView
from .views import LoginAPIView
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView
 
urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^login/$', LoginAPIView.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
]