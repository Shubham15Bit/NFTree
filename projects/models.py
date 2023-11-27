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


def plant_image_upload(instance, filename):
    file_extension = filename.split(".")[-1]
    new_file_name = str(random.randrange(1000, 1000000)) + "." + file_extension
    return "/".join(["plant_image", new_file_name])


class PlantImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=plant_image_upload)
    project = models.ForeignKey("ProjectInfo", on_delete=models.CASCADE)


class ProjectInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(default="", null=True, blank=True)
    plant_types = models.CharField(max_length=500, blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    plant_planned = models.IntegerField(blank=True, null=True)
    plants_planted = models.IntegerField(blank=True, null=True)
    donation = models.IntegerField(blank=True, null=True)
    # donation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    document = models.FileField(upload_to=document_upload, blank=True, null=True)
    image = models.FileField(upload_to=image_upload, blank=True, null=True)
    is_completed = models.BooleanField(default=False)


class Transaction(models.Model):
    project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trees_count = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name}'s donation for {self.project.name}"
    

class ProjectReport(models.Model):
    project = models.OneToOneField(ProjectInfo, on_delete=models.CASCADE)
    # total_plants = models.IntegerField(blank=True, null=True)
    # plant_types = models.CharField(max_length=500, blank=True, null=True)
    trees_age = models.CharField(max_length=100, blank=True, null=True)
    trees_growth = models.CharField(max_length=100, blank=True, null=True)
    co2_absorption = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    oxygen_emission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    leaf_health = models.CharField(max_length=100, blank=True, null=True)
    root_health = models.CharField(max_length=100, blank=True, null=True)
    soil_nitrogen = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    soil_phosphorus = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    soil_potassium = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Report for {self.project.name}"
    