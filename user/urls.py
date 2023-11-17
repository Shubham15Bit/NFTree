from django.urls import path
from user.views import (
    UserCreate,
    ProfilePictureListCreateView,
    ProfilePictureDetailView,
    AccountListCreateView,
    AccountRetrieveUpdateDestroyView,
    EmailListView,
    UserEmailDetailView,
    UserEmailVerifyView,
    OrganizationListCreateView,
    OrganizationRetrieveUpdateDestroyView,
    KYCListView,
    KYCDetailView,
)
from user.authviews import SocialLoginView, UserLoginView

urlpatterns = [
    path("register/", UserCreate.as_view(), name="user-create"),
    path("login/", UserLoginView.as_view(), name="token_obtain_pair"),
    path("auth/", SocialLoginView.as_view(), name="social-auth"),

    path('avatar/', ProfilePictureListCreateView.as_view(), name='profile-picture-list-create'),
    path('avatar/<int:pk>/', ProfilePictureDetailView.as_view(), name='profile-picture-detail'),

    path("account/", AccountListCreateView.as_view()),
    path("account/<int:pk>/", AccountRetrieveUpdateDestroyView.as_view()),

    path("email/", EmailListView.as_view()),
    path("email/<int:pk>/", UserEmailDetailView.as_view()),
    path("verify-email/<int:pk>/", UserEmailVerifyView.as_view()),

    path("organization/", OrganizationListCreateView.as_view()),
    path("organization/<int:pk>/", OrganizationRetrieveUpdateDestroyView.as_view()),
    
    path("kyc/", KYCListView.as_view()),
    path("kyc/<int:pk>/", KYCDetailView.as_view()),
]
