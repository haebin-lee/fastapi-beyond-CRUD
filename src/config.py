from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:testpass@localhost:5432/bookly"
    JWT_SECRET: str = "2f1b750aea00acb11fe974de577c037f2f5da569a5dc9f7457cdcd8d8878e521"
    JWT_ALGORITHM: str = "HS256"
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    MAIL_USERNAME: str = "norma.schumm5@ethereal.email"
    MAIL_PASSWORD: str = "3UeGDK6pasgKZMQjFE"
    MAIL_FROM: str = "hblee8080@gmail.com"
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.ethereal.email"
    MAIL_FROM_NAME: str = "Haebin Lee"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    DOMAIN: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()


broker_url = Config.REDIS_URL
result_backend = Config.REDIS_URL
broker_connection_retry_on_startup = True