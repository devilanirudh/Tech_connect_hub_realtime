# Generated by Django 5.1.4 on 2024-12-20 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0008_alter_project_options"),
        ("users", "0006_alter_profile_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.profile",
            ),
        ),
    ]
