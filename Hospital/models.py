from django.db import models
from django.core.exceptions import ValidationError
from django.db import connection
import datetime
# Create your models here.


class Patient(models.Model):
    class Meta:
        verbose_name = '患者信息'
        verbose_name_plural = '患者信息'

    SEX = (
        ('male', '男'),
        ('female', '女')
    )

    doctor = (
        ('zzh', '赵志宏'),
        ('cz', '陈震'),
        ('ln', '李宁')
    )

    select = (
        ('yes', '有'),
        ('no', '无')
    )

    select2 = (
        ('yes', '是'),
        ('no', '否')
    )

    patient_id = models.CharField(primary_key=True,verbose_name='就诊号', max_length=10)
    name = models.CharField(verbose_name='姓名', max_length=10)
    sex = models.CharField(choices=SEX, verbose_name='性别', max_length=10)
    age = models.IntegerField(verbose_name='年龄')
    hos_number = models.CharField(verbose_name='住院号', max_length=20)
    jizhang_number = models.CharField(verbose_name='记账号', max_length=20)
    doctor = models.CharField(choices=doctor, verbose_name='术者', max_length=20)
    inTime = models.DateField(
        verbose_name='入院时间')
    outTime = models.DateField(
        verbose_name='出院时间')
    jiguan = models.CharField(verbose_name='籍贯', max_length=20, default='天津')
    BMI = models.CharField(verbose_name='BMI', max_length=20, default='100')
    phone = models.CharField(verbose_name='联系电话', max_length=20, default='1')
    livePlace = models.CharField(
        verbose_name='居住地', max_length=100, default='天津')
    mail = models.CharField(verbose_name='邮箱', max_length=20, default='1')
    mailPlace = models.CharField(verbose_name='邮编', max_length=20, default='1')
    gaoxueya = models.CharField(
        choices=select, verbose_name='高血压', max_length=20)
    # 内科
    gxy_year = models.IntegerField(verbose_name='', default=0)
    guanxinbing = models.CharField(
        choices=select, verbose_name='冠心病', max_length=20)
    gxb_year = models.IntegerField(verbose_name='', default=0)
    gmzj = models.CharField(choices=select, verbose_name='冠脉支架', max_length=20)
    gmzj_year = models.IntegerField(verbose_name='', default=0)
    tnb = models.CharField(choices=select, verbose_name='糖尿病', max_length=20)
    tnb_year = models.IntegerField(verbose_name='', default=0)
    nk_other = models.TextField(verbose_name='其他', max_length=100)
    # 外科
    jxdyy = models.CharField(
        choices=select, verbose_name='急性胆源性胰腺炎', max_length=20)
    jxdyy_value = models.CharField(
        choices=(('low', '轻'), ('high', '重')), verbose_name='', max_length=20,blank=True)
    jxdgy = models.CharField(choices=(
        ('AC', 'AC'), ('AOC', 'AOC'), ('AOSC', 'AOSC')), verbose_name='急性胆管炎', max_length=20)
    jxdny = models.CharField(choices=(
        ('yes_jieshi', '有结石'), ('no_jieshi', '无结石')), verbose_name='急性胆囊炎', max_length=20)
    wk_other = models.TextField(verbose_name='其他', max_length=100)
    wk_sss = models.TextField(verbose_name='手术史', max_length=100)
    # 个人习惯
    smoke = models.CharField(choices=select2, verbose_name='抽烟', max_length=10)
    smoke_year = models.IntegerField(verbose_name='', default=0)
    drink = models.CharField(choices=select2, verbose_name='饮酒', max_length=10)
    drink_year = models.IntegerField(verbose_name='', default=0)
    breakfast = models.CharField(
        choices=select2, verbose_name='不吃早餐', max_length=10)
    breakfast_year = models.IntegerField(verbose_name='', default=0)
    likegzc = models.CharField(
        choices=select2, verbose_name='喜高脂餐', max_length=10)
    likegzc_year = models.IntegerField(verbose_name='', default=0)
    likess = models.CharField(
        choices=select2, verbose_name='喜素食', max_length=10)
    likess_year = models.IntegerField(verbose_name='', default=0)
    likexl = models.CharField(
        choices=select2, verbose_name='喜辛辣食物', max_length=10)
    likexl_year = models.IntegerField(verbose_name='', default=0)
    grxg_other = models.TextField(verbose_name='其他', max_length=100)
    # 相关家族史
    family_jieshi = models.CharField(choices=(
        ('dannang', '胆囊'), ('gannei', '肝内'), ('ganwai', '肝外')), verbose_name='结石', max_length=10)
    family_ddzl = models.CharField(
        choices=select, verbose_name='胆道肿瘤', max_length=20)
    family_tnb = models.CharField(
        choices=select, verbose_name='糖尿病', max_length=20)
    family_gxy = models.CharField(
        choices=select, verbose_name='高血压', max_length=20)
    family_gzxz = models.CharField(
        choices=select, verbose_name='高脂血症', max_length=20)
    # 术前诊断
    sq_dgy = models.CharField(
        choices=select, verbose_name='急性化脓性胆管炎', max_length=20)
    sq_yxy = models.CharField(
        choices=select, verbose_name='急性胆源性胰腺炎', max_length=20)
    sq_jsqd = models.CharField(
        choices=select, verbose_name='乳头部结石嵌顿', max_length=20)
    sq_hd = models.CharField(
        choices=select, verbose_name='梗阻性黄疸', max_length=20)
    sq_dzgkz = models.CharField(
        choices=select, verbose_name='胆总管扩张', max_length=20)
    sq_dzgjs = models.CharField(
        choices=select, verbose_name='胆总管结石', max_length=20)
    sq_dny = models.CharField(
        choices=select, verbose_name='急性胆囊炎', max_length=20)
    sq_dnjs = models.CharField(
        choices=select, verbose_name='胆囊结石', max_length=20)

    def __str__(self):
        return self.patient_id
# class Class(models.Model):
#     classid = models.CharField(verbose_name='班级名称', max_length=50)

#     class Meta:
#         verbose_name = '班级信息'
#         verbose_name_plural = '班级信息'

#     def get_number(self):
#         return len(Students.objects.filter(sclass__classid=self.classid))
#     get_number.short_description = '班级人数'

#     def get_classavg(self):
#         list_result = list(Students.objects.filter(sclass__classid=self.classid).values())
#         schoice = 0
#         if len(list_result) == 0:
#             return 0
#         for i in range(0, len(list_result)):
#             number = list_result[i]['snumber']
#             if Choices.objects.filter(snumber__snumber=number).exists():
#                 schoice += Choices.objects.filter(snumber__snumber=number).aggregate(mygrade=Avg('grade'))['mygrade']
#             else:
#                 schoice += 0
#         return round(schoice / len(list_result), 1)
#     get_classavg.short_description = '平均成绩'

#     def __str__(self):
#         return self.classid

# class Subjects(models.Model):
#     subid = models.CharField(primary_key=True, verbose_name='课程编号', max_length=50)
#     name = models.CharField(verbose_name='课程名称', max_length=50)
#     tname = models.CharField(verbose_name='教师姓名', max_length=10)
#     score = models.IntegerField(verbose_name='学分')
#     suitableage = models.IntegerField(verbose_name='适合年级')
#     deleteyear = models.IntegerField(verbose_name='取消年份', blank=True, null=True)

#     class Meta:
#         verbose_name = '课程信息'
#         verbose_name_plural = '课程信息'

#     def clean(self):
#         if len(self.subid) != 7:
#             raise ValidationError("课程编号为7位，请重新输入！")

#     def get_avg(self):
#         if Choices.objects.filter(subid=self.subid).exists():
#             return round(Choices.objects.filter(subid=self.subid).aggregate(Avg('grade'))['grade__avg'], 1)
#         else:
#             return 0
#     get_avg.short_description = '平均成绩'

#     def get_50(self):
#         return len(Choices.objects.filter(subid=self.subid, grade__lt=60))

#     def get_60(self):
#         return len(Choices.objects.filter(subid=self.subid, grade__lt=70, grade__gte=60))

#     def get_70(self):
#         return len(Choices.objects.filter(subid=self.subid, grade__lt=80, grade__gte=70))

#     def get_80(self):
#         return len(Choices.objects.filter(subid=self.subid, grade__lt=90, grade__gte=80))

#     def get_90(self):
#         return len(Choices.objects.filter(subid=self.subid, grade__lt=100, grade__gte=90))

#     def get_100(self):
#         return len(Choices.objects.filter(subid=self.subid, grade=100))

#     def __str__(self):
#         return self.subid

# class Students(models.Model):
#     SEX = (
#         ('male', '男'),
#         ('female', '女')
#     )
#     snumber = models.CharField(primary_key=True, verbose_name='学号', max_length=50)
#     name = models.CharField(verbose_name='学生姓名', max_length=50, null=False)
#     sex = models.CharField(choices=SEX, verbose_name='性别', max_length=50)
#     inage = models.IntegerField(verbose_name='入学年龄')
#     inyear = models.IntegerField(verbose_name='入学年份')
#     sclass = models.ForeignKey('Class', verbose_name='班级', on_delete=models.CASCADE)


#     class Meta:
#         verbose_name = '学生信息'  # 这个是修改增加xx 按钮名字
#         verbose_name_plural = '学生信息'  # 这个是修改显示Studentss文字

#     def clean(self):
#         if len(self.snumber) != 10:
#             raise ValidationError("学号为10位，请重新输入！")

#         if not 10 <= self.inage <= 50:
#             raise ValidationError("年龄在10到50之间，请重新输入！")


#     def get_avg(self):
#         if Choices.objects.filter(snumber=self.snumber).exists():
#             return round(Choices.objects.filter(snumber=self.snumber).aggregate(Avg('grade'))['grade__avg'], 1)
#         else:
#             return 0
#     get_avg.short_description = '平均成绩'

#     def __str__(self):
#         return self.snumber

# class Choices(models.Model):
#     snumber = models.ForeignKey('Students', verbose_name='学生学号', on_delete=models.CASCADE, blank=True, null=True)
#     subid = models.ForeignKey('Subjects', verbose_name='课程号', on_delete=models.CASCADE, blank=True, null=True)
#     year = models.IntegerField(verbose_name='选课年份', blank=True)
#     grade = models.IntegerField(verbose_name='成绩', blank=True)

#     def clean(self):
#         if self.year > Subjects.objects.get(subid=self.subid).deleteyear:
#             raise ValidationError('选课年份超过课程取消年份，请重新输入！')

#         if Students.objects.get(snumber=self.snumber).inyear > Subjects.objects.get(subid=self.subid).suitableage:
#             raise ValidationError('学生年级不到课程适合年级，请重新输入！')

#     class Meta:
#         verbose_name = '选课信息'
#         verbose_name_plural = '选课信息'
#         unique_together = ('snumber', 'subid')

#     def __str__(self):
#         return "%s, %s" % (self.snumber, self.subid)
