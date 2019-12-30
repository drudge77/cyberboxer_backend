# users/urls.py
 
from django.conf.urls import url
from dashboard.views import CreateOrganisation
 
urlpatterns = [
    url(r'^$', CreateOrganisation.as_view()),
]