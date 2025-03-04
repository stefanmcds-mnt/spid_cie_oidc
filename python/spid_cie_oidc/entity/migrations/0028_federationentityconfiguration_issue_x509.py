# Generated by Django 4.2.1 on 2023-07-09 15:23

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        (
            "spid_cie_oidc_entity",
            "0027_alter_federationhistoricalkey_revocation_motivation",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="federationentityconfiguration",
            name="issue_x509",
            field=models.BooleanField(
                default=False,
                help_text="If TA/Intermediate: issues x509 in both entity statements and configuration. if leaf, issues x509 certificates in configuration.",
            ),
        ),
    ]
