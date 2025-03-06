# Generated by Django 4.0.2 on 2022-02-14 15:16

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("spid_cie_oidc_entity", "0003_federationentityconfiguration_constraints"),
    ]

    operations = [
        migrations.AlterField(
            model_name="federationentityconfiguration",
            name="authority_hints",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="only required if this Entity is an intermediary or leaf.",
            ),
        ),
        migrations.AlterField(
            model_name="federationentityconfiguration",
            name="default_exp",
            field=models.PositiveIntegerField(
                default=2880,
                help_text="how many minutes from now() an issued statement must expire",
            ),
        ),
    ]
