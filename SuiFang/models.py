from django.db import models
from Hospital.models import Patient

class SuiFang(models.Model):
    class Meta:
        verbose_name = '随访'
        verbose_name_plural = '随访'

    select = (
        ('yes', '是'),
        ('no', '否')
    )

    suifang_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE)
    suifang_day = models.IntegerField(verbose_name='术后',default=1)
    suifang_ft = models.CharField(verbose_name='腹痛',choices=select,max_length=10,blank=True,default='yes')
    suifang_fz = models.CharField(verbose_name='腹胀',choices=select,max_length=10,blank=True,default='yes')
    suifang_fr = models.CharField(verbose_name='发热',choices=select,max_length=10,blank=True,default='yes')
    suifang_ot = models.CharField(verbose_name='呕吐',choices=select,max_length=10,blank=True,default='yes')
    suifang_hy = models.CharField(verbose_name='黄疸',choices=select,max_length=10,blank=True,default='yes')
    suifang_dgy = models.CharField(verbose_name='急性胆管炎',choices=select,max_length=10,blank=True,default='yes')
    suifang_cyjs = models.CharField(verbose_name='胆管残余结石',choices=select,max_length=10,blank=True,default='yes')
    suifang_yxy = models.CharField(verbose_name='急性胰腺炎',choices=select,max_length=10,blank=True,default='yes')
    suifang_dgxz = models.CharField(verbose_name='胆管狭窄',choices=select,max_length=10,blank=True,default='yes')
    suifang_jz = models.CharField(verbose_name='是否就诊',choices=select,max_length=10,blank=True,default='yes')
    suifang_ffjs = models.CharField(verbose_name='复发结石',choices=select,max_length=10,blank=True,default='yes')
    suifang_dgzw = models.CharField(verbose_name='胆管占位',choices=select,max_length=10,blank=True,default='yes')
    suifang_hos = models.CharField(verbose_name='就诊医院',max_length=20,blank=True)
    suifang_tus_dzgzj = models.FloatField(verbose_name='胆总管最大直径',default=0)
    suifang_tus_jszj = models.FloatField(verbose_name='残余结石直径',default=0)
    suifang_tus_zdzj = models.FloatField(verbose_name='结石最大直径',default=0)
    suifang_tus_jssm = models.IntegerField(verbose_name='复发结石数目',default=0)
    suifang_tbil = models.FloatField(verbose_name='TBIL(mmol/L)', default=0)
    suifang_dbil = models.FloatField(verbose_name='DBIL(mmol/L)', default=0)
    suifang_alb = models.FloatField(verbose_name='ALB(g/L)', default=0)
    suifang_ast = models.FloatField(verbose_name='AST(U/L)', default=0)
    suifang_alt = models.FloatField(verbose_name='ALT(U/L)', default=0)
    suifang_alp = models.FloatField(verbose_name='ALP(U/L)', default=0)
    suifang_ggt = models.FloatField(verbose_name='GGT(U/L)', default=0)
    suifang_mrcp = models.CharField(verbose_name='MRCP',blank=True, max_length=50)

    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.suifang_patient_id).values())[0]['name']
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.suifang_patient_id).values())[0]['name']
