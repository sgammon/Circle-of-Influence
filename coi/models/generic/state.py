from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.core.model import Model

from coi.models.generic.geo import GeoArea, Continent
from coi.models.generic.executive import ExecutiveBody


class Nation(GeoArea):
    
    """ Describes an independent nation. """
    
    # Text Fields
    background = db.TextProperty()
    background_src = db.StringProperty()
    background_src_link = db.LinkProperty()
    
    # Basic Geo Fields
    continent = db.ReferenceProperty(Continent, collection_name="nations")
    basic_coords = db.GeoPtProperty()

    # Area
    area_km = db.FloatProperty()
    area_mi = db.FloatProperty()
    area_rank = db.IntegerProperty()
    area_comparative = db.StringListProperty()
    area_land = db.FloatProperty()
    area_water = db.FloatProperty()
    area_note = db.TextProperty()
    
    # Land
    land_boundaries_total_km = db.FloatProperty()
    land_boundaries_total_mi = db.FloatProperty()
    bordering_nations = db.ListProperty(db.Key)
    

class State(GeoArea):
    
    """ Describes a substate in a nation. """
    nation = db.ReferenceProperty(Nation, collection_name="states")
    
    
class County(GeoArea):

    """ Describes a regional county. """    
    state = db.ReferenceProperty(State, collection_name="counties")
    

class PostalCode(GeoArea):
    
    """ Describes a postal code. """
    code = db.StringProperty(indexed=True)
    nation = db.ReferenceProperty(Nation, collection_name="postal_codes")
    state = db.ReferenceProperty(State, collection_name="postal_codes")
    agency = db.ReferenceProperty(ExecutiveBody, collection_name="postal_codes")
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(P(key_name='Nation',name=['Nation'],description='Describes a nation.',
                                    direct_parent=db.Key.from_path('Proto','GeoArea'),ancestry_path=['E','GeoArea'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='State',name=['State'],description='Describes a state in a nation.',
                                    direct_parent=db.Key.from_path('Proto','GeoArea'),ancestry_path=['E','GeoArea'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='County',name=['County'],description='Describes a county in a state in a nation.',
                                    direct_parent=db.Key.from_path('Proto','GeoArea'),ancestry_path=['E','GeoArea'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='PostalCode',name=['PostalCode'],description='Describes a postal code in a state in a nation.',
                                    direct_parent=db.Key.from_path('Proto','GeoArea'),ancestry_path=['E','GeoArea'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
        
        return self.models
    

    def clean(self):
        
        self.models.append(P.get_by_key_name('Nation'))
        self.models.append(P.get_by_key_name('State'))
        self.models.append(P.get_by_key_name('County'))
        self.models.append(P.get_by_key_name('PostalCode'))
        
        return self.models