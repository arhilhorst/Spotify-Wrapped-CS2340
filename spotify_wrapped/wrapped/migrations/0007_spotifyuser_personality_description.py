# Generated by Django 5.1 on 2024-11-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wrapped", "0006_alter_savedwrap_holiday_theme_alter_savedwrap_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="spotifyuser",
            name="personality_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
