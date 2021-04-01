import os, shutil
from datetime import datetime, timedelta

from config import PROJECT_ROUTE

def clear_log_file(retentionDays=30):
    '''

    :param retentionDays:  系统日志保留天数
    :return:
    '''
    def _get_airflow_log(log_path):  # 遍历获取所有日志文件
        for root, dirs, files in os.walk(log_path):
            for dir_name in dirs:
                try:
                    file_date = datetime.strptime(dir_name[0: 10], '%Y-%m-%d')  # 日志日期
                    if file_date < last_day:
                        delete_list.append(os.path.join(root, dir_name))
                except Exception as e:
                    pass

    delete_list = []  # 需要删除的路径
    last_day = datetime.now() - timedelta(days=retentionDays)# 最后保留日
    log_path = os.path.join(PROJECT_ROUTE, 'logs')  # airflow系统日志路径
    _get_airflow_log(log_path)
    print('delete_list', delete_list)
    for delete_path in delete_list:
        if os.path.exists(delete_path) and os.path.isdir(delete_path):
            shutil.rmtree(delete_path)
