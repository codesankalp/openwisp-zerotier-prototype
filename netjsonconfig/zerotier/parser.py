import re

from ..base.parser import BaseParser

vpn_pattern = re.compile('^# zerotier config:\s', flags=re.MULTILINE)
config_pattern = re.compile('^([^\s]*) ?(.*)$')
config_suffix = '.conf'


class ZeroTierParser(BaseParser):
    def parse_text(self, config):
        raise NotImplementedError()

    def parse_tar(self, tar):
        raise NotImplementedError()

    def _get_vpns(self, text):
        raise NotImplementedError()

    def _get_config(self, contents):
        raise NotImplementedError()
