from rest_framework import serializers
from dashboard.models import (
    Organisation, OrganisationCity,
    OrganisationZipcode, OrganisationCounty
)


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'


class OrganisationCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationCity
        fields = '__all__'


class OrganisationZipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationZipcode
        fields = '__all__'


class OrganisationCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationCounty
        fields = '__all__'
