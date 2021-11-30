# Generated by Django 3.2.9 on 2021-11-29 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceCode', '0006_alter_attendancecode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancelog',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=55.70636, max_digits=10),
        ),
        migrations.AddField(
            model_name='attendancelog',
            name='long',
            field=models.DecimalField(decimal_places=6, default=12.53917, max_digits=10),
        ),
    ]
