# Generated by Django 4.0.2 on 2022-03-07 08:58

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_relying_party', '0002_rename_issuer_oidcauthentication_provider_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oidcauthenticationtoken',
            old_name='logged_out',
            new_name='revoked',
        ),
        migrations.AddField(
            model_name='oidcauthenticationtoken',
            name='refresh_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
