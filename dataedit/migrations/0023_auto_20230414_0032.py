# Generated by Django 3.2.13 on 2023-04-13 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dataedit', '0022_peerreview_datestarted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peerreview',
            old_name='dateStarted',
            new_name='date_started',
        ),
        migrations.AddField(
            model_name='peerreview',
            name='contributor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='peerreview',
            name='reviewer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='table',
            name='is_reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
