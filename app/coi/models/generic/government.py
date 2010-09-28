from google.appengine.ext import db
from ProvidenceClarity import Platform
from coi.models.generic.office import Office

class Government(Platform.ext.Entity):
    """ Describes a government. """
    pass

class GovtOffice(Office):
    """Describes government office."""
    government = db.ReferenceProperty(Government, collection_name="offices")
    
    
## Proto Inserts

class ProtoHelper(Platform.ext.DataManager):

    models = []

    def insert(self):
        
        self.models.append(self.P(_class=Government,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=True,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True,keyname_use=None,keyid_use=None,keyparent_use=None))
        
        self.models.append(self.P(_class=GovtOffice,
                                    direct_parent=db.Key.from_path('Proto','Office'),ancestry_path=['E','Office'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
    
        return self.models

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('GovtOffice'))
        
        return self.models