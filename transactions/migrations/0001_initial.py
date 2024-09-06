# Generated by Django 5.1.1 on 2024-09-06 10:19

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "transaction_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "transfer_to",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "received_from",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("amount", models.CharField(max_length=8)),
                ("is_credit", models.BooleanField(default=False)),
                ("not_pending", models.BooleanField(default=False)),
                ("done_on", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]