# Generated by Django 2.2.1 on 2019-06-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0017_auto_20190603_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
