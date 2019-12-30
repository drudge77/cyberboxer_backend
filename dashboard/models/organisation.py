

# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class Organisation(models.Model):
    '''
    This is for managing all te data related to organisations.
    name: the name of the organisation
    is_active: tells if entity is active or not
    '''

    name = models.CharField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'organisation'
        verbose_name_plural = 'organisation'
        app_label = 'dashboard'

    def __unicode__(self):
        return self.name


class OrganisationAdmin(admin.ModelAdmin):

    list_display = ['name', 'is_active']
    list_filter = ('is_active',)

    fieldsets = (
        (None, {'fields': ('name',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('name',)}),
    )

    search_fields =  ('name',)
    ordering = ['name']

    filter_horizontal = ()

 