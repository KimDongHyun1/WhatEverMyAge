# Generated by Django 2.2.3 on 2019-08-04 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_posting_likedusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='likedusers',
            field=models.TextField(),
        ),
    ]
