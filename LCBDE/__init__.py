from django.apps import AppConfig
import os
 
default_app_config = 'LCBDE.LCBDEConfig'
 
# 获取apps所在文件夹名字，如果文件夹名字修改，这里可以动态调整
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]
 
class LCBDEConfig(AppConfig):
    # 这里apps所在文件夹名字直接固定，如果更改则也需要调整
    name = get_current_app_name(__file__) 
    verbose_name = 'LCBDE'