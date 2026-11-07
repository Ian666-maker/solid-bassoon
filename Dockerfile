# 使用官方轻量级 Python 3.10 镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 先复制依赖安装文件或直接安装依赖
RUN pip install --no-cache-dir fastapi uvicorn openai pydantic pymysql

# 复制当前项目的所有文件到容器中
COPY . /app

# 暴露 FastAPI 运行的 8000 端口
EXPOSE 8000

# 启动命令
CMD ["python", "main.py"]