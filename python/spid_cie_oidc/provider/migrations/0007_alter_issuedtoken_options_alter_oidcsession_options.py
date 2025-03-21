# Generated by Django 4.0.3 on 2022-03-19 17:20

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_provider', '0006_oidcsession_acr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issuedtoken',
            options={'verbose_name': 'Issued Token', 'verbose_name_plural': 'Issued Tokens'},
        ),
        migrations.AlterModelOptions(
            name='oidcsession',
            options={'ordering': ['-created'], 'verbose_name': 'User Session', 'verbose_name_plural': 'User Sessions'},
        ),
    ]
