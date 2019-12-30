# users/urls.py
 
from django.conf.urls import url
from dashboard.views import CreateIndustry
 
urlpatterns = [
    url(r'^$', CreateIndustry.as_view()),
]