import os

config_variables = {
    'ENV': os.getenv('WORKING_ENV') or 'develop',
    'TRINO_HOST': os.getenv('TRINO_HOST') or 'no Trino host',
    'TRINO_PORT': os.getenv('TRINO_PORT') or 'no Trino port',
    'TRINO_USER': os.getenv('TRINO_USER') or 'no Trino user',
    'TRINO_CATALOG': os.getenv('TRINO_CATALOG') or 'no Trino catalog',
    'TRINO_SCHEMA': os.getenv('TRINO_SCHEMA') or 'no Trino schema'
}


class Config(object):
    def __init__(self):
        self._config = config_variables

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]


class BasicConfig(Config):

    @property
    def env(self):
        return self.get_property('ENV')

    @property
    def trino_host(self):
        return self.get_property('TRINO_HOST')

    @property
    def trino_port(self):
        return self.get_property('TRINO_PORT')

    @property
    def trino_user(self):
        return self.get_property('TRINO_USER')

    @property
    def trino_catalog(self):
        return self.get_property('TRINO_CATALOG')

    @property
    def trino_schema(self):
        return self.get_property('TRINO_SCHEMA')


config_by_name = dict(
    BasicConfig=BasicConfig()
)
