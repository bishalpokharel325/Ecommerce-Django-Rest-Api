# Generated by Django 3.1.7 on 2021-02-27 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='online',
            new_name='visible',
        ),
        migrations.RenameField(
            model_name='primarycategory',
            old_name='online',
            new_name='visible',
        ),
        migrations.RenameField(
            model_name='secondarycategory',
            old_name='online',
            new_name='visible',
        ),
    ]
