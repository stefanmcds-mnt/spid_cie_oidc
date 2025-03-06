# Generated by Django 4.2.1 on 2023-07-09 15:44

from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("spid_cie_oidc_onboarding", "0008_onboardingregistration_auth_request_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onboardingregistration",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("federation_entity", "federation_entity"),
                    ("openid_relying_party", "openid_relying_party"),
                    ("openid_provider", "openid_provider"),
                    ("oauth_resource", "oauth_resource"),
                    ("wallet_provider", "wallet_provider"),
                    ("wallet_relying_party", "wallet_relying_party"),
                ],
                default="openid_relying_party",
                help_text="OpenID Connect Federation entity type",
                max_length=33,
            ),
        ),
    ]
