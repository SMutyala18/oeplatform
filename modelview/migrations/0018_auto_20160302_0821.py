# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-02 07:21
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("modelview", "0017_auto_20160302_0819")]

    operations = [
        migrations.AlterField(
            model_name="basicfactsheet",
            name="additional_software",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    help_text="Which additional software is required to run the model?",
                    max_length=1000,
                ),
                default=list,
                size=None,
                verbose_name="Additional software (comma-separated)",
            ),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="institutions",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    help_text="Which institutions develop(ed) the model?",
                    max_length=1000,
                ),
                default=list,
                null=True,
                size=None,
                verbose_name="Institution(s) (comma-separated)",
            ),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="interal_data_processing_software",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    help_text="Which data processing software is required?",
                    max_length=1000,
                ),
                default=list,
                null=True,
                size=None,
                verbose_name="Internal data processing software (comma-separated)",
            ),
        ),
        migrations.AlterField(
            model_name="basicfactsheet",
            name="modelling_software",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    help_text="What modelling software and which version is used?",
                    max_length=1000,
                ),
                default=list,
                null=True,
                size=None,
                verbose_name="Modelling software  (comma-separated)",
            ),
        ),
        migrations.AlterField(
            model_name="energyframework",
            name="used",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=1000),
                default=list,
                null=True,
                size=None,
                verbose_name="Models using this framework (comma-separated)",
            ),
        ),
        migrations.AlterField(
            model_name="energymodel",
            name="geographical_coverage",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    help_text="What regions are covered? Please, list the regions covered by the model. Leave blank, if the model and data are not limited to a specific region. Example input: USA, Canada, Mexico",  # noqa
                    max_length=1000,
                ),
                default=list,
                null=True,
                size=None,
                verbose_name="Geographical coverage (comma-separated)",
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="citation_doi",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=1000),
                null=True,
                size=None,
                verbose_name="Citation doi (comma-separated)",
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="citation_reference",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=1000),
                null=True,
                size=None,
                verbose_name="Citation reference (comma-separated)",
            ),
        ),
    ]
