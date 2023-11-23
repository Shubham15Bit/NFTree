# contact/urls.py
from django.urls import path
from .views import ContactMessageCreateAPIView,ContactMessageListAPIView

urlpatterns = [
    path('contact-us/', ContactMessageCreateAPIView.as_view(), name='contact_us'),
    path('contact-messages/', ContactMessageListAPIView.as_view(), name='contact_messages_list'),
]
