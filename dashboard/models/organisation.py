

# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
import sys


class Organisation(models.Model):
    '''
    This is for managing all te data related to organisations.
    name: the name of the organisation
    is_active: tells if entity is active or not
    '''
    id = models.IntegerField(unique=True, primary_key=True)
    k_id = models.CharField(max_length=255, default=None, null=True)
    company_name = models.CharField(max_length=255, default=None, null=True)
    company_website = models.CharField(max_length=255, default=None, null=True)
    company_address = models.CharField(max_length=255, default=None, null=True)
    address = models.CharField(max_length=255, default=None, null=True)
    employee_band_at_address = models.CharField(
        max_length=255, default=None, null=True)
    employee_band_at_company = models.CharField(
        max_length=255, default=None, null=True)
    final_industry_code = models.CharField(
        max_length=255, default=None, null=True)
    last_update = models.CharField(max_length=255, blank=True, null=True)
    naics_num = models.CharField(max_length=255, default=None, null=True)
    state = models.CharField(max_length=255, default=None, null=True)
    year_established = models.CharField(
        max_length=255, default=None, null=True)
    county_name = models.CharField(max_length=255, default=None, null=True)
    city_name = models.CharField(max_length=255, default=None, null=True)
    zipcode = models.CharField(max_length=255, default=None, null=True)
    latitude = models.CharField(max_length=255, default=None, null=True)
    longitude = models.CharField(max_length=255, default=None, null=True)

    class Meta:
        verbose_name = 'organisation'
        verbose_name_plural = 'organisation'
        app_label = 'dashboard'

    def __unicode__(self):
        return self.id


class OrganisationAdmin(admin.ModelAdmin):

    list_per_page = 40

    list_display = [
        'id',
        'k_id', 'company_name', 'company_website', 'company_address', 'address',
        'employee_band_at_address', 'employee_band_at_company',
        'final_industry_code', 'last_update', 'naics_num', 'state',
        'year_established', 'county_name', 'city_name', 'zipcode', 'latitude',
        'longitude']
    # list_filter = ('state',)

    fieldsets = (
        (None, {'fields': ('id',
                           'k_id', 'company_name', 'company_website', 'company_address', 'address',
                           'employee_band_at_address', 'employee_band_at_company',
                           'final_industry_code', 'last_update', 'naics_num', 'state',
                           'year_established', 'county_name', 'city_name', 'zipcode', 'latitude',
                           'longitude')}),
    )

    add_fieldsets = (
        (None, {'fields': ('id',
                           'k_id', 'company_name', 'company_website', 'company_address', 'address',
                           'employee_band_at_address', 'employee_band_at_company',
                           'final_industry_code', 'last_update', 'naics_num', 'state',
                           'year_established', 'county_name', 'city_name', 'zipcode', 'latitude',
                           'longitude')}),
    )

    # search_fields = ('company_name', 'company_address',
    #  'latitude', 'longitude')
    ordering = ['id']

    filter_horizontal = ()
