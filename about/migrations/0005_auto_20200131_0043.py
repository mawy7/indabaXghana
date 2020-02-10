# Generated by Django 2.2.5 on 2020-01-31 00:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0004_auto_20200131_0014'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team',
            new_name='About',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='image',
            new_name='team_member_image',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='linkedin',
            new_name='team_member_linkedin',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='name',
            new_name='team_member_name',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='twitter',
            new_name='team_member_twitter',
        ),
    ]