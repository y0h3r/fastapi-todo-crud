from functools import lru_cache
import os
from pydantic_settings import BaseSettings

@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"

class EnvironmentSettings(BaseSettings):
    DB_PWD: str
    DB_USR: str
    DB_URI: str
    ENCRYPT_HASH: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_SECRET_KEY: str

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"

@lru_cache
def get_environment_variables():
    try:
        env_vars = EnvironmentSettings()
        return env_vars
    except Exception as e:
        print(f"Error loading environment variables: {e}")
        raise 

if __name__ == "__main__":
    settings = get_environment_variables()
