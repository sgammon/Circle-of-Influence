from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

## Model Imports
from coi.models.generic.state import Nation, State
from coi.models.generic.office import Office


class Government(E):

    """ Describes a government in the abstract. """

    # Naming
    long_name = db.StringProperty()
    short_name = db.StringProperty()
    abbreviation = db.StringProperty()
    
    type_description = db.TextProperty()
    
    # References
    head_of_state = db.ReferenceProperty(Office)
    head_of_government = db.ReferenceProperty(Office)
    
    
class NationalGovernment(Government):

    """ Describes a government for a nation. """

    nation = db.ReferenceProperty(Nation, collection_name="government")
    
    
class StateGovernment(Government):

    """ Describes a government for a state. """

    state = db.ReferenceProperty(State, collection_name="government")
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(P(key_name='Government',name=['Government'],description='Describes an abstract form a government.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=True,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='NationalGovernment',name=['NationalGovernment'],description='Describes a government that rules a nation.',
                                    direct_parent=db.Key.from_path('Proto','Government'),ancestry_path=['E','Government'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='StateGovernment',name=['StateGovernment'],description='Describes a government that rules a state.',
                                    direct_parent=db.Key.from_path('Proto','Government'),ancestry_path=['E','Government'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
        
        return self.models
    

    def clean(self):
        
        self.models.append(P.get_by_key_name('Government'))
        self.models.append(P.get_by_key_name('NationalGovernment'))
        self.models.append(P.get_by_key_name('StateGovernment'))
        
        return self.models