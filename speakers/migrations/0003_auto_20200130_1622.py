# Generated by Django 2.2.5 on 2020-01-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_auto_20200130_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speaker',
            name='status',
        ),
        migrations.AddField(
            model_name='speaker',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
    ]
