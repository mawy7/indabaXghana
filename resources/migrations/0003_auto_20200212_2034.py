# Generated by Django 2.2.5 on 2020-02-12 20:34

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20200212_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(default='team.png', upload_to='static/photos/'),
        ),
    ]
