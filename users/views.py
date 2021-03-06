from dashboard.models import Organisation
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.signals import user_logged_in
import jwt
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from.models import User
from.serializers import UserSerializer


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'type': 'success',
            'data': serializer.data
        },
            status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']
            try:
                user = User.objects.get(email=email, password=password)
                if user:
                    try:
                        payload = jwt_payload_handler(user)
                        token = jwt.encode(payload, settings.SECRET_KEY)
                        user_details = {}
                        user_details['name'] = "%s %s" % (
                            user.first_name, user.last_name)
                        user_details['token'] = token
                        user_logged_in.send(sender=user.__class__,
                                            request=request, user=user)
                        return Response({
                            'type': 'success',
                            'data': user_details
                        },
                            status=status.HTTP_200_OK)

                    except Exception:
                        res = {
                            'type': 'failed',
                            'message': 'Invalid credentials'}
                        return Response(res, status=status.HTTP_200_OK)
            except Exception:
                res = {
                    'type': 'failed',
                    'message': 'Invalid credentials'}
                return Response(res, status=status.HTTP_200_OK)
            else:
                res = {
                    'type': 'error',
                    'message': 'can not authenticate with the given credentials or the account has been deactivated'}
                return Response(res, status=status.HTTP_200_OK)
        except KeyError:
            res = {
                'type': 'failed',
                'message': 'please provide a email and a password'}
            return Response(res, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):

    # Allow only authenticated users to access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)
        return Response({
            'type': 'success',
            'data': serializer.data
        },
            status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'type': 'success',
            'data': serializer.data
        },
            status=status.HTTP_200_OK)
