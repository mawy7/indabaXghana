# Generated by Django 2.2.5 on 2020-02-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20200211_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='team.png', upload_to='static/photos/'),
        ),
    ]
