from copy import deepcopy

from netjsonconfig import ZeroTier as BaseZeroTier


class ZeroTier(BaseZeroTier):

    schema = deepcopy(BaseZeroTier.schema)
