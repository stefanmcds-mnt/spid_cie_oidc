# Generated by Django 4.2.1 on 2023-07-13 04:54

from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        (
            "spid_cie_oidc_entity",
            "0029_alter_federationentityconfiguration_entity_type_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="federationentityconfiguration",
            name="issue_x509",
        ),
    ]
