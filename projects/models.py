from django.db import models
from django.contrib.auth.models import User
import random


def document_upload(instance, filename):
    file_extension = filename.split(".")[-1]
    new_file_name = str(random.randrange(1000, 1000000)) + "." + file_extension
    return "/".join(["documents", new_file_name])


def image_upload(instance, filename):
    file_extension = filename.split(".")[-1]
    new_file_name = str(random.randrange(1000, 1000000)) + "." + file_extension
    return "/".join(["image", new_file_name])


# Create your models here.
class ProjectInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(default="", null=True, blank=True)
    plantTypes = models.CharField(max_length=500, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    plantPlanned = models.IntegerField(blank=True, null=True)
    donation = models.IntegerField(blank=True, null=True)
    # donation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    document = models.FileField(upload_to=document_upload, blank=True, null=True)
    image = models.FileField(upload_to=image_upload, blank=True, null=True)
