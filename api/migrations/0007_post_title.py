# Generated by Django 2.2.3 on 2019-07-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
