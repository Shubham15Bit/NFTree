from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import (
    UserSerializer,
    AccountSerializer,
    UserEmailSerializer,
    OrganizationSerializer,
    KYCSerializer,
)
from user.models import Account, Organization, UserEmail, KYC
from django.core.mail import send_mail
import random
from user.mail import send_otp_email, send_kyc_email


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class AccountListCreateView(generics.ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        account, created = Account.objects.get_or_create(user=self.request.user)
        return Account.objects.filter(user=self.request.user)


class AccountRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class EmailListView(generics.ListAPIView):
    serializer_class = UserEmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_email, created = UserEmail.objects.get_or_create(user=self.request.user)
        return UserEmail.objects.filter(user=self.request.user)


class UserEmailDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserEmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_email, created = UserEmail.objects.get_or_create(user=self.request.user)
        return UserEmail.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        instance = self.get_object()
        email = self.request.data.get("email")

        if email:
            otp = send_otp_email(email)  # Send OTP to the provided email
            instance.otp = otp
            instance.email = None  # Do not update the email directly
            instance.save()
            print(instance.otp)
            return Response(
                {"detail": "OTP has been sent to your email address."},
                status=status.HTTP_200_OK,
            )

        serializer.save()


class UserEmailVerifyView(generics.UpdateAPIView):
    serializer_class = UserEmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserEmail.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        otp = request.data.get("otp")
        print(instance.otp)
        print(otp)

        if not otp:
            return Response(
                {"detail": "OTP is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if instance.otp == int(otp):
            email = request.data.get("email")
            instance.email = email
            instance.otp = None
            instance.save()
            return Response(
                {"detail": "Email address has been verified and updated."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "Invalid OTP."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class OrganizationListCreateView(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        account, created = Organization.objects.get_or_create(user=self.request.user)
        return Organization.objects.filter(user=self.request.user)


class OrganizationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Organization.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user, is_verified=False)


class KYCListView(generics.ListAPIView):
    serializer_class = KYCSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        kyc, created = KYC.objects.get_or_create(user=self.request.user)
        return KYC.objects.filter(user=self.request.user)


class KYCDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = KYCSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return KYC.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        send_kyc_email()
        serializer.save()
