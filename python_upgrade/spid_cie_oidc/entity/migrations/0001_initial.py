# Generated by Django 4.0.2 on 2022-02-13 09:06

from django.db import migrations, models
import spid_cie_oidc.entity.models
import spid_cie_oidc.entity.validators
import uuid

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FederationEntityConfiguration",
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
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "sub",
                    models.URLField(
                        help_text="URL that identifies this Entity in the Federation. This value and iss are the same in the Entity Configuration.",
                        max_length=255,
                    ),
                ),
                (
                    "default_exp",
                    models.PositiveIntegerField(
                        default=33,
                        help_text="how many minutes from now() an issued statement must expire",
                    ),
                ),
                (
                    "default_signature_alg",
                    models.CharField(
                        default="RS256",
                        help_text="default signature algorithm, eg: RS256",
                        max_length=16,
                    ),
                ),
                (
                    "authority_hints",
                    models.JSONField(
                        blank=True,
                        default=list,
                        help_text="only required if this Entity is an intermediary",
                    ),
                ),
                (
                    "jwks",
                    models.JSONField(
                        default=spid_cie_oidc.entity.models.FederationEntityConfiguration._create_jwks,
                        help_text="a list of public keys",
                    ),
                ),
                (
                    "trust_marks",
                    models.JSONField(
                        blank=True,
                        default=list,
                        help_text="which trust marks MUST be exposed in its entity configuration",
                    ),
                ),
                (
                    "trust_mark_issuers",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text='Only usable for Trust Anchors and intermediates. Which issuers are allowed to issue trust marks for the descendants. Example: {"https://www.spid.gov.it/certification/rp": ["https://registry.spid.agid.gov.it", "https://intermediary.spid.it"],"https://sgd.aa.it/onboarding": ["https://sgd.aa.it", ]}',
                    ),
                ),
                (
                    "metadata",
                    models.JSONField(
                        default=dict,
                        help_text='federation_entity metadata, eg: {"federation_entity": { ... },"openid_provider": { ... },"openid_relying_party": { ... },"oauth_resource": { ... }}',
                        validators=[
                            spid_cie_oidc.entity.validators.validate_entity_metadata
                        ],
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=False,
                        help_text="If this configuration is active. At least one configuration must be active",
                    ),
                ),
            ],
            options={
                "verbose_name": "Federation Entity Configuration",
                "verbose_name_plural": "Federation Entity Configurations",
            },
        ),
        migrations.CreateModel(
            name="PublicJwk",
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
                    "kid",
                    models.CharField(
                        help_text="unique code that identifies this jwks. ",
                        max_length=1024,
                        unique=True,
                    ),
                ),
                (
                    "jwk",
                    models.JSONField(
                        default=dict,
                        help_text="Public jwk",
                        validators=[
                            spid_cie_oidc.entity.validators.validate_public_jwks
                        ],
                    ),
                ),
            ],
            options={
                "verbose_name": "Public JWKs",
                "verbose_name_plural": "Public JWKs",
            },
        ),
        migrations.CreateModel(
            name="TrustChain",
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
                    "sub",
                    models.URLField(
                        help_text="URL that identifies this Entity in the Federation. ",
                        max_length=255,
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
                        default="openid_provider",
                        help_text="OpenID Connect Federation entity type",
                        max_length=33,
                    ),
                ),
                ("exp", models.DateTimeField()),
                ("iat", models.DateTimeField()),
                (
                    "chain",
                    models.JSONField(
                        blank=True,
                        default=list,
                        help_text="A list of entity statements collected during the metadata discovery",
                    ),
                ),
                (
                    "resultant_metadata",
                    models.JSONField(
                        default=dict,
                        help_text="The final metadata applied with the metadata policy built over the chain",
                    ),
                ),
                (
                    "parties_involved",
                    models.JSONField(
                        blank=True,
                        default=list,
                        help_text="subjects involved in the metadata discovery",
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
                        help_text="Status of this trust chain, on each update.",
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
                        default=True,
                        help_text="If you need to disable the trust to this subject, deacticate this",
                    ),
                ),
            ],
            options={
                "verbose_name": "Trust Chain",
                "verbose_name_plural": "Trust Chains",
                "unique_together": {("sub", "type")},
            },
        ),
    ]
