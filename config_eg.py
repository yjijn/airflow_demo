#!/usr/bin/env python
# -- coding = 'utf-8' --

# debug服务配置
# 爬虫配置
# 获取年报的地址
YEAR_REPORT_URLS = {
    'df': 'http://finance.eastmoney.com/a/cssgs.html',  # 东方财富
    'jc': 'http://www.cninfo.com.cn/new/hisAnnouncement/query'  #'http://www.cninfo.com.cn/new/index'# 巨潮
}

# 获取社报的地址
SOCIAL_REPORT_URLS = {
    'jc': 'http://www.cninfo.com.cn/new/hisAnnouncement/query  '#'http://www.cninfo.com.cn/new/index'# 巨潮
}

# 请求重试次数
MAX_RETRY = 5

# 数据库配置
ODS_OPTION = {
  'HOST': '172.24.3.61',
  'USERNAME': 'root',
  'PASSWORD': 'csr123',
  'DATABASE': 'ods_test',
  'PORT': 3306
}

DW_OPTION = {
  'HOST': '172.24.3.61',
  'USERNAME': 'root',
  'PASSWORD': 'csr123',
  'DATABASE': 'dw_test',
  'PORT': 3306
}

DM_OPTION = {
  'HOST': '172.24.3.61',
  'USERNAME': 'root',
  'PASSWORD': 'csr123',
  'DATABASE': 'dm_test',
  'PORT': 3306
}

# 项目目录
PROJECT_ROUTE = '/airflow'

# 文件存放路径
YEAR_REPORT_ROUTE = PROJECT_ROUTE + '/data/yearReport/'  # 年报存放路径
SOCIAL_REPORT_ROUTE = PROJECT_ROUTE + '/data/socialReport/'  # 社报存放路径

# 日志路径
YEAR_REPORT_LOG_ROUTE = PROJECT_ROUTE + '/logs/yearReport/'  # 年报日志存放路径
SOCIAL_REPORT_LOG_ROUTE = PROJECT_ROUTE + '/logs/socialReport/'  # 年报日志存放路径
ETL_LOG_ROUTE = PROJECT_ROUTE + '/logs/etl/'


# 接口appkey
APPKEY_temp = 'a6ebdae634ce4fe9ac1ecbbc1e778c4a'
SECRET_KEY ='e8d26b7f-1b0c-41cf-9e9e-34ced649366e'

# 集团接口
APPID = 'nfzm'
ACCESSKEY = '7D24EC7B25774FE091C1660AFFA36CD1'

# 数据库表
TABLE_1 = 'fact_public_sentiment'
TABLE_2 = 'fact_public_sentiment_detail'
TABLE_3 = 'dw_sentiment_data'

# data_backend_server
DATA_BACKEND_SERVER = 'http://127.0.0.1:8000'

# user_backend_server
USER_BACKEND_SERVER = 'http://127.0.0.1:8001'
USER_BACKEND_USER = 'ETL服务'
USER_BACKEND_PWD = 'Qsc@123'

# aliyuncs oss server
AL_OSS_SERVER = True  # oss服务使用标记
AL_OSS_URL = 'oss-cn-beijing.aliyuncs.com'
AL_OSS_OPTION = {
    'AK_ID': 'LTAI4GEcUvUNQCLN25gRfNTg',
    'AK_SE': 'UFr9z5LZFdhpKEIDiWtJhnkrUnIN2y',
    'BUCKET_NAME': 'tmpreport'
}

# 企业微信群机器人Webhook
WX_WORK_WEB_HOOK = '06c8e670-93da-4f60-8d6c-3e527da04609'
WX_AUDIT_WEB_HOOK = '2e384ca0-c8a5-4a86-af10-cea34dd89efc'