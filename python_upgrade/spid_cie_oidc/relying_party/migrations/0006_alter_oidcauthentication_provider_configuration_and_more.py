# Generated by Django 4.0.2 on 2022-03-07 11:27

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_relying_party', '0005_rename_logged_out_oidcauthenticationtoken_revoked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oidcauthentication',
            name='provider_configuration',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='oidcauthentication',
            name='state',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]
