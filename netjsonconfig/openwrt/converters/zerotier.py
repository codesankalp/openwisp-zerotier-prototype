from ...zerotier.converters import ZeroTier as BaseZeroTier
from .base import OpenWrtConverter


class ZeroTier(OpenWrtConverter, BaseZeroTier):
    _uci_types = ['zerotier']

    def __intermediate_vpn(self, vpn):
        vpn.update(
            {
                '.name': self._get_uci_name(vpn.pop('name')),
                '.type': 'zerotier',
            }
        )
        return super().__intermediate_vpn(vpn, remove=[''])

    def __netjson_vpn(self, vpn):
        # 'enabled' defaults to False in OpenWRT
        vpn['disabled'] = vpn.pop('enabled', '0') == '0'
        vpn['name'] = vpn.pop('.name')
        del vpn['.type']
        return super().__netjson_vpn(vpn)
