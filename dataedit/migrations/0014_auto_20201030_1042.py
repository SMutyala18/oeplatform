# Generated by Django 3.0.4 on 2020-10-30 09:42

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dataedit", "0013_auto_20170810_1031"),
    ]

    operations = [
        migrations.AddField(
            model_name="table",
            name="search",
            field=django.contrib.postgres.search.SearchVectorField(default=""),
        ),
    ]
