# Generated by Django 3.2.9 on 2021-11-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceCode', '0007_auto_20211129_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancelog',
            name='lat',
            field=models.DecimalField(decimal_places=8, default=55.70636, max_digits=10),
        ),
        migrations.AlterField(
            model_name='attendancelog',
            name='long',
            field=models.DecimalField(decimal_places=8, default=12.53917, max_digits=10),
        ),
    ]