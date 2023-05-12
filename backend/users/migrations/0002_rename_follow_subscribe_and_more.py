# Generated by Django 4.2 on 2023-05-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follow',
            new_name='Subscribe',
        ),
        migrations.RemoveConstraint(
            model_name='subscribe',
            name='unique_follow',
        ),
        migrations.AddConstraint(
            model_name='subscribe',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_subscribe'),
        ),
    ]