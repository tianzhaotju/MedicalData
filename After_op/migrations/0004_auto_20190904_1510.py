# Generated by Django 2.2 on 2019-09-04 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('After_op', '0003_auto_20190904_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afteroperate',
            name='after_cs',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='残石'),
        ),
        migrations.AlterField(
            model_name='afteroperate',
            name='after_cx',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='术后出血'),
        ),
        migrations.AlterField(
            model_name='afteroperate',
            name='after_dl',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='胆漏'),
        ),
        migrations.AlterField(
            model_name='afteroperate',
            name='after_fr',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='发热'),
        ),
        migrations.AlterField(
            model_name='afteroperate',
            name='after_ft',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='腹痛'),
        ),
        migrations.AlterField(
            model_name='afteroperate',
            name='after_fz',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='腹胀'),
        ),
        migrations.AlterField(
            model_name='afteroperate',
            name='after_ot',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='呕吐'),
        ),
        migrations.AlterField(
            model_name='afteroperate',
            name='after_yxy',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=10, verbose_name='胰腺炎'),
        ),
    ]
