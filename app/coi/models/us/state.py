from google.appengine.ext import db
from ProvidenceClarity.api.data import DataManager
from coi.models.generic.state import State


class USState(State):
    
    pass
    
    
## Proto Inserts

class ProtoHelper(DataManager):

    def insert(self):
        
        self.models.append(self.P(_class=USState,
                                    direct_parent=db.Key.from_path('Proto','State'),ancestry_path=['E','GeoArea','State','USState'],abstract=False,derived=True,is_data=True,poly_model=True,uses_keyname=True,uses_parent=False,uses_id=False,
                                   created_modified=True,keyname_use='Official postal service 2-letter abbreviation of US state.',keyid_use=None,keyparent_use=None))
        
        return self.models
        
        
    def base(self):
    
        self.models.append(USState(key_name="AL",abbreviation="AL",fullname="Alabama",primary_display_text="Alabama",display_text=["AL","Alabama"]))
        self.models.append(USState(key_name="AK",abbreviation="AK",fullname="Alaska",primary_display_text="Alaska",display_text=["AK","Alaska"]))
        self.models.append(USState(key_name="AZ",abbreviation="AZ",fullname="Arizona",primary_display_text="Arizona",display_text=["AZ","Arizona"]))
        self.models.append(USState(key_name="AR",abbreviation="AR",fullname="Arkansas",primary_display_text="Arkansas",display_text=["AR","Arkansas"]))
        self.models.append(USState(key_name="CA",abbreviation="CA",fullname="California",primary_display_text="California",display_text=["CA","California"]))
        self.models.append(USState(key_name="CO",abbreviation="CO",fullname="Colorado",primary_display_text="Colorado",display_text=["CO","Colorado"]))
        self.models.append(USState(key_name="CT",abbreviation="CT",fullname="Connecticut",primary_display_text="Connecticut",display_text=["CT","Connecticut"]))
        self.models.append(USState(key_name="DE",abbreviation="DE",fullname="Delaware",primary_display_text="Delaware",display_text=["DE","Delaware"]))
        self.models.append(USState(key_name="FL",abbreviation="FL",fullname="Florida",primary_display_text="Florida",display_text=["FL","Florida"]))
        self.models.append(USState(key_name="GA",abbreviation="GA",fullname="Georgia",primary_display_text="Georgia",display_text=["GA","Georgia"]))
        self.models.append(USState(key_name="HI",abbreviation="HI",fullname="Hawaii",primary_display_text="Hawaii",display_text=["HI","Hawaii"]))
        self.models.append(USState(key_name="ID",abbreviation="ID",fullname="Idaho",primary_display_text="Idaho",display_text=["ID","Idaho"]))
        self.models.append(USState(key_name="IL",abbreviation="IL",fullname="Illinois",primary_display_text="Illinois",display_text=["IL","Illinois"]))
        self.models.append(USState(key_name="IN",abbreviation="IN",fullname="Indiana",primary_display_text="Indiana",display_text=["IN","Indiana"]))
        self.models.append(USState(key_name="IA",abbreviation="IA",fullname="Iowa",primary_display_text="Iowa",display_text=["IA","Iowa"]))
        self.models.append(USState(key_name="KS",abbreviation="KS",fullname="Kansas",primary_display_text="Kansas",display_text=["KS","Kansas"]))
        self.models.append(USState(key_name="KY",abbreviation="KY",fullname="Kentucky",primary_display_text="Kentucky",display_text=["KY","Kentucky"]))
        self.models.append(USState(key_name="LA",abbreviation="LA",fullname="Louisiana",primary_display_text="Louisiana",display_text=["LA","Louisiana"]))
        self.models.append(USState(key_name="ME",abbreviation="ME",fullname="Maine",primary_display_text="Maine",display_text=["ME","Maine"]))
        self.models.append(USState(key_name="MD",abbreviation="MD",fullname="Maryland",primary_display_text="Maryland",display_text=["MD","Maryland"]))
        self.models.append(USState(key_name="MA",abbreviation="MA",fullname="Massachusetts",primary_display_text="Massachusetts",display_text=["MA","Massachusetts"]))
        self.models.append(USState(key_name="MI",abbreviation="MI",fullname="Michigan",primary_display_text="Michigan",display_text=["MI","Michigan"]))
        self.models.append(USState(key_name="MN",abbreviation="MN",fullname="Minnesota",primary_display_text="Minnesota",display_text=["MN","Minnesota"]))
        self.models.append(USState(key_name="MS",abbreviation="MS",fullname="Mississippi",primary_display_text="Mississippi",display_text=["MS","Mississippi"]))
        self.models.append(USState(key_name="MO",abbreviation="MO",fullname="Missouri",primary_display_text="Missouri",display_text=["MO","Missouri"]))
        self.models.append(USState(key_name="MT",abbreviation="MT",fullname="Montana",primary_display_text="Montana",display_text=["MT","Montana"]))
        self.models.append(USState(key_name="NE",abbreviation="NE",fullname="Nebraska",primary_display_text="Nebraska",display_text=["NE","Nebraska"]))
        self.models.append(USState(key_name="NV",abbreviation="NV",fullname="Nevada",primary_display_text="Nevada",display_text=["NV","Nevada"]))
        self.models.append(USState(key_name="NH",abbreviation="NH",fullname="New Hampshire",primary_display_text="New Hampshire",display_text=["NH","New Hampshire"]))
        self.models.append(USState(key_name="NJ",abbreviation="NJ",fullname="New Jersey",primary_display_text="New Jersey",display_text=["NJ","New Jersey"]))
        self.models.append(USState(key_name="NM",abbreviation="NM",fullname="New Mexico",primary_display_text="New Mexico",display_text=["NM","New Mexico"]))
        self.models.append(USState(key_name="NY",abbreviation="NY",fullname="New York",primary_display_text="New York",display_text=["NY","New York"]))
        self.models.append(USState(key_name="NC",abbreviation="NC",fullname="North Carolina",primary_display_text="North Carolina",display_text=["NC","North Carolina"]))
        self.models.append(USState(key_name="ND",abbreviation="ND",fullname="North Dakota",primary_display_text="North Dakota",display_text=["ND","North Dakota"]))
        self.models.append(USState(key_name="OH",abbreviation="OH",fullname="Ohio",primary_display_text="Ohio",display_text=["OH","Ohio"]))
        self.models.append(USState(key_name="OK",abbreviation="OK",fullname="Oklahoma",primary_display_text="Oklahoma",display_text=["OK","Oklahoma"]))
        self.models.append(USState(key_name="OR",abbreviation="OR",fullname="Oregon",primary_display_text="Oregon",display_text=["OR","Oregon"]))
        self.models.append(USState(key_name="PA",abbreviation="PA",fullname="Pennsylvania",primary_display_text="Pennsylvania",display_text=["PA","Pennsylvania"]))
        self.models.append(USState(key_name="RI",abbreviation="RI",fullname="Rhode Island",primary_display_text="Rhode Island",display_text=["RI","Rhode Island"]))
        self.models.append(USState(key_name="SC",abbreviation="SC",fullname="South Carolina",primary_display_text="South Carolina",display_text=["SC","South Carolina"]))
        self.models.append(USState(key_name="SD",abbreviation="SD",fullname="South Dakota",primary_display_text="South Dakota",display_text=["SD","South Dakota"]))
        self.models.append(USState(key_name="TN",abbreviation="TN",fullname="Tennessee",primary_display_text="Tennessee",display_text=["TN","Tennessee"]))
        self.models.append(USState(key_name="TX",abbreviation="TX",fullname="Texas",primary_display_text="Texas",display_text=["TX","Texas"]))
        self.models.append(USState(key_name="UT",abbreviation="UT",fullname="Utah",primary_display_text="Utah",display_text=["UT","Utah"]))
        self.models.append(USState(key_name="VT",abbreviation="VT",fullname="Vermont",primary_display_text="Vermont",display_text=["VT","Vermont"]))
        self.models.append(USState(key_name="VA",abbreviation="VA",fullname="Virginia",primary_display_text="Virginia",display_text=["VA","Virginia"]))
        self.models.append(USState(key_name="WA",abbreviation="WA",fullname="Washington",primary_display_text="Washington",display_text=["WA","Washington"]))
        self.models.append(USState(key_name="WV",abbreviation="WV",fullname="West Virginia",primary_display_text="West Virginia",display_text=["WV","West Virginia"]))
        self.models.append(USState(key_name="WI",abbreviation="WI",fullname="Wisconsin",primary_display_text="Wisconsin",display_text=["WI","Wisconsin"]))
        self.models.append(USState(key_name="WY",abbreviation="WY",fullname="Wyoming",primary_display_text="Wyoming",display_text=["WY","Wyoming"]))
    
        return self.models

    def clean(self):
        
        self.models.append(self.P.get_by_key_name('USState'))
        
        return self.models