from google.appengine.ext import db
from ProvidenceClarity.api.data import DataManager
from ProvidenceClarity.data.input import DataSource
from ProvidenceClarity.data.proto import P
from ProvidenceClarity.data.entity import E

## Model Imports
from coi.models.generic.geo import GeoArea


class DemographicCriterion(E):

    """ Describes a data point that can be held about a person or group of people. """
    
    pass
    
class AgeBracket(DemographicCriterion): """ Describes an age bracket (example: 18-24). """
class Gender(DemographicCriterion): """ Describes a gender (example: male). """
class Ethnicity(DemographicCriterion): """ Describes an ethnicity (example: Chicano/Latino). """
class Religion(DemographicCriterion): """ Describes a religion (example: Catholicism). """
class SexualOrientation(DemographicCriterion): """ Describes a sexual orientation (example: Bisexuality). """


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

class ProtoHelper(DataManager):

    models = []

    def insert(self):

        ## DemographicCriterion series

        self.models.append(self.P(_class=DemographicCriterion,
                            direct_parent=db.Key.from_path('P','E'),ancestry_path=['E'],abstract=True,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))

                            
        self.models.append(self.P(_class=AgeBracket,
                            direct_parent=db.Key.from_path('P','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))

                            
        self.models.append(self.P(_class=Gender,
                            direct_parent=db.Key.from_path('P','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=True,uses_parent=False,uses_id=False,
                            created_modified=True,keyname_use="Basic name of gender (male/female)."))

                            
        self.models.append(self.P(_class=Ethnicity,
                            direct_parent=db.Key.from_path('P','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))

                            
        self.models.append(self.P(_class=Religion,
                            direct_parent=db.Key.from_path('P','DemographicCriterion'),ancestry_path=['E','DemographicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(self.P(_class=SexualOrientation,
                            direct_parent=db.Key.from_path('P','DemographicCriterion'),ancestry_path=['E','DemogrpahicCriterion'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True,keyname_use="Common name for sexual orientation."))
                            
        ## DemographicStat series
                            
        self.models.append(self.P(_class=DemographicStat,
                            direct_parent=db.Key.from_path('P','E'),ancestry_path=['E'],abstract=True,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(self.P(_class=DemographicGeoStat,
                            direct_parent=db.Key.from_path('P','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(self.P(_class=DemographicDateStat,
                            direct_parent=db.Key.from_path('P','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))                  
                            
                            
        self.models.append(self.P(_class=DemographicGeoDateStat,
                            direct_parent=db.Key.from_path('P','DemographicGeoStat'),ancestry_path=['E','DemographicStat','DemographicGeoStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))                            


        self.models.append(self.P(_class=DemographicDateRangeStat,
                            direct_parent=db.Key.from_path('P','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
                            
        self.models.append(self.P(_class=DemographicDateRangeGeoStat,
                            direct_parent=db.Key.from_path('P','DemographicGeoStat'),ancestry_path=['E','DemographicStat','DemographicGeoStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        self.models.append(self.P(_class=DemographicDateTimeStat,
                            direct_parent=db.Key.from_path('P','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        self.models.append(self.P(_class=DemographicDateTimeRangeStat,
                            direct_parent=db.Key.from_path('P','DemographicStat'),ancestry_path=['E','DemographicStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))
                            
        self.models.append(self.P(_class=DemographicDateTimeRangeGeoStat,
                            direct_parent=db.Key.from_path('P','DemographicGeoStat'),ancestry_path=['E','DemographicStat','DemographicGeoStat'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=False,uses_parent=False,uses_id=False,
                            created_modified=True))                                                                                                                

        return self.models
        

    def base(self):
        
        # Genders
        self.models.append(Gender(key_name='male',display_text=['male','masculine','man','men'],primary_display_text='male'))
        self.models.append(Gender(key_name='female',display_text=['female','feminine','woman','women'],primary_display_text='female'))
        
        # Sexualities
        self.models.append(SexualOrientation(key_name='heterosexual',display_text=['heterosexual','straight','hetero']))
        self.models.append(SexualOrientation(key_name='homosexual',display_text=['homosexual','gay','homo']))
        self.models.append(SexualOrientation(key_name='bisexual',display_text=['bisexual','bi']))

        return self.models

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('DemographicCriterion'))
        self.models.append(self.P.get_by_key_name('AgeBracket'))
        self.models.append(self.P.get_by_key_name('Gender'))
        self.models.append(self.P.get_by_key_name('Ethnicity'))
        self.models.append(self.P.get_by_key_name('Religion'))
        self.models.append(self.P.get_by_key_name('SexualOrientation'))
        self.models.append(self.P.get_by_key_name('DemographicStat'))
        self.models.append(self.P.get_by_key_name('DemographicGeoStat'))
        self.models.append(self.P.get_by_key_name('DemographicDateStat'))
        self.models.append(self.P.get_by_key_name('DemographicGeoDateStat'))
        self.models.append(self.P.get_by_key_name('DemographicDateRangeStat'))
        self.models.append(self.P.get_by_key_name('DemographicDateRangeGeoStat'))
        self.models.append(self.P.get_by_key_name('DemographicDateTimeStat'))
        self.models.append(self.P.get_by_key_name('DemographicDateTimeRangeStat'))
        self.models.append(self.P.get_by_key_name('DemographicDateTimeRangeGeoStat'))

        return self.models