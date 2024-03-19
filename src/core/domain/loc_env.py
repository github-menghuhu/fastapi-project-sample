import os

os.environ["POSTGRESQL_HOST"] = "127.0.0.1"
os.environ["POSTGRESQL_PORT"] = "5433"
os.environ["POSTGRESQL_USER"] = "postgres"
os.environ["POSTGRESQL_PASSWORD"] = "123456"
os.environ["POSTGRESQL_NAME"] = "fastapi-nebula-test"

os.environ["REDIS_HOST"] = "127.0.0.1"
os.environ["REDIS_PORT"] = "6379"
os.environ["REDIS_USER"] = ""
os.environ["REDIS_PASSWORD"] = ""
