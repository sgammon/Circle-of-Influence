from google.appengine.ext import db
from coi.models.us.state import USState
from coi.models.generic.legislature import LegislativeBody


class StateLegislature(LegislativeBody):
    
    """ Describes a legislature for a US State. """
    
    state = db.ReferenceProperty(USState, collection_name="legislature")
    legislature_name = db.StringProperty()


## Proto Inserts

class ProtoHelper(object):

    models = []

    def insert(self):
        
        self.models.append(self.P(_class=StateLegislature,
                                    direct_parent=db.Key.from_path('Proto','LegislativeBody'),ancestry_path=['E','GeoArea','State','USState'],abstract=False,derived=False,is_data=True,poly_model=True,uses_keyname=True,uses_parent=True,uses_id=False,
                                   created_modified=True,keyname_use='Official postal service 2-letter abbreviation of US state.',keyid_use=None,keyparent_use='US State record the legislature is based on.'))
        
        return self.models

    def base(self):
        
        self.models.append(StateLegislature(USState.get_by_key_name('AL'),key_name='AL',state=db.Key.from_path('USState','AL')))
        self.models.append(StateLegislature(USState.get_by_key_name('AK'),key_name='AK',state=db.Key.from_path('USState','AK')))
        self.models.append(StateLegislature(USState.get_by_key_name('AZ'),key_name='AZ',state=db.Key.from_path('USState','AZ')))
        self.models.append(StateLegislature(USState.get_by_key_name('AR'),key_name='AR',state=db.Key.from_path('USState','AR')))
        self.models.append(StateLegislature(USState.get_by_key_name('CA'),key_name='CA',state=db.Key.from_path('USState','CA')))
        self.models.append(StateLegislature(USState.get_by_key_name('CO'),key_name='CO',state=db.Key.from_path('USState','CO')))
        self.models.append(StateLegislature(USState.get_by_key_name('CT'),key_name='CT',state=db.Key.from_path('USState','CT')))
        self.models.append(StateLegislature(USState.get_by_key_name('DE'),key_name='DE',state=db.Key.from_path('USState','DE')))
        self.models.append(StateLegislature(USState.get_by_key_name('FL'),key_name='FL',state=db.Key.from_path('USState','FL')))
        self.models.append(StateLegislature(USState.get_by_key_name('GA'),key_name='GA',state=db.Key.from_path('USState','GA')))
        self.models.append(StateLegislature(USState.get_by_key_name('HI'),key_name='HI',state=db.Key.from_path('USState','HI')))
        self.models.append(StateLegislature(USState.get_by_key_name('ID'),key_name='ID',state=db.Key.from_path('USState','ID')))
        self.models.append(StateLegislature(USState.get_by_key_name('IL'),key_name='IL',state=db.Key.from_path('USState','IL')))
        self.models.append(StateLegislature(USState.get_by_key_name('IN'),key_name='IN',state=db.Key.from_path('USState','IN')))
        self.models.append(StateLegislature(USState.get_by_key_name('IA'),key_name='IA',state=db.Key.from_path('USState','IA')))
        self.models.append(StateLegislature(USState.get_by_key_name('KS'),key_name='KS',state=db.Key.from_path('USState','KS')))
        self.models.append(StateLegislature(USState.get_by_key_name('KY'),key_name='KY',state=db.Key.from_path('USState','KY')))
        self.models.append(StateLegislature(USState.get_by_key_name('LA'),key_name='LA',state=db.Key.from_path('USState','LA')))
        self.models.append(StateLegislature(USState.get_by_key_name('ME'),key_name='ME',state=db.Key.from_path('USState','ME')))
        self.models.append(StateLegislature(USState.get_by_key_name('MD'),key_name='MD',state=db.Key.from_path('USState','MD')))
        self.models.append(StateLegislature(USState.get_by_key_name('MA'),key_name='MA',state=db.Key.from_path('USState','MA')))
        self.models.append(StateLegislature(USState.get_by_key_name('MI'),key_name='MI',state=db.Key.from_path('USState','MI')))
        self.models.append(StateLegislature(USState.get_by_key_name('MN'),key_name='MN',state=db.Key.from_path('USState','MN')))
        self.models.append(StateLegislature(USState.get_by_key_name('MS'),key_name='MS',state=db.Key.from_path('USState','MS')))
        self.models.append(StateLegislature(USState.get_by_key_name('MO'),key_name='MO',state=db.Key.from_path('USState','MO')))
        self.models.append(StateLegislature(USState.get_by_key_name('MT'),key_name='MT',state=db.Key.from_path('USState','MT')))
        self.models.append(StateLegislature(USState.get_by_key_name('NE'),key_name='NE',state=db.Key.from_path('USState','NE')))
        self.models.append(StateLegislature(USState.get_by_key_name('NV'),key_name='NV',state=db.Key.from_path('USState','NV')))
        self.models.append(StateLegislature(USState.get_by_key_name('NH'),key_name='NH',state=db.Key.from_path('USState','NH')))
        self.models.append(StateLegislature(USState.get_by_key_name('NJ'),key_name='NJ',state=db.Key.from_path('USState','NJ')))
        self.models.append(StateLegislature(USState.get_by_key_name('NM'),key_name='NM',state=db.Key.from_path('USState','NM')))
        self.models.append(StateLegislature(USState.get_by_key_name('NY'),key_name='NY',state=db.Key.from_path('USState','NY')))
        self.models.append(StateLegislature(USState.get_by_key_name('NC'),key_name='NC',state=db.Key.from_path('USState','NC')))
        self.models.append(StateLegislature(USState.get_by_key_name('ND'),key_name='ND',state=db.Key.from_path('USState','ND')))
        self.models.append(StateLegislature(USState.get_by_key_name('OH'),key_name='OH',state=db.Key.from_path('USState','OH')))
        self.models.append(StateLegislature(USState.get_by_key_name('OK'),key_name='OK',state=db.Key.from_path('USState','OK')))
        self.models.append(StateLegislature(USState.get_by_key_name('OR'),key_name='OR',state=db.Key.from_path('USState','OR')))
        self.models.append(StateLegislature(USState.get_by_key_name('PA'),key_name='PA',state=db.Key.from_path('USState','PA')))
        self.models.append(StateLegislature(USState.get_by_key_name('RI'),key_name='RI',state=db.Key.from_path('USState','RI')))
        self.models.append(StateLegislature(USState.get_by_key_name('SC'),key_name='SC',state=db.Key.from_path('USState','SC')))
        self.models.append(StateLegislature(USState.get_by_key_name('SD'),key_name='SD',state=db.Key.from_path('USState','SD')))
        self.models.append(StateLegislature(USState.get_by_key_name('TN'),key_name='TN',state=db.Key.from_path('USState','TN')))
        self.models.append(StateLegislature(USState.get_by_key_name('TX'),key_name='TX',state=db.Key.from_path('USState','TX')))
        self.models.append(StateLegislature(USState.get_by_key_name('UT'),key_name='UT',state=db.Key.from_path('USState','UT')))
        self.models.append(StateLegislature(USState.get_by_key_name('VT'),key_name='VT',state=db.Key.from_path('USState','VT')))
        self.models.append(StateLegislature(USState.get_by_key_name('VA'),key_name='VA',state=db.Key.from_path('USState','VA')))
        self.models.append(StateLegislature(USState.get_by_key_name('WA'),key_name='WA',state=db.Key.from_path('USState','WA')))
        self.models.append(StateLegislature(USState.get_by_key_name('WV'),key_name='WV',state=db.Key.from_path('USState','WV')))
        self.models.append(StateLegislature(USState.get_by_key_name('WI'),key_name='WI',state=db.Key.from_path('USState','WI')))
        self.models.append(StateLegislature(USState.get_by_key_name('WY'),key_name='WY',state=db.Key.from_path('USState','WY')))
        
        return self.models

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('StateLegislature'))
        
        return self.models