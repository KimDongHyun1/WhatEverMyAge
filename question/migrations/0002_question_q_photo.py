# Generated by Django 2.2.3 on 2019-08-07 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='q_photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
