from google.appengine.ext import db
from ProvidenceClarity.api.data import DataManager
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

## Property Imports
from ProvidenceClarity.data.core.properties.util import NormalizedStringListProperty

## Model Imports
from coi.models.generic.person import Person
from coi.models.generic.office import Office


class Role(E):
    
    """ Abstract model that describes a role that a person can play. """
    
    name = db.StringProperty()
    description = db.TextProperty()
    

class RoleMapping(E):
    
    """ Maps a person to something through a role. """
    
    # References
    person = db.ReferenceProperty(Person, collection_name="roles")
    role = db.ReferenceProperty(Role, collection_name="people")
        
    # Date fields
    date_start = db.DateProperty()
    date_start_dat = NormalizedStringListProperty()
    date_end = db.DateProperty()
    date_end_dat = NormalizedStringListProperty()
    

class OfficeMapping(RoleMapping):
    
    """ Maps a person to an office through a role. """
    
    # Added References
    office = db.ReferenceProperty(Office, collection_name="people")
    
    
## Proto Inserts

class ProtoHelper(DataManager):

    models = []

    def insert(self):
        
        self.models.append(self.P(_class=Role,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(self.P(_class=RoleMapping,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(self.P(_class=OfficeMapping,
                                    direct_parent=db.Key.from_path('Proto','RoleMapping'),ancestry_path=['E','RoleMapping'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
        
        return self.models
    

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('Role'))
        self.models.append(self.P.get_by_key_name('RoleMapping'))
        self.models.append(self.P.get_by_key_name('OfficeMapping'))
        
        return self.models