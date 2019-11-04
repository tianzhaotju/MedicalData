from django.db import models
from Hospital.models import Patient
import datetime

class ERCP(models.Model):
    class Meta:
        verbose_name = 'ERCP'
        verbose_name_plural = 'ERCP'

    select = (
        ('yes', '有'),
        ('no', '无')
    )

    select2 = (
        ('yes', '是'),
        ('no', '否')
    )

    ercp_patient_id = models.ForeignKey(Patient, verbose_name='就诊号', on_delete=models.CASCADE)
    ercp_check_id = models.CharField(primary_key=True, verbose_name='检查号', max_length=10, blank=True)
    ercp_day = models.IntegerField(verbose_name='术前', default=0)
    ercp_rtlx = models.CharField(verbose_name='乳头类型', choices=(('xbq', '小半球'),('dbq','大半球'),('bp','扁平'),('rtx','乳头型'),('spgx','沙皮狗型')), max_length=20)
    ercp_kkxz = models.CharField(verbose_name='乳头开口形状', choices=(('hb','花瓣'),('kl','颗粒'),('lx','裂隙'),('dz','点状')),max_length=10)
    ercp_kkdx = models.CharField(verbose_name='乳头开口大小',choices=(('small','< 4mm'),('big', '>= 4mm')), max_length=10)
    ercp_dzpc = models.CharField(verbose_name='胆汁自行排出情况',choices=select, max_length=10)
    ercp_dzxz = models.CharField(verbose_name='胆汁形状',choices=(('ql','清亮'),('hz','浑浊'),('yj','淤积'),('gr','感染')),max_length=20)
    ercp_zwqs1 = models.CharField(verbose_name='乳头周围憩室',choices=select, max_length=10)
    ercp_zwqs2 = models.CharField(verbose_name='',choices=(('multi','多发'),('single','单发')), max_length=10,blank=True)
    ercp_qsdx = models.CharField(verbose_name='估计憩室大小',choices=(('1','1cm'),('2','2cm'),('3','3cm'),('4','4cm')),max_length=10)
    ercp_qswz = models.CharField(verbose_name='憩室位置(解剖位)',choices=(('left','乳头在憩室左侧'),('right','乳头在憩室右侧'),('middle','乳头在憩室中央')),max_length=30)
    ercp_rtqs = models.CharField(verbose_name='乳头与憩室间关系',choices=(('1','乳头开口在憩室外、根部在憩室外'),('2','乳头开口在憩室外、根部在憩室内'),('3','乳头开口在憩室外、根部沿憩室边缘'),('4','乳头开口及根部均在憩室内')),max_length=20)
    ercp_chaguan = models.CharField(verbose_name='插管',choices=select2,max_length=10)
    ercp_cgny = models.CharField(verbose_name='插管难易程度',choices=(('difficult','困难'),('normal','一般'),('easy','容易')),max_length=10)
    ercp_est = models.CharField(verbose_name='EST',choices=(('small','小切开(仅切开开口)'),('middle','中切开(切断部分Oddi括约肌)'),('big','大切开(切断Oddi括约肌)'),('other','柱状气囊扩张')),max_length=30)
    ercp_erbd = models.CharField(verbose_name='ERBD',choices=(('dzw','单猪尾(胰管支架)'),('zg','直管')),max_length=20)
    ercp_erbd_diameter = models.FloatField(verbose_name='直径',default=0)
    ercp_enbd = models.CharField(verbose_name='ENBD',choices=(('zw','猪尾型'),('gn','肝内型管')),max_length=20)
    ercp_enbd_diameter = models.FloatField(verbose_name='直径',default=0)
    ercp_diagnose = models.CharField(verbose_name='ERCP诊断',choices=(('multi','胆总管多发结石'),('single','胆总管单发结石'),('kz','胆总管扩张、胆汁淤积'),('ch','十二指肠乳头炎、排空迟缓'),('xz','缩窄性乳头炎')),max_length=30)
    ercp_date = models.DateField(verbose_name='内镜时间')
    ercp_time_hour = models.IntegerField(verbose_name='操作时间',default=0)
    ercp_time_min = models.IntegerField(verbose_name='',default=0)
    ercp_video = models.CharField(verbose_name='录像',choices=select,max_length=10)
    ercp_other = models.TextField(verbose_name='其他备注',blank=True)

    def get_name(self):
        name = list(Patient.objects.filter(patient_id=self.ercp_patient_id).values())[0]['name']
        return name
    get_name.short_description = '姓名'

    def __str__(self):
        return list(Patient.objects.filter(patient_id=self.ercp_patient_id).values())[0]['name']
