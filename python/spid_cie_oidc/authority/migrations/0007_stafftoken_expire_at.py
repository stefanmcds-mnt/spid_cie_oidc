# Generated by Django 4.0.3 on 2022-03-20 10:53

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('spid_cie_oidc_authority', '0006_stafftoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='stafftoken',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
