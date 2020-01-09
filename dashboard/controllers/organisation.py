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
from dashboard.models import Organisation
from dashboard.serializers import OrganisationSerializer
from rest_framework import filters


class CreateOrganisation(APIView):

    # Allow only authenticated users to access this url

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({}, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response({}, status=status.HTTP_201_CREATED)


class OrganisationAPIView(generics.ListCreateAPIView):

    # # Allow only authenticated users to access this url

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
