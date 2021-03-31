#!/usr/bin/env python
# -- coding = 'utf-8' --

# debug服务配置
# 数据库配置
MYSQL_OPTION = {
  'HOST': '127.0.0.1',
  'USERNAME': 'root',
  'PASSWORD': 'xxxx',
  'DATABASE': 'xxx',
  'PORT': 3306
}

# 项目目录
PROJECT_ROUTE = '/airflow'

# 文件存放路径
DATA_ROUTE = PROJECT_ROUTE + '/data/yearReport/'  # 静态资源或数据存放路径

# 日志路径
LOG_ROUTE = PROJECT_ROUTE + '/logs/'  # 日志存放路径
ETL_LOG_ROUTE = PROJECT_ROUTE + '/logs/etl/'

