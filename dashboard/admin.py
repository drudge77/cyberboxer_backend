from django.contrib import admin

from dashboard.models import Organisation
from dashboard.models import OrganisationAdmin

from dashboard.models import Industry
from dashboard.models import IndustryAdmin

# Register your models here.

# Organisation

admin.site.register(Organisation,OrganisationAdmin)

# Industry

admin.site.register(Industry,IndustryAdmin)