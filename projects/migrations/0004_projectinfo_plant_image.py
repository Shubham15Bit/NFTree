# Generated by Django 4.2.6 on 2023-11-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_plantimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="projectinfo",
            name="plant_image",
            field=models.ManyToManyField(blank=True, to="projects.plantimage"),
        ),
    ]