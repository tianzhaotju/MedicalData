# Generated by Django 2.2 on 2019-09-04 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('After_op', '0002_auto_20190902_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afteroperate',
            name='after_out_date',
            field=models.DateField(verbose_name='出院日期'),
        ),
    ]
