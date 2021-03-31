import random
import json

from utils.utils_etl import rm_temp_file


def gen_random_data(json_time):  # 生成随机数据文件并写入中间文件
    data = {}
    for i in range(10):
        data[str(i)] = random.randint(1, 100)
    # 生成结果临时文件
    with open('demo_data' + json_time + '.json', 'w') as f:
        f.write(json.dumps(data))
    return json_time


def print_data(json_time):
    # 读取数据
    with open('odsSocialScore' + json_time + '.json', 'r') as f:
        data = json.loads(f.read())
    # 遍历打印数据
    for key, value in data.items():
        print('key: {}, vlaue:{}'.format(key, value))


def rm_etl_temp_file(json_time):  # 删除etl临时文件
    file_list = ['demo_data']
    rm_temp_file(file_list, json_time)
    return json_time
