

# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


class OrganisationCounty(models.Model):
    '''
    This is for managing all te data related to OrgnisationCounties.
    name: the name of the industry
    is_active: tells if entity is active or not
    '''

    id = models.IntegerField(unique=True, primary_key=True)
    county_name = models.CharField(max_length=255, default=True, null=True)
    orgs_count = models.IntegerField(default=0, null=True)
    orgs_score = models.CharField(max_length=255, default=True, null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = 'organisation_county'
        verbose_name_plural = 'organisation_counties'
        app_label = 'dashboard'

    def __unicode__(self):
        return self.id


class OrganisationCountyAdmin(admin.ModelAdmin):

    list_display = ['id', 'county_name', 'orgs_count', 'orgs_score',
                    'is_active']
    list_filter = ('is_active',)

    fieldsets = (
        (None, {'fields': ('id', 'county_name', 'orgs_count', 'orgs_score',
                           'is_active')}),
    )

    add_fieldsets = (
        (None, {'fields': ('id', 'county_name', 'orgs_count', 'orgs_score',
                           'is_active',)}),
    )

    search_fields = ('county_name',)
    ordering = ['id']

    filter_horizontal = ()
