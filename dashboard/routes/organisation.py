# users/urls.py
 
from django.conf.urls import url
from dashboard.views import CreateOrganisation
from dashboard.views import OrganisationAPIView
 
urlpatterns = [
    url(r'^$', CreateOrganisation.as_view()),
    url('search/', OrganisationAPIView.as_view())
]