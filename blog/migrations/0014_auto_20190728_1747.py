# Generated by Django 2.2.3 on 2019-07-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20190728_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=50, default=0.0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='posting',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=50, default=0.0, max_digits=50),
        ),
    ]
