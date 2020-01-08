from django.contrib import admin

from dashboard.models import Organisation
from dashboard.models import OrganisationAdmin

from dashboard.models import Industry
from dashboard.models import IndustryAdmin

from dashboard.models import CSScore
from dashboard.models import CSScoreAdmin

from dashboard.models import PonemonScore
from dashboard.models import PonemonScoreAdmin

from dashboard.models import NetdScore
from dashboard.models import NetdScoreAdmin

from dashboard.models import OrganisationCounty
from dashboard.models import OrganisationCountyAdmin

from dashboard.models import OrganisationCity
from dashboard.models import OrganisationCityAdmin

from dashboard.models import OrganisationZipcode
from dashboard.models import OrganisationZipcodeAdmin


# Register your models here.

# Organisation

admin.site.register(Organisation,OrganisationAdmin)

# Industry

admin.site.register(Industry,IndustryAdmin)

# CSScore

admin.site.register(CSScore,CSScoreAdmin)

# PonemonScore

admin.site.register(PonemonScore,PonemonScoreAdmin)

# Industry

admin.site.register(NetdScore,NetdScoreAdmin)

# OrganisationCounty

admin.site.register(OrganisationCounty,OrganisationCountyAdmin)

# OrganisationCity

admin.site.register(OrganisationCity,OrganisationCityAdmin)

# OrganisationZipcode

admin.site.register(OrganisationZipcode,OrganisationZipcodeAdmin)