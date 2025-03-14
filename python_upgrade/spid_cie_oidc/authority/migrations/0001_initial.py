# Generated by Django 4.0.2 on 2022-02-13 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import spid_cie_oidc.authority.models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("spid_cie_oidc_entity", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FederationDescendant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "uid",
                    models.CharField(
                        default=spid_cie_oidc.authority.models.FederationDescendant.def_uid,
                        help_text="an unique code that identifies this entry. For italian public service it may be the IPA code.",
                        max_length=1024,
                        unique=True,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="human readable name of this entity. It may be a unit or organization name",
                        max_length=33,
                    ),
                ),
                (
                    "sub",
                    models.URLField(
                        help_text="URL that identifies this Entity in the Federation.",
                        max_length=255,
                        unique=True,
                        validators=[
                            spid_cie_oidc.authority.validators.validate_entity_configuration
                        ],
                    ),
                ),
                (
                    "type",
                    models.CharField(
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
                (
                    "metadata_policy",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="if present overloads the DEFAULT policy",
                    ),
                ),
                (
                    "constraints",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="if present overloads the DEFAULT policy",
                    ),
                ),
                (
                    "extended_claims",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="a dictionary containing any other claim like: jti, crti, policy_language_crit and any other extension",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("unreachable", "unreachable"),
                            ("valid", "valid"),
                            ("signature_failed", "signature_failed"),
                            ("not_valid", "not_valid"),
                            ("unknown", "unknown"),
                            ("expired", "expired"),
                        ],
                        default=False,
                        help_text="Its entity configuration is periodically fetched and validated.",
                        max_length=33,
                    ),
                ),
                (
                    "status_log",
                    models.JSONField(blank=True, default=dict, help_text="status log"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False, help_text="If this entity is active. "
                    ),
                ),
                (
                    "registrant",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Logged in users can modify only sub, contacts and jwks attributes, if they're owner of this entry. ",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Federation Entity Descendant",
                "verbose_name_plural": "Federation Entity Descendants",
            },
        ),
        migrations.CreateModel(
            name="FederationEntityProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(help_text="Profile name. ", max_length=33)),
                (
                    "profile_category",
                    models.CharField(
                        choices=[
                            ("federation_entity", "federation_entity"),
                            ("openid_relying_party", "openid_relying_party"),
                            ("openid_provider", "openid_provider"),
                            ("oauth_resource", "oauth_resource"),
                        ],
                        help_text="Profile id. It SHOULD be a URL but feel free to put whatever",
                        max_length=64,
                    ),
                ),
                (
                    "profile_id",
                    models.CharField(
                        help_text="Profile id. It SHOULD be a URL but feel free to put whatever",
                        max_length=1024,
                        unique=True,
                    ),
                ),
                (
                    "trust_mark_template",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="trust marks template for this profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Federation Entity Profile",
                "verbose_name_plural": "Federation Entity Profiles",
            },
        ),
        migrations.CreateModel(
            name="FederationEntityAssignedProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "descendant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_authority.federationdescendant",
                    ),
                ),
                (
                    "issuer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_entity.federationentityconfiguration",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_authority.federationentityprofile",
                    ),
                ),
            ],
            options={
                "verbose_name": "Federation Entity Descendant Assigned Profile",
                "verbose_name_plural": "Federation Descendant Assigned Profiles",
            },
        ),
        migrations.CreateModel(
            name="FederationDescendantJwk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "descendant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_authority.federationdescendant",
                    ),
                ),
                (
                    "jwk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_entity.publicjwk",
                    ),
                ),
            ],
            options={
                "verbose_name": "Federation Descendant Public JWK",
                "verbose_name_plural": "Federation Descendant Public JWKs",
            },
        ),
        migrations.CreateModel(
            name="FederationDescendantContact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "contact",
                    models.CharField(
                        help_text="any kind of contact type, usually an email.",
                        max_length=255,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("email", "email"),
                            ("telephone", "telephone"),
                            ("other", "other"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "entity",
                    models.ForeignKey(
                        help_text="Entity for which this contac is related",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="spid_cie_oidc_authority.federationdescendant",
                    ),
                ),
            ],
            options={
                "verbose_name": "Federation Entity Contact",
                "verbose_name_plural": "Federation Entity Contacts",
            },
        ),
    ]
