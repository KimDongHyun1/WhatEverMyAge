# Generated by Django 2.2.3 on 2019-08-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20190808_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='cnt',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
