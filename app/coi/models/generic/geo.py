from google.appengine.ext import db
from ProvidenceClarity.api.data import DataManager
from ProvidenceClarity.data.entity import E

## Basic Classes

class GeoPoint(E):

    """ Describes a geographic point. """
    coordinates = db.GeoPtProperty(default=None,indexed=True)
    altitude = db.FloatProperty(default=None,indexed=True)


class GeoArea(E):
    
    """ Describes a geographic area. """
    coordinates = db.ListProperty(db.GeoPt, default=None)
    altitudes = db.ListProperty(float, default=None)
    bboxEast = db.FloatProperty(indexed=True)
    bboxWest = db.FloatProperty(indexed=True)
    bboxSouth = db.FloatProperty(indexed=True)
    bboxNorth = db.FloatProperty(indexed=True)
    geohash = db.StringProperty(indexed=True)
    
    
class Continent(GeoArea):
    
    """ Describes a continent. """
    pass
    
class LegislativeDistrict(GeoArea):
    
    """ Describes an abstract district that is represented in a legislature. """
    pass
    
## Proto Inserts

class ProtoHelper(DataManager):

    models = []

    def insert(self):

        self.models.append(self.P(_class=GeoPoint,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(self.P(_class=GeoArea,
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(self.P(_class=LegislativeDistrict,
                                    direct_parent=db.Key.from_path('Proto','GeoArea'),ancestry_path=['E','GeoArea'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True,keyname_use=None,keyid_use=None,keyparent_use=None))
                            
        return self.models
    
    
    def base(self):
        
        # Continents
        self.models.append(Continent(key_name='asia',display_text=['asia','Asia'],primary_display_text='Asia'))
        self.models.append(Continent(key_name='africa',display_text=['africa','Africa'],primary_display_text='Africa'))
        self.models.append(Continent(key_name='europe',display_text=['europe','Europe'],primary_display_text='Europe'))
        self.models.append(Continent(key_name='north_america',display_text=['north america','North America'],primary_display_text='North America'))
        self.models.append(Continent(key_name='south_america',display_text=['south america','South America'],primary_display_text='South America'))
        self.models.append(Continent(key_name='australia',display_text=['australia','Australia'],primary_display_text='Australia'))
        self.models.append(Continent(key_name='antarctica',display_text=['antarctica','Antarctica'],primary_display_text='Antarctica'))
    
        return self.models
        

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('GeoPoint'))
        self.models.append(self.P.get_by_key_name('GeoArea'))
        self.models.append(self.P.get_by_key_name('LegislativeDistrict'))        
        
        return self.models