# Generated by Django 2.2.3 on 2019-07-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190723_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='user_photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
