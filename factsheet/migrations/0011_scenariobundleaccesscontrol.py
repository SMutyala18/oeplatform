# Generated by Django 3.2.22 on 2023-11-30 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('factsheet', '0010_rename_user_id_oekg_modifications_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScenarioBundleAccessControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bundle_id', models.CharField(default='none', max_length=400)),
                ('owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenario_bundle_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
