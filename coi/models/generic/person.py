from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

## Property Imports
from ProvidenceClarity.data.core.properties.util import NormalizedStringListProperty

## Model Imports
from coi.models.generic.demographics import Gender, Ethnicity, Religion, SexualOrientation

class Person(E):
    
    """Describes a single person tracked by the system."""
    
    # Naming fields
    firstname = NormalizedStringListProperty(indexed=True)
    middlename = NormalizedStringListProperty(indexed=True)
    nickname = NormalizedStringListProperty(indexed=True)
    lastname = NormalizedStringListProperty(indexed=True)
    suffix = NormalizedStringListProperty(indexed=True)
    name_dat = NormalizedStringListProperty(indexed=True)
    
    # Personal details
    gender = db.ReferenceProperty(Gender, collection_name="people")
    ethnicity = db.ReferenceProperty(Ethnicity, collection_name="people")
    religion = db.ReferenceProperty(Religion, collection_name="people")
    sexual_orientation = db.ReferenceProperty(SexualOrientation, collection_name="people")
    
    # Date fields
    date_of_birth = db.DateProperty()
    date_of_birth_dat = db.StringListProperty()
    date_of_death = db.DateProperty()
    date_of_death_dat = db.StringListProperty()
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(P(key_name='Person',name=['Person'],description='Describes a person.',
                                    direct_parent=db.Key.from_path('Proto','_otherproto_'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
        
        return self.models
    

    def clean(self):
        
        self.models.append(P.get_by_key_name('Person'))
        
        return self.models