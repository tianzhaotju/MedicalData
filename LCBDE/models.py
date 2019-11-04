from django.db import models
from Hospital.models import Patient
import datetime

class LCBDE(models.Model):
    class Meta:
        verbose_name = 'LCBDE'
        verbose_name_plural = 'LCBDE'

    select = (
        ('yes','是'),
        ('no','否')
    )

    lcbde_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE)
    lcbde_check_id = models.CharField(primary_key=True, verbose_name='检查号', max_length=10, blank=True)
    lcbde_date = models.DateField(verbose_name='手术日期')
    lcbde_time = models.FloatField(verbose_name='手术时间',default=0)
    lcbde_dnyz = models.CharField(verbose_name='胆囊炎症',choices=(('small','轻'),('big','重')),max_length=10)
    lcbde_size = models.CharField(verbose_name='胆囊大小',choices=(('normal','正常'),('big','增大'),('small','萎缩')),max_length=10)
    lcbde_dngzj = models.FloatField(verbose_name='胆囊管直径',default=0)
    lcbde_dzgzj = models.FloatField(verbose_name='胆总管直径',default=0)
    lcbde_qc = models.CharField(verbose_name='胆囊切除',choices=select,max_length=10)
    
    lcbde_ddj = models.CharField(verbose_name='术中胆道镜',choices=select,max_length=10)
    lcbde_jdng = models.CharField(verbose_name='经胆囊管',choices=select,blank=True,max_length=10)
    lcbde_jdng_qs = models.CharField(verbose_name='取石',choices=select,blank=True,max_length=10)
    lcbde_jdng_number = models.IntegerField(verbose_name='胆管结石',default=0)
    lcbde_jdng_zdzj = models.FloatField(verbose_name='最大直径',default=0)
    lcbde_jdng_way = models.CharField(verbose_name='',choices=(('jf','继发'),('yf','原发')),blank=True,max_length=10)
    
    lcbde_jdzg = models.CharField(verbose_name='经胆总管',choices=select,blank=True,max_length=10)
    lcbde_jdzg_qs = models.CharField(verbose_name='取石',choices=select,blank=True,max_length=10)
    lcbde_jdzg_number = models.IntegerField(verbose_name='胆管结石',default=0)
    lcbde_jdzg_zdzj = models.FloatField(verbose_name='最大直径',default=0)
    lcbde_jdzg_way = models.CharField(verbose_name='',choices=(('jf','继发'),('yf','原发')),blank=True,max_length=10)

    lcbde_ddzy = models.CharField(verbose_name='术中胆道造影',choices=select,max_length=10)
    lcbde_fzzj = models.CharField(verbose_name='顺行放置支架',choices=select,max_length=10)
    lcbde_fzzj_way = models.CharField(verbose_name='',choices=(('dzw','单猪尾(胰管型)'),('zg','直管(胆管型)')),max_length=20)
    lcbde_fzzj_number = models.FloatField(verbose_name='',default=0)
    lcbde_tlsj = models.IntegerField(verbose_name='支架脱落时间',default=0)
    lcbde_zjbfz = models.CharField(verbose_name='支架并发症',choices=(('yes','是'),('no','否')),max_length=10)
    lcbde_fhway = models.CharField(verbose_name='缝合方式',choices=(('jd','间断'),('lx','连续')),max_length=10)
    lcbde_fxway = models.CharField(verbose_name='缝线类型',choices=(('dq','单桥'),('pds','PDS-II')),max_length=10)
    lcbde_fxtype = models.CharField(verbose_name='缝线型号',choices=(('3-0','3-0'),('4-0','4-0'),('5-0','5-0')),max_length=10)
    lcbde_cx = models.FloatField(verbose_name='术中出血',default=0)
    lcbde_fqyl = models.CharField(verbose_name='腹腔引流',choices=(('0','无'),('1','1根'),('2','2根')),max_length=10)
    lcbde_ylglx = models.CharField(verbose_name='引流管类型',choices=(('0','S6'),('1','M6'),('2','乳胶管'),('3','硅胶管')),max_length=10)
    lcbde_zzkf = models.CharField(verbose_name='中转开腹',choices=select,max_length=10)
    lcbde_sslx = models.CharField(verbose_name='手术录像',choices=(('yes','是'),('no','否')),max_length=10)
    lcbde_other = models.TextField(verbose_name='其他',blank=True)

    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.lcbde_patient_id).values())[0]['name']
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.lcbde_patient_id).values())[0]['name']
