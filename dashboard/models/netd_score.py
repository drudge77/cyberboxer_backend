

# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


class NetdScore(models.Model):
    '''
    This is for managing all te data related to Netd Scores.
    name: the name of the industry
    is_active: tells if entity is active or not
    '''

    id = models.IntegerField(unique=True, primary_key=True)
    naics_code = models.CharField(max_length=255)
    industry_title = models.CharField(max_length=255)
    netd_score = models.CharField(max_length=255)
    indicator = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = 'netd_score'
        verbose_name_plural = 'netd_scores'
        app_label = 'dashboard'

    def __unicode__(self):
        return self.id


class NetdScoreAdmin(admin.ModelAdmin):

    list_display = ['id', 'naics_code', 'industry_title', 'netd_score', 'indicator',
                    'is_active']
    list_filter = ('is_active',)

    fieldsets = (
        (None, {'fields': ('id', 'naics_code', 'industry_title', 'netd_score', 'indicator',
                           'is_active',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('id', 'naics_code', 'industry_title', 'netd_score', 'indicator',
                           'is_active',)}),
    )

    search_fields = ('naics_code',)
    ordering = ['id']

    filter_horizontal = ()
