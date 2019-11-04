# Generated by Django 2.2 on 2019-09-01 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TUS',
            fields=[
                ('B_check_id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False, verbose_name='检查号')),
                ('B_dnsize1', models.FloatField(default=0, verbose_name='胆囊大小')),
                ('B_dnsize2', models.FloatField(default=0, verbose_name='')),
                ('B_dnbhd', models.FloatField(default=0, verbose_name='胆囊壁厚度')),
                ('B_dnjsnum', models.IntegerField(default=0, verbose_name='胆囊结石数目')),
                ('B_dnjszj', models.FloatField(default=0, verbose_name='胆囊结石最大直径')),
                ('B_dzgzj', models.FloatField(default=0, verbose_name='胆总管最大直径')),
                ('B_dzgjsnum', models.IntegerField(default=0, verbose_name='胆管结石数目')),
                ('B_dzgjszj', models.FloatField(default=0, verbose_name='胆管结石最大直径')),
                ('B_patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.Patient', verbose_name='就诊号')),
            ],
            options={
                'verbose_name': 'TUS',
                'verbose_name_plural': 'TUS',
            },
        ),
        migrations.CreateModel(
            name='MRCP',
            fields=[
                ('M_check_id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False, verbose_name='检查号')),
                ('M_dzgkz', models.CharField(choices=[('yes', '有'), ('no', '无')], max_length=20, verbose_name='胆总管扩张')),
                ('M_dzgzj', models.FloatField(default=0, verbose_name='胆总管直径')),
                ('M_dzgjs1', models.CharField(choices=[('yes', '有'), ('no', '无')], max_length=20, verbose_name='胆总管结石')),
                ('M_dzgjs2', models.CharField(blank=True, choices=[('multi', '多发'), ('single', '单发')], max_length=20, verbose_name='')),
                ('M_gndgjs', models.CharField(choices=[('yes', '有'), ('no', '无')], max_length=20, verbose_name='肝内胆管结石')),
                ('M_qs', models.CharField(choices=[('yes', '有'), ('no', '无')], max_length=20, verbose_name='十二指肠乳头周围憩室')),
                ('M_xz', models.CharField(choices=[('yes', '有'), ('no', '无')], max_length=20, verbose_name='胆总管下端狭窄')),
                ('M_hlyc', models.CharField(choices=[('yes', '有'), ('no', '无')], max_length=20, verbose_name='胆胰管合流异常')),
                ('M_patient_id', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='Hospital.Patient', verbose_name='就诊号')),
            ],
            options={
                'verbose_name': 'MRCP',
                'verbose_name_plural': 'MRCP',
            },
        ),
        migrations.CreateModel(
            name='LAB',
            fields=[
                ('lab_check_id', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False, verbose_name='检查号')),
                ('lab_wbc', models.FloatField(default=0, verbose_name='WBC(10^9/L)')),
                ('lab_n', models.FloatField(default=0, verbose_name='N(%)')),
                ('lab_hgb', models.FloatField(default=0, verbose_name='HGB(g/L)')),
                ('lab_plt', models.FloatField(default=0, verbose_name='PLT(10^9/L)')),
                ('lab_tbil', models.FloatField(default=0, verbose_name='TBIL(mmol/L)')),
                ('lab_dbil', models.FloatField(default=0, verbose_name='DBIL(mmol/L)')),
                ('lab_alb', models.FloatField(default=0, verbose_name='ALB(g/L)')),
                ('lab_ast', models.FloatField(default=0, verbose_name='AST(U/L)')),
                ('lab_alt', models.FloatField(default=0, verbose_name='ALT(U/L)')),
                ('lab_alp', models.FloatField(default=0, verbose_name='ALP(U/L)')),
                ('lab_ggt', models.FloatField(default=0, verbose_name='GGT(U/L)')),
                ('lab_tg', models.FloatField(default=0, verbose_name='TG(mmol/L)')),
                ('lab_xamy', models.FloatField(default=0, verbose_name='血AMY(U/L)')),
                ('lab_namy', models.FloatField(default=0, verbose_name='尿AMY(U/L)')),
                ('lab_yjzb', models.FloatField(default=0, verbose_name='应急指标')),
                ('lab_patient_id', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='Hospital.Patient', verbose_name='就诊号')),
            ],
            options={
                'verbose_name': '实验室检查',
                'verbose_name_plural': '实验室检查',
            },
        ),
    ]
