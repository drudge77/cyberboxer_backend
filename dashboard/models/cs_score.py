

# from __future__ import unicode_literals
from django.db import models
from django.contrib import admin


class CSScore(models.Model):
    '''
    This is for managing all te data related to Cyber Security Scores.
    name: the name of the industry
    is_active: tells if entity is active or not
    '''

    id = models.IntegerField(unique=True, primary_key=True)
    naics_code = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    band = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    severity = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    indicator = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = 'cs_score'
        verbose_name_plural = 'cs_scores'
        app_label = 'dashboard'

    def __unicode__(self):
        return self.id


class CSScoreAdmin(admin.ModelAdmin):

    list_display = ['id', 
                    'naics_code',
                    'industry',
                    'band',
                    'score',
                    'indicator',
                    'severity',
                    'frequency',
                    'is_active']
    list_filter = ('is_active',)

    fieldsets = (
        (None, {'fields': (
                    'id',
                    'naics_code',
                    'industry',
                    'band',
                    'score',
                    'indicator',
                    'severity',
                    'frequency',
                    'is_active',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('id',
                    'naics_code',
                    'industry',
                    'band',
                    'score',
                    'indicator',
                    'severity',
                    'frequency',
                    'is_active',)}),
    )

    search_fields = ('naics_code',)
    ordering = ['id']

    filter_horizontal = ()
