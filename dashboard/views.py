from django.shortcuts import render

# Create your views here.

# Mapping controllers to view 

from dashboard.controllers.organisation import CreateOrganisation, OrganisationAPIView
from dashboard.controllers.industry import CreateIndustry