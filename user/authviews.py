from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import SocialAuthSerializer

from rest_framework.response import Response
from rest_framework import status
from social_django.utils import load_backend, load_strategy
from social_core.exceptions import MissingBackend
from urllib.error import HTTPError
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from social_django.utils import load_strategy, load_backend
from rest_framework_simplejwt.tokens import RefreshToken


class SocialLoginView(generics.GenericAPIView):
    serializer_class = SocialAuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Authenticate user through the provider and access_token"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.data.get("provider", None)
        strategy = load_strategy(request)
        try:
            backend = load_backend(strategy=strategy, name=provider, redirect_uri=None)
        except MissingBackend:
            return Response(
                {"error": "Please provide a valid provider"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get("access_token")
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response(
                {"error": {"access_token": "Invalid token", "details": str(error)}},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except AuthTokenError as error:
            return Response(
                {"error": "Invalid credentials", "details": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            authenticated_user = backend.do_auth(access_token, user=user)
        except HTTPError as error:
            return Response(
                {"error": "invalid token", "details": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except AuthForbidden as error:
            return Response(
                {"error": "invalid token", "details": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if authenticated_user and authenticated_user.is_active:
            refresh = RefreshToken.for_user(authenticated_user)
            token = str(refresh.access_token)

            response = {
                "email": authenticated_user.email,
                "username": authenticated_user.username,
                "token": token,  # Include the JWT token in the response
                "id": authenticated_user.id,
            }
            return Response(status=status.HTTP_200_OK, data=response)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
