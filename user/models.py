from django.db import models
from django.contrib.auth.models import User
import random


def fileupload(instance, filename):
    file_extension = filename.split(".")[-1]
    new_file_name = str(random.randrange(1000, 1000000)) + "." + file_extension
    return "/".join(["user", new_file_name])


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, blank=True, null=True)
    wallet = models.CharField(max_length=100, blank=True, null=True)


class UserEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    reg_id = models.CharField(max_length=50, blank=True, null=True)
    reg_proof = models.FileField(upload_to=fileupload, blank=True, null=True)


class KYC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50, blank=True, null=True)
    is_applied = models.BooleanField(default=False)
    status_option = (
        ("unverified", "unverified"),
        ("in_progress", "in_progress"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Revoked", "Revoked"),
    )
    status = models.CharField(
        max_length=20, choices=status_option, default="unverified"
    )
