# Generated by Django 4.0.2 on 2022-03-06 22:36

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_authority', '0003_alter_federationdescendantcontact_entity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='federationdescendant',
            name='jwks',
            field=models.JSONField(default=list, help_text='a list of public keys'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FederationDescendantJwk',
        ),
    ]
