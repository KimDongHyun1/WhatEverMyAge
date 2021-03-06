# Generated by Django 2.2.3 on 2019-08-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_pictures_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pictures',
            name='picture',
            field=models.URLField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
