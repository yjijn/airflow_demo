import os
from datetime import datetime

# 产生时间标记（dag用）
def gen_json_time():
    return datetime.now().strftime('%Y%m%d%H%M%S')


# 删除临时文件通用方法
def rm_temp_file(file_list, json_time):
    '''
    删除dag过程中的临时文件
    :param file_list:  file name list
    :param json_time:  文件后缀标记
    :return: None
    '''
    for name in file_list:
        if os.path.exists(name + json_time + '.json'):
            os.remove(name + json_time + '.json')
            print('DELETE TEMP FILE：%s' % name + json_time + '.json')
        if os.path.exists(name + json_time + '.csv'):
            os.remove(name + json_time + '.csv')
            print('DELETE TEMP FILE：%s' % name + json_time + '.csv')
        if os.path.exists(name + json_time + '.xlsx'):
            os.remove(name + json_time + '.xlsx')
            print('DELETE TEMP FILE：%s' % name + json_time + '.xlsx')
