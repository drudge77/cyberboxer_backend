from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.conf import settings
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
# from rest_framework_jwt.utils import jwt_payload_handler
# import jwt
# from django.contrib.auth.signals import user_logged_in
from rest_framework.permissions import IsAuthenticated
from dashboard.models import (
    Organisation, OrganisationCity,
    OrganisationZipcode, OrganisationCounty
)
from dashboard.serializers import (
    OrganisationSerializer, OrganisationCitySerializer,
    OrganisationZipCodeSerializer, OrganisationCountySerializer
)
from rest_framework import filters


class CreateOrganisation(APIView):
    # Allow only authenticated users to access this url

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({}, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response({}, status=status.HTTP_201_CREATED)


class OrganisationAPIView(generics.ListCreateAPIView):

    # Allow only authenticated users to access this url

    permission_classes = (IsAuthenticated,)

    search_fields = ['company_name']
    filter_backends = [filters.SearchFilter]

    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    # def get(self, request):
    #         return Response({
    #             'type': 'success',
    #             'data': None
    #         },
    #             status=status.HTTP_200_OK)


class GetMappedData(generics.ListAPIView):
    serializer_class = OrganisationCitySerializer

    def get_queryset(self):
        level = int(self.request.GET.get('level'))
        if level == 1:
            db = Organisation
            serializer_class = OrganisationSerializer
        elif level == 2:
            db = OrganisationZipcode
            serializer_class = OrganisationZipCodeSerializer
        elif level == 3:
            db = OrganisationCity
            serializer_class = OrganisationCitySerializer
        elif level == 4:
            db = OrganisationCounty
            serializer_class = OrganisationCountySerializer
        qs = db.objects.all()
        if qs.exists:
            qs_null = qs.filter(latitude__isnull=True)
            if qs_null.count() > 0:
                obj = qs_null.first()
                obj.latitude = 36.778261
                obj.longitude = 36.778261
                obj.save()
        return qs
