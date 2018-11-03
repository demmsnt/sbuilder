from abc import ABCMeta, abstractmethod


class NoDefailt:
    """Empy class to allow None as default"""
    pass


class AbstractConfig(metaclass=ABCMeta):
    """fix interface"""
    def __init__(self, app):
        self.app = app

    @abstractmethod
    def get(self, key, **args):
        """Имитация словаря"""

    @abstractmethod
    def __getitem__(self, key):
        """Имитация словаря"""

    @abstractmethod
    def find(self, path, default=NoDefailt):
        """XPath like find key"""

    @abstractmethod
    def reload(self):
        """Reload config"""