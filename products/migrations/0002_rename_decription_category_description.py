# Generated by Django 4.2 on 2023-12-18 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='decription',
            new_name='description',
        ),
    ]
