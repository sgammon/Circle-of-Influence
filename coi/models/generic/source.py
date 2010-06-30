from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

class DataSource(E):
    pass

class DataFeed(E):
    pass
    
class DataEntry(E):
    pass

## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(P(key_name='DataSource',name=['DataSource'],description='Describes an external Providence/Clarity data source.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='DataFeed',name=['DataFeed'],description='Describes a feed of data available at a DataSource.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='DataEntry',name=['DataEntry'],description='Describes an entry in a DataFeed that is available from a DataSource.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
        
        return self.models
    

    def clean(self):
        
        self.models.append(P.get_by_key_name('DataSource'))
        self.models.append(P.get_by_key_name('DataFeed'))
        self.models.append(P.get_by_key_name('DataEntry'))
        
        return self.models