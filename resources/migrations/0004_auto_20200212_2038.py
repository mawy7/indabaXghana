# Generated by Django 2.2.5 on 2020-02-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20200212_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='indabax_edition',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_description',
            field=models.TextField(blank=True, default=' ', null=True),
        ),
    ]
