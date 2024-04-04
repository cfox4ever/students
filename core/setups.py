


STATES = (('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
           ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), 
           ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'),
            ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
             ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'),
              ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), 
              ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), 
              ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
               ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
                ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'),
                 ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), 
                 ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'),
                  ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), 
                  ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
                   ('WI', 'Wisconsin'), ('WY', 'Wyoming'))
ChoiceRole =  ( 
    ("Resident Or Family Member","Resident Or Family Member"),
    ("maintstaff", "Maintenance-Staff"), 
    ("maintsupervisor", "Maintenance-Supervisor"), 
    ("maintdirector", "Maintenance-Director"), 
    ("it", "IT"), 
    ("sec", "Secuirty"), 
    ("hkDirctor", "HouseKeeping-Director"), 
    ("hkstaff", "HouseKeeping-Staff"), 
    ("accounting", "Accounting"), 
    ("activity", "Activity"),
    ("nursing", "Nursing"),      
    ("exe", "Executive-Director"), 
    ("corp", "Corprate"), 
    )  
status     = (('Pending Approval','Pending Approval'),('Active','Active'),
                  ('No Longer Active','No Longer Active'))
PR = (('Critical','Critical'),('High','High'),('Medium','Medium'),('Low','Low'))
WO_TYPE = (('Electric','Electric'),('HVAC','HVAC'),('Paint','Paint'),('Plumbing','Plumbing'),
                ('Misc.','Misc.'),('Life Saftey','Life Saftey'),('House Keeping','House Keeping'))
STATUS  = (('Open','Open'),('In-Progress','In-Progress'),('Completed','Completed'))
locationStatus = (('Active','Active'),('Inactive','Inactive'))