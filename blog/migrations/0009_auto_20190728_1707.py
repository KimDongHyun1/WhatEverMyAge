# Generated by Django 2.2.3 on 2019-07-28 08:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190728_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='author',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]