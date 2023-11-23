from rest_framework import serializers
from .models import ContactMessage

class ContactMessageSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only =True)
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone_number', 'subject', 'message_type', 'message','timestamp']
