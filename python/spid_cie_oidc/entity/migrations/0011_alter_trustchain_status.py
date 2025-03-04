# Generated by Django 4.0.2 on 2022-03-01 16:03

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("spid_cie_oidc_entity", "0010_federationentityconfiguration_entity_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trustchain",
            name="status",
            field=models.CharField(
                choices=[
                    ("unreachable", "unreachable"),
                    ("valid", "valid"),
                    ("signature_failed", "signature_failed"),
                    ("not_valid", "not_valid"),
                    ("unknown", "unknown"),
                    ("expired", "expired"),
                ],
                default="unreachable",
                help_text="Status of this trust chain, on each update.",
                max_length=33,
            ),
        ),
    ]
