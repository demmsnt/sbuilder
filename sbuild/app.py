#!/usr/bin/python3
import logging
from services.config import YamlConfig

log = logging.getLogger(__name__)


class SbuildApplication(object):
    def __init__(self, config=YamlConfig):
        self.services = {
            'config': YamlConfig(self)
        }
        self.routers = []
        self.contenttrypes = {}

    def add_service(self, name, service):
        if name in self.services:
            log.warning('Service {} alredy in services and will be overridden'.format(name))
        self.services[name] = service

    def load_config(self):
        cfg = self.services['config']
        try:
            services
        except KeyError:
            log.warning('Services section not found in config')
            return
        for service in cfg.find('services'):
            sclass = ''
            name = ''
            params = ''
            if isinstance(service, dict):
                sclass = service.get('class', '')
                name = service.get('name', '')
                params = service.get('params', [])
            elif isinstance(service, str):
                sclass = service
            if name == '':
                name = sclass
            if sclass == '':
                sclass = name
            if sclass == '':
                raise RuntimeError("Bad service name or class for service {}".format(str(service)))
            

if __name__ == '__main__':
    app = SbuildApplication()
    app.load_config()