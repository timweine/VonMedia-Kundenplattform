# Generated by Django 3.1.4 on 2022-04-25 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_brand_assets_brand_logos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand_Assets',
            new_name='Brand_Asset',
        ),
        migrations.RenameModel(
            old_name='Brand_Logos',
            new_name='Brand_Logo',
        ),
    ]