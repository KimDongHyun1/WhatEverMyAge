# Generated by Django 2.2.3 on 2019-07-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190728_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
    ]
