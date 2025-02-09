# Generated by Django 3.0 on 2020-04-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modelview", "0052_auto_20200408_1308"),
    ]

    operations = [
        migrations.AddField(
            model_name="energyframework",
            name="data_postprocessing",
            field=models.BooleanField(
                default=False,
                help_text="Which output format(s) can the framework apply? Please list!",  # noqa
                verbose_name="data postprocessing",
            ),
        ),
        migrations.AlterField(
            model_name="energyframework",
            name="agricultural_demand",
            field=models.BooleanField(
                default=False,
                help_text="Which agricultural demands are already modelled with the framework?",  # noqa
                verbose_name="Agricultural demand",
            ),
        ),
        migrations.AlterField(
            model_name="energyframework",
            name="gm_singleNode",
            field=models.BooleanField(default=False, verbose_name="Single-node model"),
        ),
    ]
