# Generated by Django 2.2.5 on 2020-02-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0007_auto_20200131_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='talk_description',
            field=models.TextField(default=' '),
        ),
    ]
