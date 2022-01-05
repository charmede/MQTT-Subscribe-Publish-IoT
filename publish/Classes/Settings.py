import random


class Settings:
    def __init__(self):
        pass

    def get_broker(self):
        return 'broker.emqx.io'

    def get_port(self):
        return 1883

    def get_topic(self):
        return "python/mqtt"

    def get_client_id(self):
        return f'python-mqtt-{random.randint(0, 1000)}'

    def get_username(self):
        return 'emqx'

    def get_password(self):
        return 'public'
