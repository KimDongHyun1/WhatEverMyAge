# Generated by Django 2.2.3 on 2019-08-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20190803_2302'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='pictures',
            name='picture',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
