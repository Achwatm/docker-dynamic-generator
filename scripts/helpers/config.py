from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import  ConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="./.env", extra='ignore')


    MQTT_BROKER_HOST: str
    MQTT_BROKER_PORT: int
    MQTT_MAIN_TOPIC: str
    MQTT_BROKER_USER: str
    MQTT_BROKER_PASS: str

    
    DEBUG: bool
    GENERATOR_LOOP_INTERVAL: int

settings = Settings()