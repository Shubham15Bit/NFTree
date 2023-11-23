from django.db import models


class ContactMessage(models.Model):
    MESSAGE_TYPES = [
        ('General Inquiry', 'General Inquiry'),
        ('Support', 'Support'),
        ('Sales', 'Sales'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES, default='General Inquiry')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Add this line for timestamp

    def __str__(self):
        return f"{self.full_name} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
