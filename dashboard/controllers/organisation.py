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

class CreateOrganisation(APIView):

    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    # serializer_class = UserSerializer
 
    def post(self, request):
        return Response({}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        return Response({}, status=status.HTTP_201_CREATED)