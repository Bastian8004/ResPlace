# Generated by Django 5.0.6 on 2024-07-24 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Res", "0009_reservation_user_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
