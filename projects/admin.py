from django.contrib import admin
from .models import ProjectInfo, PlantImage, Transaction, ProjectReport

# Register your models here.

admin.site.register(ProjectInfo)
admin.site.register(PlantImage)
admin.site.register(Transaction)
admin.site.register(ProjectReport)
