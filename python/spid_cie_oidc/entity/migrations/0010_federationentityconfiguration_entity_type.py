# Generated by Django 4.0.2 on 2022-02-26 23:30

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("spid_cie_oidc_entity", "0009_trustchain_trust_marks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="federationentityconfiguration",
            name="entity_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("federation_entity", "federation_entity"),
                    ("openid_relying_party", "openid_relying_party"),
                    ("openid_provider", "openid_provider"),
                    ("oauth_resource", "oauth_resource"),
                ],
                default="openid_relying_party",
                help_text="OpenID Connect Federation entity type",
                max_length=33,
            ),
        ),
    ]
