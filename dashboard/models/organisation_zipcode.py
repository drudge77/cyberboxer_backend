

# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


class OrganisationZipcode(models.Model):
    '''
    This is for managing all te data related to OrganisationZipcodes.
    name: the name of the industry
    is_active: tells if entity is active or not
    '''

    id = models.IntegerField(unique=True, primary_key=True)
    zipcode = models.CharField(max_length=255, default=True, null=True)
    orgs_count = models.IntegerField(default=0, null=True)
    orgs_score = models.CharField(max_length=255, default=True, null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = 'organisation_zipcode'
        verbose_name_plural = 'organisation_zipcodes'
        app_label = 'dashboard'

    def __unicode__(self):
        return self.id


class OrganisationZipcodeAdmin(admin.ModelAdmin):

    list_display = ['id', 'zipcode', 'orgs_count', 'orgs_score',
                    'is_active']
    list_filter = ('is_active',)

    fieldsets = (
        (None, {'fields': ('id', 'zipcode', 'orgs_count', 'orgs_score',
                           'is_active')}),
    )

    add_fieldsets = (
        (None, {'fields': ('id', 'zipcode', 'orgs_count', 'orgs_score',
                           'is_active',)}),
    )

    search_fields = ('zipcode',)
    ordering = ['id']

    filter_horizontal = ()
