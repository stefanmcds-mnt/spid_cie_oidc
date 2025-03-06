# Generated by Django 4.0.5 on 2022-10-18 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import spid_cie_oidc.entity.utils

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spid_cie_oidc_entity', '0018_trustchain_jwks'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(default=spid_cie_oidc.entity.utils.random_token, help_text='it will be generated automatically.', max_length=255)),
                ('expire_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(help_text='The user responsible of thi token', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff Token',
                'verbose_name_plural': 'Staff Tokens',
            },
        ),
    ]
