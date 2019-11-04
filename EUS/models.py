from django.db import models
from Hospital.models import Patient

class EUS(models.Model):
    class Meta:
        verbose_name = 'EUS'
        verbose_name_plural = 'EUS'
    eus_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE,default='0')
    eus_check_id = models.CharField(primary_key=True,verbose_name='检查号', max_length=10,blank=True)
    eus_day = models.IntegerField(verbose_name='术前(天)', default=0)
    eus_way = models.CharField(
        choices=(('hs', '环扫'), ('ss', '扇扫')), verbose_name='方式', max_length=10)
    eus_dzgzj = models.IntegerField(verbose_name='胆总管直径', default=0)
    eus_ygzj = models.IntegerField(verbose_name='胰管直径', default=0)
    eus_blgb = models.CharField(max_length=30, verbose_name='病理改变', choices=(('dzgjs', '胆总管结石'), (
        'dzgkz', '胆总管扩张'), ('dnjs', '胆囊结石'), ('dngjs', '胆囊管结石'), ('hlxz', '胆管远端合流部狭窄'), ('zwzs', '胆总管占位梗阻')))

    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.eus_patient_id).values())[0]['name']
        # name = Patient.objects.filter(self.after_patient_id=patient_id)
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.eus_patient_id).values())[0]['name']