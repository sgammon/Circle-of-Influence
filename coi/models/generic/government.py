from ProvidenceClarity.data.proto import P
from coi.models.generic.office import Office

class GovtOffice(Office):
    """Describes government office."""
    government = db.ReferenceProperty(Government, collection_name="offices")
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(P(key_name='GovtOffice',name=['GovtOffice'],description='Describes an office in a government.',
                                    direct_parent=db.Key.from_path('Proto','Office'),ancestry_path=['E','Office'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
    
        return self.models

    def clean(self):
        
        self.models.append(P.get_by_key_name('GovtOffice'))
        
        return self.models