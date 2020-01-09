from rest_framework import serializers
from dashboard.models.organisation import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'