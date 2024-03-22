import os

# postgresql
os.environ["POSTGRESQL_HOST"] = "127.0.0.1"
os.environ["POSTGRESQL_PORT"] = "5433"
os.environ["POSTGRESQL_USER"] = "postgres"
os.environ["POSTGRESQL_PASSWORD"] = "123456"
os.environ["POSTGRESQL_NAME"] = "fastapi-nebula-test"

# redis
os.environ["REDIS_HOST"] = "127.0.0.1"
os.environ["REDIS_PORT"] = "6379"
os.environ["REDIS_USER"] = ""
os.environ["REDIS_PASSWORD"] = ""

# authing
os.environ["AUTHING_APP_ID"] = "65fd3671c86993eb77cce77a"
os.environ["AUTHING_APP_SECRET"] = "b33f76c2718d1db79c7a980bde0294c6"
os.environ["AUTHING_APP_HOST"] = "https://kgpfw7kkay0t-demo.authing.cn"
os.environ["AUTHING_REDIRECT_URL"] = "https://console.authing.cn/console/get-started/65fd3671c86993eb77cce77a"
