from ..base.converter import BaseConverter
from .schema import schema


class ZeroTier(BaseConverter):
    netjson_key = 'zerotier'
    intermediate_key = 'zerotier'
    _schema = schema

    def to_intermediate_loop(self, block, result, index=None):
        vpn = self.__intermediate_vpn(block)
        result.setdefault('zerotier', [])
        result['zerotier'].append(vpn)
        return result

    def __intermediate_vpn(self, config, remove=[False, 0, '']):
        config['nwid'] = config.pop('id')
        config['n'] = config.get('name')
        return self.sorted_dict(config)
