# Generated by Django 2.2.3 on 2019-07-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190728_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_id',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='author_username',
            field=models.TextField(blank=True),
        ),
    ]