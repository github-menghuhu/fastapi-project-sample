import os

# 全局配置环境
ENV = os.getenv("ENV")

if ENV == "prod":
    FAST_API_DOCS_URL = None
    FAST_API_REDOC_URL = None
else:
    FAST_API_DOCS_URL = "/docs"
    FAST_API_REDOC_URL = "/redoc"

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# 全局时区
TIME_ZONE = "Asia/Shanghai"

# 全局时间格式化规则
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# 全局密钥
SECRET = ""

# jwt过期时间（单位秒）
JWT_LIFETIME_SECONDS = 60 * 60 * 24 * 7

# postgresql
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_PORT = os.getenv("POSTGRESQL_PORT")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_NAME = os.getenv("POSTGRESQL_NAME")
IS_PRINT_SQL = True

# redis
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_USER = os.getenv("REDIS_USER")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

# authing
AUTHING_APP_ID = os.getenv("AUTHING_APP_ID")
AUTHING_APP_SECRET = os.getenv("AUTHING_APP_SECRET")
AUTHING_APP_HOST = os.getenv("AUTHING_APP_HOST")
AUTHING_REDIRECT_URL = os.getenv("AUTHING_REDIRECT_URL")

# celery
CELERY_BROKER_DB = 0
CELERY_RESULT_DB = 1
CELERY_RESULT_EXPIRES = 60 * 60 * 24 * 7

# 其他媒体文件暂存根路由
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
