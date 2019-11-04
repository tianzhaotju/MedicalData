from django.db import models
from Hospital.models import Patient

class TUS(models.Model):
    class Meta:
        verbose_name = 'TUS'
        verbose_name_plural = 'TUS'

    '''影像学检查'''
    # B超
    B_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE)
    B_check_id = models.CharField(primary_key=True, verbose_name='检查号', max_length=10, blank=True)
    B_dnsize1 = models.FloatField(verbose_name='胆囊大小', default=0)
    B_dnsize2 = models.FloatField(verbose_name='', default=0)
    B_dnbhd = models.FloatField(verbose_name='胆囊壁厚度', default=0)
    B_dnjsnum = models.IntegerField(verbose_name='胆囊结石数目', default=0)
    B_dnjszj = models.FloatField(verbose_name='胆囊结石最大直径', default=0)
    B_dzgzj = models.FloatField(verbose_name='胆总管最大直径', default=0)
    B_dzgjsnum = models.IntegerField(verbose_name='胆管结石数目', default=0)
    B_dzgjszj = models.FloatField(verbose_name='胆管结石最大直径', default=0)

    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.B_patient_id).values())[0]['name']
        # name = Patient.objects.filter(self.after_patient_id=patient_id)
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.B_patient_id).values())[0]['name']

class MRCP(models.Model):
    select = (
        ('yes', '有'),
        ('no', '无')
    )

    class Meta:
        verbose_name = 'MRCP'
        verbose_name_plural = 'MRCP'
    # MRCP
    M_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE,default='0')
    M_check_id = models.CharField(primary_key=True,verbose_name='检查号', max_length=10,blank=True)
    M_dzgkz = models.CharField(
        choices=select, verbose_name='胆总管扩张', max_length=20)
    M_dzgzj = models.FloatField(verbose_name='胆总管直径', default=0)
    M_dzgjs1 = models.CharField(
        choices=select, verbose_name='胆总管结石', max_length=20)
    M_dzgjs2 = models.CharField(choices=(
        ('multi', '多发'), ('single', '单发')), verbose_name='', max_length=20, blank=True)
    M_gndgjs = models.CharField(
        choices=select, verbose_name='肝内胆管结石', max_length=20)
    M_qs = models.CharField(
        choices=select, verbose_name='十二指肠乳头周围憩室', max_length=20)
    M_xz = models.CharField(
        choices=select, verbose_name='胆总管下端狭窄', max_length=20)
    M_hlyc = models.CharField(
        choices=select, verbose_name='胆胰管合流异常', max_length=20)

    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.M_patient_id).values())[0]['name']
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.M_patient_id).values())[0]['name']
        

class LAB(models.Model):
    class Meta:
        verbose_name = '实验室检查'
        verbose_name_plural = '实验室检查'
    '''实验室检查'''
    lab_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE,default='0')
    lab_check_id = models.CharField(primary_key=True,verbose_name='检查号', max_length=10,blank=True)
    lab_wbc = models.FloatField(verbose_name='WBC(10^9/L)', default=0)
    lab_n = models.FloatField(verbose_name='N(%)', default=0)
    lab_hgb = models.FloatField(verbose_name='HGB(g/L)', default=0)
    lab_plt = models.FloatField(verbose_name='PLT(10^9/L)', default=0)
    lab_tbil = models.FloatField(verbose_name='TBIL(mmol/L)', default=0)
    lab_dbil = models.FloatField(verbose_name='DBIL(mmol/L)', default=0)
    lab_alb = models.FloatField(verbose_name='ALB(g/L)', default=0)
    lab_ast = models.FloatField(verbose_name='AST(U/L)', default=0)
    lab_alt = models.FloatField(verbose_name='ALT(U/L)', default=0)
    lab_alp = models.FloatField(verbose_name='ALP(U/L)', default=0)
    lab_ggt = models.FloatField(verbose_name='GGT(U/L)', default=0)
    lab_tg = models.FloatField(verbose_name='TG(mmol/L)', default=0)
    lab_xamy = models.FloatField(verbose_name='血AMY(U/L)', default=0)
    lab_namy = models.FloatField(verbose_name='尿AMY(U/L)', default=0)
    lab_yjzb = models.FloatField(verbose_name='应急指标', default=0)
    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.lab_patient_id).values())[0]['name']
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.lab_patient_id).values())[0]['name']
