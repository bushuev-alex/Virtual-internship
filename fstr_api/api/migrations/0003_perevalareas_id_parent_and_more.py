# Generated by Django 4.2.2 on 2023-07-01 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_perevalimages_date_added"),
    ]

    operations = [
        migrations.AddField(
            model_name="perevalareas",
            name="id_parent",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="perevalimages",
            name="date_added",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 1, 18, 46, 12, 918805, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
