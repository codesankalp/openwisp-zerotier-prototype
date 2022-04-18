from copy import deepcopy
from netjsonconfig import ZeroTier as BaseZeroTier
from copy import deepcopy

class ZeroTier(BaseZeroTier):
    
    schema = deepcopy(BaseZeroTier.schema)
