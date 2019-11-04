import xadmin
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Container, PrependedText
from xadmin.views import CommAdminView
import xadmin.views as xviews
from Hospital.models import *
from After_op.models import *
from Before_op.models import *
from EUS.models import *
from ERCP.models import *
from LCBDE.models import *
from SuiFang.models import *
# Register your models here.


class PatientAdmin(object):
    list_display = ('patient_id','name', 'sex', 'age', 'hos_number')
    list_per_page = 10
    search_fields = ('name', 'patient_id')
    form_layout = (
        Fieldset('患者一般情况',
                'patient_id',
                 Row('name', 'sex', 'age', ),
                 Row('hos_number', 'jizhang_number', 'doctor'),
                 Row('jiguan', 'BMI', 'phone'),
                 Row('livePlace', 'mail', 'mailPlace'),
                 Row('inTime', 'outTime',),
                 Fieldset('术前合并症',
                          Fieldset('内科',
                                   Row('gaoxueya', AppendedText(
                                       'gxy_year', '年')),
                                   Row('guanxinbing', AppendedText(
                                       'gxb_year', '年')),
                                   Row('gmzj', AppendedText('gmzj_year', '个')),
                                   Row('tnb', AppendedText('tnb_year', '年')),
                                   'nk_other'
                                   ),
                          Fieldset('外科',
                                   Row('jxdyy', 'jxdyy_value'),
                                   'jxdgy', 'jxdny', 'wk_other', 'wk_sss'
                                   ),
                          ),
                 Fieldset('个人习惯',
                          Row('smoke', AppendedText('smoke_year', '年')),
                          Row('drink', AppendedText('drink_year', '年')),
                          Row('breakfast', AppendedText('breakfast_year', '年')),
                          Row('likegzc', AppendedText('likegzc_year', '年')),
                          Row('likess', AppendedText('likess_year', '年')),
                          Row('likexl', AppendedText('likexl_year', '年')),
                          'grxg_other'
                          ),
                 Fieldset('相关家族史', 'family_jieshi', 'family_ddzl',
                          'family_tnb', 'family_gxy', 'family_gzxz'),
                 Fieldset('术前诊断', 'sq_dgy', 'sq_yxy', 'sq_jsqd',
                          'sq_hd', 'sq_dzgkz', 'sq_dzgjs', 'sq_dny', 'sq_dnjs')
                 ),
    )


xadmin.site.register(Patient, PatientAdmin)


class AfterOperateAdmin(object):
    list_per_page = 10
    list_display = ('after_patient_id','get_name',)
    form_layout = (
        'after_patient_id',
        Row('after_ft', 'after_fz', 'after_fr'),
        Row('after_ot', 'after_dl', 'after_cx',
            AppendedText('after_cx_number', 'ml')),
        Row('after_yxy', 'after_cs', 'after_other'),
        Row('after_pain', 'after_satisfy'),
        Row('after_out_date', AppendedText('after_out_day', '天'), AppendedText('after_out_cost','元'))
    )


xadmin.site.register(AfterOperate, AfterOperateAdmin)


class TUSAdmin(object):
    list_per_page = 10
    list_display = ('B_patient_id','get_name',)
    form_layout = ('B_patient_id','B_check_id',
                   Row(AppendedText('B_dnsize1', 'mm X'),
                       AppendedText('B_dnsize2', 'mm')),
                   Row(AppendedText('B_dnbhd', 'mm'), AppendedText(
                       'B_dnjsnum', '枚'), AppendedText('B_dnjszj', 'mm')),
                   Row(AppendedText('B_dzgzj', 'mm'), AppendedText(
                       'B_dzgjsnum', '枚'), AppendedText('B_dzgjszj', 'mm'))
                   )


xadmin.site.register(TUS, TUSAdmin)


class MRCPAdmin(object):
    list_per_page = 10
    list_display = ('M_patient_id','get_name',)
    form_layout = (
        'M_patient_id','M_check_id',
        Row('M_dzgkz', AppendedText('M_dzgzj', 'mm')),
        Row('M_dzgjs1', 'M_dzgjs2'),
        Row('M_gndgjs', 'M_qs'),
        Row('M_xz', 'M_hlyc')
    )


xadmin.site.register(MRCP, MRCPAdmin)


class LABAdmin(object):
    list_per_page = 10
    list_display = ('lab_patient_id','get_name',)
    form_layout = (
        'lab_patient_id','lab_check_id',
        Row('lab_wbc', 'lab_n', 'lab_hgb'),
        Row('lab_plt', 'lab_tbil', 'lab_dbil'),
        Row('lab_alb', 'lab_ast', 'lab_alt'),
        Row('lab_alp', 'lab_ggt', 'lab_tg'),
        Row('lab_xamy', 'lab_namy', 'lab_yjzb')
    )


xadmin.site.register(LAB, LABAdmin)


class EUSAdmin(object):
    list_per_page = 10
    list_display = ('eus_patient_id','get_name',)
    form_layout = (
        'eus_patient_id','eus_check_id',
        Row(AppendedText('eus_day', '天'), 'eus_way'),
        Row(AppendedText('eus_dzgzj', 'mm'),
            AppendedText('eus_ygzj', 'mm'), 'eus_blgb')
    )


xadmin.site.register(EUS, EUSAdmin)


class ERCPAdmin(object):
    list_per_page = 10
    list_display = ('ercp_patient_id','get_name',)
    form_layout = (

        'ercp_patient_id','ercp_check_id',
        AppendedText('ercp_day', '天'),
        
        Fieldset('十二指肠镜下',
                 Row('ercp_rtlx', 'ercp_kkxz', 'ercp_kkdx', 'ercp_dzpc'),
                 Row('ercp_dzxz', 'ercp_zwqs1', 'ercp_zwqs2')),
        Row('ercp_qsdx', 'ercp_qswz', 'ercp_rtqs'),
        Row('ercp_chaguan', 'ercp_cgny', 'ercp_est'),
        Row('ercp_erbd', AppendedText('ercp_erbd_diameter',
                                      'Fr'), 'ercp_enbd', AppendedText('ercp_enbd_diameter', 'Fr')),
        Row('ercp_diagnose', 'ercp_date', 'ercp_video'),
        Row(AppendedText('ercp_time_hour', 'H'), AppendedText(
            'ercp_time_min', 'M')),
        Row('ercp_other')
        
    )


xadmin.site.register(ERCP, ERCPAdmin)


class LCBDEAdmin(object):
    list_per_page = 10
    list_display = ('lcbde_patient_id','get_name',)
    form_layout = (
        'lcbde_patient_id','lcbde_check_id',
        Row('lcbde_date', 'lcbde_time', 'lcbde_dnyz', 'lcbde_size'),
        Row(AppendedText('lcbde_dngzj', 'mm'),
            AppendedText('lcbde_dzgzj', 'mm'), 'lcbde_qc'),
        'lcbde_ddj',
        Row('lcbde_jdng', 'lcbde_jdng_qs', AppendedText('lcbde_jdng_number',
                                                        '枚'), AppendedText('lcbde_jdng_zdzj', 'mm'), 'lcbde_jdng_way'),
        Row('lcbde_jdzg', 'lcbde_jdzg_qs', AppendedText('lcbde_jdzg_number',
                                                        '枚'), AppendedText('lcbde_jdzg_zdzj', 'mm'), 'lcbde_jdzg_way'),
        Row('lcbde_ddzy', 'lcbde_fzzj', 'lcbde_fzzj_way', 'lcbde_fzzj_number'),
        Row('lcbde_tlsj', 'lcbde_zjbfz'),
        Row('lcbde_fhway', 'lcbde_fxway', 'lcbde_fxtype', 'lcbde_cx'),
        Row('lcbde_fqyl', 'lcbde_ylglx', 'lcbde_zzkf', 'lcbde_sslx'),
        'lcbde_other'
    )


xadmin.site.register(LCBDE, LCBDEAdmin)


class SuiFangAdmin(object):
    list_per_page = 10
    list_display = ('suifang_patient_id','get_name',)
    form_layout = (
        Fieldset('',
	'suifang_patient_id',
        AppendedText('suifang_day', '月'),
        Row('suifang_ft', 'suifang_fz', 'suifang_fr'),
        Row('suifang_ot', 'suifang_hy', 'suifang_dgy'),
        Row('suifang_cyjs', 'suifang_yxy', 'suifang_dgxz'),
        Row('suifang_ffjs', 'suifang_dgzw', 'suifang_jz'),
        'suifang_hos',
        Fieldset('TUS',
                 AppendedText('suifang_tus_dzgzj', 'mm'),
                 AppendedText('suifang_tus_jszj', 'mm'),
                 AppendedText('suifang_tus_zdzj', 'mm'),
                 AppendedText('suifang_tus_jssm', '枚')
                 ),
        Fieldset('肝功能',
                 Row('suifang_tbil', 'suifang_dbil'),
                 Row('suifang_alb', 'suifang_ast', 'suifang_alt'),
                 Row('suifang_alp', 'suifang_ggt')
                 ),
        'suifang_mrcp')
    )


xadmin.site.register(SuiFang, SuiFangAdmin)

# class StudentsAdmin():
#     list_display = ('snumber', 'name', 'sex', 'inage', 'inyear', 'sclass', 'get_avg')
#     style_fields = {'subjects': 'checkbox-inline', }
#     search_fields = ('name', 'snumber')
#     #readonly_fields = ['snumber',]
#     #过滤
#     list_filter = ('sex', 'sclass')
#     #list_editable = ['name', 'sex', 'inage', 'inyear', 'sclass',]

# class ClassAdmin(object):
#     list_display = ('classid', 'get_number', 'get_classavg')

# xadmin.site.register(Students, StudentsAdmin)
# xadmin.site.register(Class, ClassAdmin)

# class SubjectsAdmin(object):
#     list_display = ('subid', 'name', 'tname', 'score', 'suitableage', 'deleteyear', 'get_avg')
#     data_charts = {
#          "avg": {'title': '课程分数统计',
#                  "x-field": "name",
#                  "y-field": ("get_50", "get_60", "get_70", "get_80", "get_90", "get_100"),
#                  'option': {
#                      "xaxis": {"aggregate": "name", "mode": "categories"}
#                  },
#                  }
#     }
#     readonly_fields = ['subid',]
# xadmin.site.register(Subjects, SubjectsAdmin)

# class ChoicesAdmin(object):
#     list_display = ('snumber', 'subid', 'year', 'grade')

#     search_fields = ('subid__subid', 'snumber__snumber')
#     list_filter = ('year',)
#     readonly_fields = ['snumber', 'subid',]
# xadmin.site.register(Choices, ChoicesAdmin)


class GlobalSetting(CommAdminView):
    # 左上角及浏览器标题
    site_title = '医疗信息管理系统'
    # 页脚版权信息
    site_footer = 'Copyright © 2019 南开医院'
    menu_style = 'accordion'

    def get_site_menu(self):
        return (
            {'title': '患者信息', 'url': self.get_model_url(
                Patient, 'changelist')},
            {'title': '术前检查', 'menus': (

                {'title': 'TUS', 'url': self.get_model_url(
                    TUS, 'changelist')},
                {'title': 'MRCP', 'url': self.get_model_url(
                    MRCP, 'changelist')},

                {'title': '实验室检查', 'url': self.get_model_url(
                    LAB, 'changelist')},
            )},
            {'title': '手术情况', 'menus': (
                {'title': 'EUS', 'url': self.get_model_url(EUS, 'changelist')},
                {'title': 'ERCP', 'url': self.get_model_url(
                    ERCP, 'changelist')},
                {'title': 'LCBDE', 'url': self.get_model_url(
                    LCBDE, 'changelist')}
            )},
            {'title': '术后并发症', 'url': self.get_model_url(
                AfterOperate, 'changelist')},
            {'title': '随访', 'url': self.get_model_url(
                SuiFang, 'changelist')}
        )


class BaseSetting(object):
    enable_themes = True  # 使用主题
    use_bootswatch = True


xadmin.site.register(xviews.BaseAdminView, BaseSetting)
xadmin.site.register(CommAdminView, GlobalSetting)
