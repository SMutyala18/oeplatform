# Generated by Django 3.0 on 2020-11-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedimages",
            name="image",
            field=models.ImageField(upload_to="image/%Y/%m/"),
        ),
    ]
