from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E
from coi.models.generic.government import GovtOffice

class ExecutiveBody(E):
    pass

class ExecutiveOffice(GovtOffice):
    """Describes an executive-type office."""
    body = db.ReferenceProperty(ExecutiveBody, collection_name="offices")
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):

        self.models.append(P(key_name='ExecutiveBody',name=['ExecutiveBody'],description='Describes an executive agency or other institution.',
                            direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        self.models.append(P(key_name='ExecutiveOffice',name=['ExecutiveOffice'],description='Describes an office to be held in an executive body.',
                            direct_parent=db.Key.from_path('Proto','GovtOffice'),ancestry_path=['E','GovtOffice'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        return self.models
        

    def clean(self):

        self.models.append(P.get_by_key_name('ExecutiveBody'))
        self.models.append(P.get_by_key_name('ExecutiveOffice'))
        
        return self.models