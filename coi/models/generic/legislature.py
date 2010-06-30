from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

from coi.models.generic.government import GovtOffice
from coi.models.generic.legislature import LegislativeBody, LegislativeHouse

class LegislativeBody(E):
    pass
    
class LegislativeHouse(E):
    body = db.ReferenceProperty(LegislativeBody, collection_name="houses")
    status = db.StringProperty(choices=['upper','lower'],default=None)
    
class LegislativeSession(E):
    body = db.ReferenceProperty(LegislativeBody, collection_name="sessions")
    start_date = db.DateProperty()
    end_date = db.DateProperty()
    duration_in_days = db.IntegerProperty()

class LegislativeOffice(GovtOffice):
    """Describes a legislative-type office."""
    legislature = db.ReferenceProperty(LegislativeBody, collection_name="offices")
    house = db.ReferenceProperty(LegislativeHouse, collection_name="offices")
    
class DistrictBasedOffice(LegislativeOffice):
    pass
    
class StateBasedOffice(LegislativeOffice):
    pass
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(P(key_name='LegislativeBody',name=['LegislativeBody'],description='Describes a body that forms and passes legislation.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='LegislativeHouse',name=['LegislativeHouse'],description='Describes a house in a legislature, like a senate or house of representatives.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        return self.models
    

    def clean(self):
        
        self.models.append(P.get_by_key_name('LegislativeBody'))
        self.models.append(P.get_by_key_name('LegislativeHouse'))
        
        return self.models