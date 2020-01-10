# users/urls.py
 
from django.conf.urls import url
from dashboard.views import CreateOrganisation, OrganisationAPIView, GetMappedData
 
urlpatterns = [
    url(r'^$', CreateOrganisation.as_view()),
    url('search/', OrganisationAPIView.as_view()),
    url('map/', GetMappedData.as_view()),
]