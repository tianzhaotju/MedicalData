from django.db import models
import datetime
from Hospital.models import Patient

class AfterOperate(models.Model):   
    class Meta:
        verbose_name = '术后并发症'
        verbose_name_plural = '术后并发症'
    
    select = (
        ('yes', '是'),
        ('no', '否')
    )

    pain = (
        ('0', '0: 无痛'),
        ('1', '1~3: 轻度疼痛'),
        ('2', '4~6: 中度疼痛'),
        ('3', '7~10: 重度疼痛')
    )

    satisfy = (
        ('0', '0: 不满意'),
        ('1', '1~3: 一般'),
        ('2', '4~6: 满意'),
        ('3', '7~10: 非常满意')
    )

    after_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE,default='0')
    after_ft = models.CharField(verbose_name='腹痛',choices=select,max_length=10,default='yes')
    after_fz = models.CharField(verbose_name='腹胀',choices=select,max_length=10,default='yes')
    after_fr = models.CharField(verbose_name='发热',choices=select,max_length=10,default='yes')
    after_ot = models.CharField(verbose_name='呕吐',choices=select,max_length=10,default='yes')
    after_dl = models.CharField(verbose_name='胆漏',choices=select,max_length=10,default='yes')
    after_cx = models.CharField(verbose_name='术后出血',choices=select,max_length=10,default='yes')
    after_cx_number = models.FloatField(verbose_name='', default=0)
    after_yxy = models.CharField(verbose_name='胰腺炎',choices=select,max_length=10,default='yes')
    after_cs = models.CharField(verbose_name='残石',choices=select,max_length=10,default='yes')
    after_other = models.CharField(verbose_name='其他病发症',blank=True,max_length=100)
    after_pain = models.CharField(verbose_name='疼痛评分',choices=pain,max_length=20)
    after_satisfy = models.CharField(verbose_name='满意度评分',choices=satisfy,max_length=20)
    after_out_date = models.DateField(verbose_name='出院日期')
    after_out_day = models.IntegerField(verbose_name='住院天数',default=0)
    after_out_cost = models.FloatField(verbose_name='住院费用',default=0)

    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.after_patient_id).values())[0]['name']
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.after_patient_id).values())[0]['name']
        
