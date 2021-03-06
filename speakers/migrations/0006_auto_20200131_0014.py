# Generated by Django 2.2.5 on 2020-01-31 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0005_auto_20200130_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='linkedin',
            field=models.CharField(default=' ', help_text='Please enter only the user name eg. in/mawy7 ', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='twitter',
            field=models.CharField(default=' ', help_text="Please enter only the user name eg.'mawy_7' ", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='website',
            field=models.CharField(default=' ', max_length=100, null=True),
        ),
    ]
