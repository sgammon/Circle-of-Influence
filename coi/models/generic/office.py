from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

## External Imports
from coi.models.generic.geo import LegislativeDistrict, State
from coi.models.generic.executive import ExecutiveBody
from coi.models.generic.government import Government
from coi.models.generic.legislature import LegislativeBody, LegislativeHouse


## Abstract Models

class Office(E):
    """Describes an office that a person can hold."""
    created = db.DateProperty()
    destroyed = db.DateProperty()
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(P(key_name='Office',name=['Office'],description='Describes an office that a person can hold.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
    
        return self.models

    def clean(self):
        
        self.models.append(P.get_by_key_name('Office'))
        
        return self.models