from google.appengine.ext import db
from ProvidenceClarity import Platform

## Abstract Models

class Office(Platform.ext.Entity):
    """Describes an office that a person can hold."""
    filled = db.DateProperty()
    left = db.DateProperty()
    
    
## Proto Inserts

class ProtoHelper(Platform.ext.DataManager):

    models = []

    def insert(self):
        
        self.models.append(self.P(_class=Office,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=True,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
    
        return self.models

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('Office'))
        
        return self.models