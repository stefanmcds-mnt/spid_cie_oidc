# Generated by Django 4.0.2 on 2022-02-25 14:55

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("spid_cie_oidc_entity", "0007_alter_trustchain_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="fetchedentitystatement",
            name="jwt",
            field=models.CharField(default="", max_length=2048),
            preserve_default=False,
        ),
    ]
