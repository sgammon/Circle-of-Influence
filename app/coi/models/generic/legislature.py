from google.appengine.ext import db
from ProvidenceClarity.api.data import DataManager
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

from coi.models.generic.government import GovtOffice

class LegislativeBody(E):
    """ Describes a body that forms and passes legislation. """
    
    short_name = db.StringProperty()
    long_name = db.StringProperty()
    
class LegislativeHouse(E):
    
    """ Describes a house in a legislature, like a senate or house of representatives. """
    
    short_name = db.StringProperty()
    long_name = db.StringProperty()
    body = db.ReferenceProperty(LegislativeBody, collection_name="houses")
    status = db.StringProperty(choices=['upper','lower'],default=None)
    
class LegislativeSession(E):
    
    """ Describes a calendar session wherein a legislature works on legislation. """
    
    body = db.ReferenceProperty(LegislativeBody, collection_name="sessions")
    start_date = db.DateProperty()
    end_date = db.DateProperty()
    duration_in_days = db.IntegerProperty()

class LegislativeOffice(GovtOffice):
    
    """Describes a legislative-type office."""
    
    legislature = db.ReferenceProperty(LegislativeBody, collection_name="offices")
    house = db.ReferenceProperty(LegislativeHouse, collection_name="offices")
    
class DistrictBasedOffice(LegislativeOffice):
    
    """ Describes a legislative office based on some sort of geographical boundary smaller than a state. """
    
    pass
    
class StateBasedOffice(LegislativeOffice):
    
    """ Describes a legislative office based on a state. """
    
    pass
    
    
## Proto Inserts

class ProtoHelper(DataManager):

    models = []

    def insert(self):
        
        self.models.append(self.P(_class=LegislativeBody,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(self.P(_class=LegislativeHouse,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(self.P(_class=LegislativeSession,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True,keyname_use=None,keyid_use=None,keyparent_use=None))
                                   
        self.models.append(self.P(_class=LegislativeOffice,
                                    direct_parent=db.Key.from_path('Proto','GovtOffice'),ancestry_path=['E','Office','GovtOffice'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True,keyname_use=None,keyid_use=None,keyparent_use=None))
                                   
        self.models.append(self.P(_class=DistrictBasedOffice,
                                    direct_parent=db.Key.from_path('Proto','LegislativeOffice'),ancestry_path=['E','GovtOffice','LegislativeOffice'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True,keyname_use=None,keyid_use=None,keyparent_use=None))
                                   
        self.models.append(self.P(_class=StateBasedOffice,
                                    direct_parent=db.Key.from_path('Proto','LegislativeOffice'),ancestry_path=['E','Office','GovtOffice','LegislativeOffice'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True,keyname_use=None,keyid_use=None,keyparent_use=None))
                                   
        return self.models


    def base(self):
        
        pass
    

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('LegislativeBody'))
        self.models.append(self.P.get_by_key_name('LegislativeHouse'))
        self.models.append(self.P.get_by_key_name('LegislativeSession'))
        self.models.append(self.P.get_by_key_name('LegislativeOffice'))
        self.models.append(self.P.get_by_key_name('DistrictBasedOffice'))
        self.models.append(self.P.get_by_key_name('StateBasedOffice'))
        
        return self.models