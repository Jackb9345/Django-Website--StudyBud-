# Generated by Django 4.1.2 on 2022-11-12 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_room_options_room_participants"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="message", options={"ordering": ["-updated", "-created"]},
        ),
    ]
