__protos__ = ['models']

import os, logging


import ProvidenceClarity

_platform = None

class COI(object):
    
    # 1: Class Properties
    platform = None
    
    def __init__(self, *args, **kwargs):
        self._initPlatform()
        super(COI, self).__init__(*args, **kwargs)
        

    def _initPlatform(self):
        
        global _platform
        if _platform is not None:
            self.platform = _platform
        else:
            self.platform = ProvidenceClarity.initialize()