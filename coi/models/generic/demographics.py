from google.appengine.ext import db
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

## Model Imports
from coi.models.generic.geo import GeoArea
from coi.models.generic.source import DataSource


class DemographicCriterion(E):

    """ Describes a data point that can be held about a person or group of people. """
    pass
    
class AgeBracket(DemographicCriterion): pass
class Gender(DemographicCriterion): pass
class Ethnicity(DemographicCriterion): pass
class Religion(DemographicCriterion): pass
class SexualOrientation(DemographicCriterion): pass


## Statistics

class DemographicStat(E):
    
    """ Describes the percentage and count of a demographic criterion. """
    source = db.ReferenceProperty(DataSource, collection_name="demographic_stats")
    criterion = db.ReferenceProperty(DemographicCriterion, collection_name="statistics")
    percentage_of_total = db.FloatProperty()
    total_count = db.IntegerProperty()


class DemographicGeoStat(DemographicStat):
    
    """ Describes the percentage and count of a demographic criterion for a geo area. """
    geoarea = db.ReferenceProperty(GeoArea, collection_name="demographic_geo_stat")
    

class DemographicDateStat(DemographicStat):
    
    """ Describes where a single date and a demographic statistic intersect. """
    date = db.DateProperty()


class DemographicGeoDateStat(DemographicGeoStat):
    
    """ Describes where a single date, a geo area, and a demographic statistic intersect. """
    date = db.DateProperty()


class DemographicDateRangeStat(DemographicStat):
    
    """ Describes where a date range and a demographic statistic intersect. """
    start_date = db.DateProperty()
    end_date = db.DateProperty()
    

class DemographicDateRangeGeoStat(DemographicGeoStat):
    
    """ Describes where a date range, geo area, and demographic statistic intersect. """
    start_date = db.DateProperty()
    end_date = db.DateProperty()


class DemographicDateTimeStat(DemographicStat):
    
    """ Describes where a datetime and a demographic statistic intersect. """
    datetime = db.DateTimeProperty()
        

class DemographicDateTimeRangeStat(DemographicStat):
    
    """ Describes where a datetime range and a demographic statistic intersect. """
    start_datetime = db.DateTimeProperty()
    end_datetime = db.DateTimeProperty()
    
    
class DemographicDateTimeRangeGeoStat(DemographicGeoStat):
    
    """ Describes where a date range, geo area, and demographic statistic intersect. """
    start_datetime = db.DateTimeProperty()
    end_datetime = db.DateTimeProperty()    
    

    
## Proto Inserts

class ProtoHelper():

    models = []

    def insert(self):

        ## DemographicCriterion series

        self.models.append(P(key_name='DemographicCriterion',name=['DemographicCriterion'],description='Abstract model representing something that describes a demogrpahic.',
                            direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=True,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))

                            
        self.models.append(P(key_name='AgeBracket',name=['AgeBracket'],description='Describes an age group (13-17, for example).',
                            direct_parent=db.Key.from_path('Proto','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))

                            
        self.models.append(P(key_name='Gender',name=['Gender'],description='Describes a gender - male, female, or transsexual.',
                            direct_parent=db.Key.from_path('Proto','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=True,uses_parent=False,uses_id=False,
                            created_modified=True,keyname_use="Basic name of gender (male/female)."))

                            
        self.models.append(P(key_name='Ethnicity',name=['Ethnicity'],description='Describes an ethnicity',
                            direct_parent=db.Key.from_path('Proto','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))

                            
        self.models.append(P(key_name='Religion',name=['Religion'],description='Describes a religion.',
                            direct_parent=db.Key.from_path('Proto','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(P(key_name='SexualOrientation',name=['SexualOrientation'],description='Describes a sexual orientation.',
                            direct_parent=db.Key.from_path('Proto','DemographicCriterion'),ancestry_path=['E','DemogrpahicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True,keyname_use="Common name for sexual orientation."))
                            
        ## DemographicStat series
                            
        self.models.append(P(key_name='DemographicStat',name=['DemographicStat'],description='Abstract model representing where a stat and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','E'),ancestry_path=['E'],abstract=True,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(P(key_name='DemographicGeoStat',name=['DemographicGeoStat'],description='Abstract model representing something that describes a demogrpahic.',
                            direct_parent=db.Key.from_path('Proto','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(P(key_name='DemographicDateStat',name=['DemographicDateStat'],description='Where a date and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))                  
                            
                            
        self.models.append(P(key_name='DemographicGeoDateStat',name=['DemographicGeoDateStat'],description='Where a date, a geo area, and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','DemographicGeoStat'),ancestry_path=['E','DemographicStat','DemographicGeoStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))                            


        self.models.append(P(key_name='DemographicDateRangeStat',name=['DemographicDateRangeStat'],description='Where a date range and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(P(key_name='DemographicDateRangeGeoStat',name=['DemographicDateRangeGeoStat'],description='Where a date range, a geo area, and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','DemographicGeoStat'),ancestry_path=['E','DemographicStat','DemographicGeoStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        self.models.append(P(key_name='DemographicDateTimeStat',name=['DemographicDateTimeStat'],description='Where a datetime and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        self.models.append(P(key_name='DemographicDateTimeRangeStat',name=['DemographicDateTimeRangeStat'],description='Where a datetime range and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        self.models.append(P(key_name='DemographicDateTimeRangeGeoStat',name=['DemographicDateTimeRangeGeoStat'],description='Where a datetime range, a geo area, and a demographic intersect.',
                            direct_parent=db.Key.from_path('Proto','DemographicGeoStat'),ancestry_path=['E','DemographicStat','DemographicGeoStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))                                                                                                                

        return self.models
        
        

    def clean(self):
        
        self.models.append(P.get_by_key_name('DemographicCriterion'))
        self.models.append(P.get_by_key_name('AgeBracket'))
        self.models.append(P.get_by_key_name('Gender'))
        self.models.append(P.get_by_key_name('Ethnicity'))
        self.models.append(P.get_by_key_name('Religion'))
        self.models.append(P.get_by_key_name('SexualOrientation'))
        self.models.append(P.get_by_key_name('DemographicStat'))
        self.models.append(P.get_by_key_name('DemographicGeoStat'))
        self.models.append(P.get_by_key_name('DemographicDateStat'))
        self.models.append(P.get_by_key_name('DemographicGeoDateStat'))
        self.models.append(P.get_by_key_name('DemographicDateRangeStat'))
        self.models.append(P.get_by_key_name('DemographicDateRangeGeoStat'))
        self.models.append(P.get_by_key_name('DemographicDateTimeStat'))
        self.models.append(P.get_by_key_name('DemographicDateTimeRangeStat'))
        self.models.append(P.get_by_key_name('DemographicDateTimeRangeGeoStat'))

        return self.models