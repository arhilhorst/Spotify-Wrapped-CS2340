# Generated by Django 5.1.2 on 2024-11-21 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wrapped", "0007_spotifyuser_personality_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="savedwrap",
            name="personality_info",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
