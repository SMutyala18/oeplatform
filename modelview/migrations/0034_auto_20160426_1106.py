# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-26 09:06
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("modelview", "0033_auto_20160407_1635")]

    operations = [
        migrations.CreateModel(
            name="Energystudy",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_of_the_study",
                    models.CharField(
                        help_text="What is the name of the study?",
                        max_length=1000,
                        verbose_name="Name of the study",
                    ),
                ),
                (
                    "author_Institution",
                    models.CharField(
                        help_text="Who are the authors of the study and for which institution do they work?",  # noqa
                        max_length=1000,
                        verbose_name="Author, Institution",
                    ),
                ),
                (
                    "client",
                    models.CharField(
                        help_text="Who are the customers requesting the study?",
                        max_length=1000,
                        null=True,
                        verbose_name="Client",
                    ),
                ),
                ("funding_private", models.BooleanField(verbose_name="private")),
                ("funding_public", models.BooleanField(verbose_name="public")),
                ("funding_no_funding", models.BooleanField(verbose_name="no funding")),
                (
                    "citation_reference",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000),
                        null=True,
                        size=None,
                        verbose_name="Citation reference",
                    ),
                ),
                (
                    "citation_doi",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000),
                        null=True,
                        size=None,
                        verbose_name="Citation doi",
                    ),
                ),
                (
                    "aim",
                    models.CharField(
                        help_text="What is the purpose (hypothesis) and research question of the study?",  # noqa
                        max_length=1000,
                        null=True,
                        verbose_name="Aim",
                    ),
                ),
                (
                    "new_aspects",
                    models.CharField(
                        help_text="What is new? (beyond state of research)",
                        max_length=1000,
                        null=True,
                        verbose_name="New aspects",
                    ),
                ),
                (
                    "spatial_Geographical_coverage",
                    models.CharField(
                        help_text="Which geographical region is adressed in the study?",
                        max_length=1000,
                        null=True,
                        verbose_name="Spatial / Geographical coverage",
                    ),
                ),
                ("time_frame_2020", models.BooleanField(verbose_name="2020")),
                ("time_frame_2030", models.BooleanField(verbose_name="2030")),
                ("time_frame_2050", models.BooleanField(verbose_name="2050")),
                ("time_frame_other", models.BooleanField(verbose_name="other")),
                ("time_frame_other_text", models.CharField(max_length=1000, null=True)),
                (
                    "time_frame_2_target_year",
                    models.BooleanField(verbose_name="target year"),
                ),
                (
                    "time_frame_2_transformation_path",
                    models.BooleanField(verbose_name="transformation path"),
                ),
                (
                    "tools_other",
                    models.CharField(
                        help_text="Which model(s) and other tools have been used?",
                        max_length=1000,
                        null=True,
                        verbose_name="Tools",
                    ),
                ),
                (
                    "modeled_energy_sectors_electricity",
                    models.BooleanField(verbose_name="electricity"),
                ),
                (
                    "modeled_energy_sectors_heat",
                    models.BooleanField(verbose_name="heat"),
                ),
                (
                    "modeled_energy_sectors_liquid_fuels",
                    models.BooleanField(verbose_name="liquid fuels"),
                ),
                ("modeled_energy_sectors_gas", models.BooleanField(verbose_name="gas")),
                (
                    "modeled_energy_sectors_others",
                    models.BooleanField(verbose_name="others"),
                ),
                (
                    "modeled_energy_sectors_others_text",
                    models.CharField(max_length=1000, null=True),
                ),
                (
                    "modeled_demand_sectors_households",
                    models.BooleanField(verbose_name="households"),
                ),
                (
                    "modeled_demand_sectors_industry",
                    models.BooleanField(verbose_name="industry"),
                ),
                (
                    "modeled_demand_sectors_commercial_sector",
                    models.BooleanField(verbose_name="commercial sector"),
                ),
                (
                    "modeled_demand_sectors_transport",
                    models.BooleanField(verbose_name="transport"),
                ),
                (
                    "economic_behavioral_perfect",
                    models.BooleanField(
                        verbose_name="single fictive decision-maker with perfect knowledge (perfect foresight optimization)"  # noqa
                    ),
                ),
                (
                    "economic_behavioral_myopic",
                    models.BooleanField(
                        verbose_name="single fictive decision-maker with myopic foresight (time-step optimization)"  # noqa
                    ),
                ),
                (
                    "economic_behavioral_qualitative",
                    models.BooleanField(
                        verbose_name="decisions simulated by modeller due to qualitative criteria (spread-sheet simulation)"  # noqa
                    ),
                ),
                (
                    "economic_behavioral_agentbased",
                    models.BooleanField(
                        verbose_name="representation of heterogenous decision rules for multiple agents (agent-based approach)"  # noqa
                    ),
                ),
                (
                    "economic_behavioral_other",
                    models.BooleanField(verbose_name="other"),
                ),
                (
                    "economic_behavioral_other_text",
                    models.CharField(max_length=1000, null=True),
                ),
                ("renewables_PV", models.BooleanField(verbose_name="PV")),
                ("renewables_wind", models.BooleanField(verbose_name="wind")),
                ("renewables_hydro", models.BooleanField(verbose_name="hydro")),
                ("renewables_biomass", models.BooleanField(verbose_name="biomass")),
                ("renewables_biogas", models.BooleanField(verbose_name="biogas")),
                ("renewables_solar", models.BooleanField(verbose_name="solar thermal")),
                ("renewables_others", models.BooleanField(verbose_name="others")),
                (
                    "renewables_others_text",
                    models.CharField(max_length=1000, null=True),
                ),
                (
                    "conventional_generation_gas",
                    models.BooleanField(verbose_name="gas"),
                ),
                (
                    "conventional_generation_coal",
                    models.BooleanField(verbose_name="coal"),
                ),
                (
                    "conventional_generation_oil",
                    models.BooleanField(verbose_name="oil"),
                ),
                (
                    "conventional_generation_liquid",
                    models.BooleanField(verbose_name="liquid fuels"),
                ),
                (
                    "conventional_generation_nuclear",
                    models.BooleanField(verbose_name="nuclear"),
                ),
                ("CHP", models.BooleanField(verbose_name="CHP")),
                (
                    "networks_electricity_gas_electricity",
                    models.BooleanField(verbose_name="electricity"),
                ),
                (
                    "networks_electricity_gas_gas",
                    models.BooleanField(verbose_name="gas"),
                ),
                (
                    "networks_electricity_gas_heat",
                    models.BooleanField(verbose_name="heat"),
                ),
                ("storages_battery", models.BooleanField(verbose_name="battery")),
                ("storages_kinetic", models.BooleanField(verbose_name="kinetic")),
                ("storages_CAES", models.BooleanField(verbose_name="compressed air")),
                ("storages_PHS", models.BooleanField(verbose_name="pump hydro")),
                ("storages_chemical", models.BooleanField(verbose_name="chemical")),
                (
                    "economic_focuses_included",
                    models.CharField(
                        help_text="Have there been economic focusses/sectors included?",
                        max_length=1000,
                        null=True,
                        verbose_name="Economic focuses included",
                    ),
                ),
                (
                    "social_focuses_included",
                    models.CharField(
                        help_text="Have there been social focusses/sectors included? ",
                        max_length=1000,
                        null=True,
                        verbose_name="Social focuses included",
                    ),
                ),
                (
                    "endogenous_variables",
                    models.CharField(
                        help_text="Which time series and variables are generated inside the model?",  # noqa
                        max_length=1000,
                        null=True,
                        verbose_name="Endogenous variables",
                    ),
                ),
                (
                    "sensitivities",
                    models.BooleanField(
                        help_text="Have there been sensitivities?",
                        verbose_name="Sensitivities",
                    ),
                ),
                ("time_steps_anual", models.BooleanField(verbose_name="anual")),
                ("time_steps_hour", models.BooleanField(verbose_name="hour")),
                ("time_steps_15_min", models.BooleanField(verbose_name="15 min")),
                ("time_steps_1_min", models.BooleanField(verbose_name="1 min")),
                ("time_steps_sec", models.BooleanField(verbose_name="sec")),
                ("time_steps_other", models.BooleanField(verbose_name="other")),
                ("time_steps_other_text", models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(model_name="energyscenario", name="CHP"),
        migrations.RemoveField(model_name="energyscenario", name="aim"),
        migrations.RemoveField(model_name="energyscenario", name="author_Institution"),
        migrations.RemoveField(model_name="energyscenario", name="citation_doi"),
        migrations.RemoveField(model_name="energyscenario", name="citation_reference"),
        migrations.RemoveField(model_name="energyscenario", name="client"),
        migrations.RemoveField(
            model_name="energyscenario", name="conventional_generation_coal"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="conventional_generation_gas"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="conventional_generation_liquid"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="conventional_generation_nuclear"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="conventional_generation_oil"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="economic_behavioral_agentbased"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="economic_behavioral_myopic"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="economic_behavioral_other"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="economic_behavioral_other_text"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="economic_behavioral_perfect"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="economic_behavioral_qualitative"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="economic_focuses_included"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="endogenous_variables"
        ),
        migrations.RemoveField(model_name="energyscenario", name="funding_no_funding"),
        migrations.RemoveField(model_name="energyscenario", name="funding_private"),
        migrations.RemoveField(model_name="energyscenario", name="funding_public"),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_demand_sectors_commercial_sector"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_demand_sectors_households"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_demand_sectors_industry"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_demand_sectors_transport"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_energy_sectors_electricity"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_energy_sectors_gas"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_energy_sectors_heat"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_energy_sectors_liquid_fuels"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_energy_sectors_others"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="modeled_energy_sectors_others_text"
        ),
        migrations.RemoveField(model_name="energyscenario", name="name_of_the_study"),
        migrations.RemoveField(
            model_name="energyscenario", name="networks_electricity_gas_electricity"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="networks_electricity_gas_gas"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="networks_electricity_gas_heat"
        ),
        migrations.RemoveField(model_name="energyscenario", name="new_aspects"),
        migrations.RemoveField(model_name="energyscenario", name="renewables_PV"),
        migrations.RemoveField(model_name="energyscenario", name="renewables_biogas"),
        migrations.RemoveField(model_name="energyscenario", name="renewables_biomass"),
        migrations.RemoveField(model_name="energyscenario", name="renewables_hydro"),
        migrations.RemoveField(model_name="energyscenario", name="renewables_others"),
        migrations.RemoveField(
            model_name="energyscenario", name="renewables_others_text"
        ),
        migrations.RemoveField(model_name="energyscenario", name="renewables_solar"),
        migrations.RemoveField(model_name="energyscenario", name="renewables_wind"),
        migrations.RemoveField(model_name="energyscenario", name="sensitivities"),
        migrations.RemoveField(
            model_name="energyscenario", name="social_focuses_included"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="spatial_Geographical_coverage"
        ),
        migrations.RemoveField(model_name="energyscenario", name="storages_CAES"),
        migrations.RemoveField(model_name="energyscenario", name="storages_PHS"),
        migrations.RemoveField(model_name="energyscenario", name="storages_battery"),
        migrations.RemoveField(model_name="energyscenario", name="storages_chemical"),
        migrations.RemoveField(model_name="energyscenario", name="storages_kinetic"),
        migrations.RemoveField(model_name="energyscenario", name="time_frame_2020"),
        migrations.RemoveField(model_name="energyscenario", name="time_frame_2030"),
        migrations.RemoveField(model_name="energyscenario", name="time_frame_2050"),
        migrations.RemoveField(
            model_name="energyscenario", name="time_frame_2_target_year"
        ),
        migrations.RemoveField(
            model_name="energyscenario", name="time_frame_2_transformation_path"
        ),
        migrations.RemoveField(model_name="energyscenario", name="time_frame_other"),
        migrations.RemoveField(
            model_name="energyscenario", name="time_frame_other_text"
        ),
        migrations.RemoveField(model_name="energyscenario", name="time_steps_15_min"),
        migrations.RemoveField(model_name="energyscenario", name="time_steps_1_min"),
        migrations.RemoveField(model_name="energyscenario", name="time_steps_anual"),
        migrations.RemoveField(model_name="energyscenario", name="time_steps_hour"),
        migrations.RemoveField(model_name="energyscenario", name="time_steps_other"),
        migrations.RemoveField(
            model_name="energyscenario", name="time_steps_other_text"
        ),
        migrations.RemoveField(model_name="energyscenario", name="time_steps_sec"),
        migrations.RemoveField(model_name="energyscenario", name="tools_models"),
        migrations.RemoveField(model_name="energyscenario", name="tools_other"),
        migrations.AlterField(
            model_name="energymodel",
            name="transfer_electricity_transition",
            field=models.BooleanField(default=False, verbose_name="transmission"),
        ),
        migrations.AlterField(
            model_name="energymodel",
            name="transfer_gas_transition",
            field=models.BooleanField(default=False, verbose_name="transmission"),
        ),
        migrations.AlterField(
            model_name="energymodel",
            name="transfer_heat_transition",
            field=models.BooleanField(default=False, verbose_name="transmission"),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="emission_reductions_amount",
            field=models.SmallIntegerField(
                help_text="Development of emissions",
                null=True,
                verbose_name="Emission reductions",
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="emission_reductions_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="not estimated",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="energy_saving_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="not estimated",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="potential_energy_savings_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="not estimated",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_heat_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="not estimated",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_mobility_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="not estimated",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_power_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="not estimated",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="energyscenario",
            name="share_RE_total_kind",
            field=models.CharField(
                choices=[
                    ("until", "until"),
                    ("per", "per"),
                    ("not estimated", "not estimated"),
                ],
                default="not estimated",
                max_length=15,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="energystudy",
            name="tools_models",
            field=models.ForeignKey(
                help_text="Which model(s) and other tools have been used?",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="modelview.Energymodel",
                verbose_name="Tools",
            ),
        ),
        migrations.AddField(
            model_name="energyscenario",
            name="study",
            field=models.ForeignKey(
                blank=True,
                db_column="name_of_the_study_id",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="modelview.Energystudy",
            ),
        ),
    ]
