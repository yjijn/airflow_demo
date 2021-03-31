### 服务依赖
1. 数据库配置：mysql，redis(airflow可选配置)

#
### docker 部署
####airflow_server
```dockerfile
docker run -dti \
--name airflow_server \
--restart always \
-p {宿主计端口}:8080 \
-v {宿主项目路径}:/airflow \
-v {宿主机项目日志路径}:/airflow/logs \
-v {宿主机静态资源路径}:/airflow/data \  # 可选
-d airflow_docker_impage:1.0
```

#
### 项目配置
1.在 /airflow/airflow.cfg中配置airflow基本服务配置
2.在/airflow/dags/config.py中配置项目数据库及项目相关设定信息（config_eg.py为项目配置模板文件）

#
### 项目运行
1. 使用docker exec -it {容器名称} bash 进入容器
2. 进入项目目录： cd /airflow/dags
3. 启动airflow前端服务： airflow webserver -D
4. 启动scheduler监控脚本：sh sche_monitor.sh
5. 启动worker监控脚本：sh work_monitor.sh
6. 浏览器访问http://{服务器ip}:{容器映射端口}启动所需的dag
