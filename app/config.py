"""Application configuration."""

from environs import Env

env = Env()
env.read_env()


SECRET_KEY = env.str("SECRET_KEY")


SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False


PC_ON = env.str("PC_ON")


PUSHOVER_APP_TOKEN = env.str("PUSHOVER_APP_TOKEN")
PUSHOVER_USER_KEY = env.str("PUSHOVER_USER_KEY")


ESP32_PC_ON_KEY = env.str("ESP32_PC_ON_KEY")


THINKSPEAK_API_KEY = env.str("THINKSPEAK_API_KEY")


MQTT_HOST = env.str("MQTT_HOST")
MQTT_PORT = env.int("MQTT_PORT")
MQTT_CA_CERTIFICATE = env.str("MQTT_CA_CERTIFICATE")
MQTT_CLIENT_ID = env.str("MQTT_CLIENT_ID")
MQTT_TOPIC = env.str("MQTT_TOPIC")
