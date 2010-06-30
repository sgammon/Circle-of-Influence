from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
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
    name = db.StringProperty()
    
    
## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):

        self.models.append(P(key_name='GeoPoint',name=['GeoPoint'],description='Describes a single geographical point (lat/long).',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
                                   
        self.models.append(P(key_name='GeoArea',name=['GeoArea'],description='Describes a geographical area.',
                                    direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                                   created_modified=True))
    

    def clean(self):
        
        self.models.append(P.get_by_key_name('GeoPoint'))
        self.models.append(P.get_by_key_name('GeoArea'))
        
        return self.models