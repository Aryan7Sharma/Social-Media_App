# Generated by Django 4.1.4 on 2022-12-27 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="profile", name="id_user", field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="profile",
            name="profileimg",
            field=models.ImageField(
                default="blank-profile-picture.jpg", upload_to="profile_images"
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
