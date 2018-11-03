import yaml
import dpath.util
from admin.config.abc import AbstractConfig, NoDefailt
import os

class ConfigItem(object):
    def __init__(self, item):
        self.item = item

    def get(self, key, **args):
        default = None
        if len(args) > 0:
            default = args[0]
        item = self.item.get(key, default)
        if isinstance(item, dict):
            item = ConfigItem(item)
        return item

    def __getitem__(self, key):
        item = self.item[key]
        if isinstance(item, dict):
            item = ConfigItem(item)
        return item

    def find(self, path, default=NoDefailt):
        """Поиск как XPath"""
        try:
            item = dpath.util.get(self.item, path)
        except KeyError as e:
            if default != NoDefailt:
                return default
            raise e
        if isinstance(item, dict):
            item = ConfigItem(item)
        return item


class YamlConfig(ConfigItem, AbstractConfig):
    """Конфиг хранимый в ямле"""
    def __init__(self, app, path="./config.yaml"):
        super(YamlConfig, self).__init__(dict())
        self.path = path
        self.reload()

    def reload(self):
        """Reload config"""
        self.item = yaml.load(open(self.path, 'r').read())
