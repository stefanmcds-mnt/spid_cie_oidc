# Generated by Django 4.0.2 on 2022-02-25 16:04

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        (
            "spid_cie_oidc_onboarding",
            "0002_alter_onboardingregistration_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="onboardingregistration",
            options={
                "ordering": ["-created"],
                "verbose_name": "OnBoarding Registration",
                "verbose_name_plural": "OnBoarding Registrations",
            },
        ),
    ]
