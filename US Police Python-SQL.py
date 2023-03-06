# -*- coding: utf-8 -*-

# -- Sheet --

# # The Real Threat Level Project
# 
# <br>
# 
# #### This project pretends to observe and measure the real level of threat that leads US police officer's actions to the extreme. Also compare state's gun confrontation according to their level of firearm's trade.
# 
# <br>
# 
# 
# This is a public Dataset, and was collected by the [MPV](https://mappingpoliceviolence.org/) and [ATF, Bureau of Alcohol, Tobacco, Firearms and Explosives](https://www.atf.gov/).
# 
# <br>
# 
# ### Data Collection
# 
# <br>
# 
# "Mapping Police Violence sources data from a number of sources. While we strive to employ official data sources from local and state government agencies, we believe it is important to continue collecting data from publicly-accessible media sources. This allows us to identify gaps in government data, and further triangulate and validate the data.
# 
# After conducting an internal comparison of different news aggregators, we decided to use Google News as our primary method for detecting news media mentions of police violence. We are continuing to develop and improve our own automated systems to filter out irrelevant news articles, maximize the comprehensiveness of the articles we do detect, and reduce potential human coding errors...
# 
# <br>
# 
# ...Our previous methodology primarily sourced data from Fatal Encounters, The Washington Post, publicly-accessible media sources, and official data sources from local and state agencies required to report this data (e.g., California Department of Justice)."
# 
# ### Questions:
# 
# <br>
# 
# 1. What are the most deadly states?
# 2. Why are the executions high for those states?
# 3. What community is more affected?
#    
# <br>
# 
# ### Task:
# 
# <br>
# 
#  What recommendations to mitigate such a number of deaths?


# SQL (bigquery) request
df_5 = None # TODO: execute the following query:
# -- Looking at table Schema.
# 
# SELECT * 
# FROM voltaic-mantra-364014.us_police.INFORMATION_SCHEMA.COLUMNS


# SQL (bigquery) request
df_1 = None # TODO: execute the following query:
# select * from voltaic-mantra-364014.us_police.state where armed_people is not null;


# # Reshapping Data


# -- Rename columns.
# 
# `ALTER TABLE voltaic-mantra-364014.us_police.state 
#  rename column __Black_people_killed_2014 to black_people_killed_2014, 
#  rename column __Black_people_killed_2015 to black_people_killed_2015, 
#  rename column __Black_people_killed_2016 to black_people_killed_2016, 
#  rename column __Black_people_killed_2017 to black_people_killed_2017, 
# rename column __Black_people_killed_2018 to black_people_killed_2018, 
# rename column __Black_people_killed_2019 to black_people_killed_2019, 
# rename column __Black_people_killed_2020 to black_people_killed_2020, 
# rename column __Black_people_killed_2021 to black_people_killed_2021, 
# rename column __Black_people_killed_2022 to black_people_killed_2022, 
# rename column __White_people_killed_2013 to white_people_killed_2013, 
# rename column __White_people_killed_2014 to white_people_killed_2014, 
# rename column __White_people_killed_2015 to white_people_killed_2015, 
# rename column __White_people_killed_2016 to white_people_killed_2016, 
# rename column __White_people_killed_2017 to white_people_killed_2017, 
# rename column __White_people_killed_2018 to white_people_killed_2018,
# rename column __White_people_killed_2019 to white_people_killed_2019,
# rename column __White_people_killed_2020 to white_people_killed_2020,
# rename column __White_people_killed_2021 to white_people_killed_2021,
# rename column __White_people_killed_2022 to white_people_killed_2022,
# rename column __People_Killed_2013 to people_killed_2013,
# rename column __People_Killed_2014 to people_killed_2014,
# rename column __People_Killed_2015 to people_killed_2015,
# rename column __People_Killed_2016 to people_killed_2016,
# rename column __People_Killed_2017 to people_killed_2017,
# rename column __People_Killed_2018 to people_killed_2018,
# rename column __People_Killed_2019 to people_killed_2019,
# rename column __People_Killed_2020 to people_killed_2020,
# rename column __People_Killed_2021 to people_killed_2021,
# rename column __People_Killed_2022 to people_killed_2022;`


# -- rename columns.
# 
# `ALTER TABLE voltaic-mantra-364014.us_police.state
# rename column _2013_Killings_per_Population to killings_per_population_2013,
# rename column _2014_Killings_per_Population to killings_per_population_2014,
# rename column _2015_Killings_per_Population to killings_per_population_2015,
# rename column _2016_Killings_per_Population to killings_per_population_2016,
# rename column _2017_Killings_per_Population to killings_per_population_2017,
# rename column _2018_Killings_per_Population to killings_per_population_2018,
# rename column _2019_Killings_per_Population to killings_per_population_2019,
# rename column _2020_Killings_per_Population to killings_per_population_2020,
# rename column _2021_Killings_per_Population to killings_per_population_2021,
# rename column _2022_Killings_per_Population to killings_per_population_2022;`


# -- Creating a table view containing killings per year at each US state. Converting from wide to long.
# 
# `create view voltaic-mantra-364014.us_police.killings_per_state_and_year as
# select State_Full, REPLACE(year1, 'people_killed_', '') year, killed_per_year
# from 
#     (select State_Full, people_killed_2013, people_killed_2014, people_killed_2015, people_killed_2016, people_killed_2017, people_killed_2018, people_killed_2019, people_killed_2020, people_killed_2021, people_killed_2022 from voltaic-mantra-364014.us_police.state`
#     
#         ) x
# `unpivot
#     (killed_per_year for year1  in
#         (people_killed_2013, people_killed_2014, people_killed_2015, people_killed_2016, people_killed_2017, people_killed_2018, people_killed_2019, people_killed_2020, people_killed_2021, people_killed_2022) 
# `
#     ) as unpvt


# -- Creating table view with unpivot to convert wide table into long table, and sumarize deaths by the police for armed people.
# 
# `create view voltaic-mantra-364014.us_police.armed_people_killed as
# select State_Full, REPLACE(year1, 'Allegedly_Armed_People_Killed_by_Police_', '') year, armed_people_killed_per_year
# from 
#     (select State_Full, Allegedly_Armed_People_Killed_by_Police_2013, Allegedly_Armed_People_Killed_by_Police_2014, Allegedly_Armed_People_Killed_by_Police_2015, Allegedly_Armed_People_Killed_by_Police_2016, Allegedly_Armed_People_Killed_by_Police_2017, Allegedly_Armed_People_Killed_by_Police_2018, Allegedly_Armed_People_Killed_by_Police_2019, Allegedly_Armed_People_Killed_by_Police_2020, Allegedly_Armed_People_Killed_by_Police_2021, Allegedly_Armed_People_Killed_by_Police_2022 from voltaic-mantra-364014.us_police.state`
#     
#         ) x
# `unpivot
#     (armed_people_killed_per_year for year1  in
#         (Allegedly_Armed_People_Killed_by_Police_2013, Allegedly_Armed_People_Killed_by_Police_2014, Allegedly_Armed_People_Killed_by_Police_2015, Allegedly_Armed_People_Killed_by_Police_2016, Allegedly_Armed_People_Killed_by_Police_2017, Allegedly_Armed_People_Killed_by_Police_2018, Allegedly_Armed_People_Killed_by_Police_2019, Allegedly_Armed_People_Killed_by_Police_2020, Allegedly_Armed_People_Killed_by_Police_2021, Allegedly_Armed_People_Killed_by_Police_2022)` 
# 
#     ) as unpvt


# ### *Q) 1. What are the most deadly states?*


# SQL (bigquery) request
df_19 = None # TODO: execute the following query:
# -- View of overall deaths per state.
# 
# select State_Full, sum(killed_per_year) people_killed_by_police 
# from voltaic-mantra-364014.us_police.killings_per_state_and_year 
# where State_Full is not null 
# group by State_Full 
# order by people_killed_by_police desc


from lets_plot import * 
ggplot() + \
geom_bar(aes(x="State_Full", y="people_killed_by_police"), data=df_19, sampling="none" if df_19.size < 50 else sampling_pick(n=50), color="#f9c1ae", fill="#f9c1ae", stat="identity") + \
ggtitle("Most deadly states")  +\
 scale_x_discrete() +\
ylab("people killed by police") + \
ggsize(900, 600)

# ### Observations:
# <br>
# 
# California, Texas and Florida had the most overall death rates.


# SQL (bigquery) request
df_11 = None # TODO: execute the following query:
# -- Armed people killed per state and per year.
# 
# select * from voltaic-mantra-364014.us_police.armed_people_killed where (State_Full is not null) order by year asc


from lets_plot import * 
ggplot() + \
geom_line(aes(x="year", y="armed_people_killed_per_year", color="State_Full"), data=df_11, sampling="none" if df_11.size < 2500 else sampling_systematic(n=2500)) + \
ggtitle("Armed people killed per state and year")  +\
ylab("armed people killed per year") + \
ggsize(900, 500)

# SQL (bigquery) request
df_10 = None # TODO: execute the following query:
# -- Loading dataset related to police department reports.
# 
# select * from voltaic-mantra-364014.us_police.PD where State is not null 


# SQL (bigquery) request
df_8 = None # TODO: execute the following query:
# -- Armed people killed by police from 2013-2022.
# 
# 
# select State, sum(Allegedly_Armed_People_Killed_by_Police) victim_armed from voltaic-mantra-364014.us_police.PD where (State !='All') and (State !='100 Cities') group by State order by victim_armed desc


# ### Observations:
# <br>
# California, Texas, Arizona, Nevada and Florida had the most armed people killed by police from 2013 to 2022.


%%html
    <div class='tableauPlaceholder' id='viz1677922178784' style='position: relative'><noscript><a href='#'><img alt='Distributions of 2022 People killed by Danger ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022Distributionsbydanger&#47;DistributionsbyDanger&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='USCrime2013-2022Distributionsbydanger&#47;DistributionsbyDanger' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022Distributionsbydanger&#47;DistributionsbyDanger&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1677922178784');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

# ### *Q) 2. Why are the executions high for those states?*


# ## 2020 AFMER Final Report Dataset
# 
# <br>
# 
# #### About Dataset:
# 
# <br>
# 
# This is a public dataset from ATF Bureau of Alcohol, Tobacco annual report.
# 
# <br>
# 
# ### The Bureau and Law Enforcement 
# 
# <b>
# 
# "ATF recognizes the role that firearms play in violent crimes and pursues an integrated regulatory and enforcement strategy. Investigative priorities focus on armed violent offenders and career criminals, narcotics traffickers, narco-terrorists, violent gangs, and domestic and international arms traffickers. Sections 924(c) and (e) of Title 18 of the United States Code provide mandatory and enhanced sentencing guidelines for armed career criminals and narcotics traffickers as well as other dangerous armed criminals.
# 
# ATF uses these statutes to target, investigate and recommend prosecution of these offenders to reduce the level of violent crime and to enhance public safety. ATF also strives to increase State and local awareness of available Federal prosecution under these statutes. To curb the illegal use of firearms and enforce the Federal firearms laws, ATF issues firearms licenses and conducts firearms licensee qualification and compliance inspections. In addition to aiding the enforcement of Federal requirements for gun purchases, compliance inspections of existing licensees focus on assisting law enforcement to identify and apprehend criminals who illegally purchase firearms.
# 
# The inspections also help improve the likelihood that crime gun traces will be successful, since industry operations investigators educate licensees in proper record keeping and business practices."


# SQL (bigquery) request
df_12 = None # TODO: execute the following query:
# -- Load dataset related to firearms sold in US per state and type in 2020.
# 
# select * from voltaic-mantra-364014.us_police.guns_sold


# SQL (bigquery) request
df_13 = None # TODO: execute the following query:
# -- Total of guns sales per state in 2020.
# 
# select APP_PREMISE_STATE, sum(Total) total 
# from voltaic-mantra-364014.us_police.guns_sold 
# where APP_PREMISE_STATE != 'Total states' 
# group by APP_PREMISE_STATE 
# order by total desc


from lets_plot import * 
ggplot() + \
geom_bar(aes(x="APP_PREMISE_STATE", y="total"), data=df_13, sampling="none" if df_13.size < 50 else sampling_pick(n=50), color="#8c86df", fill="#8c86df", stat="identity") + \
ggtitle("Guns Sales per state in 2020")  + \
ggsize(800, 500)

# SQL (bigquery) request
df_14 = None # TODO: execute the following query:
# -- Looking at states wich had more gun confrontations and ended with death victims by police in 2020.
# 
# select * 
# from voltaic-mantra-364014.us_police.armed_people_killed 
# where (State_Full is not null) and (year = '2020') 
# group by State_Full, armed_people_killed_per_year, year 
# order by armed_people_killed_per_year desc


from lets_plot import * 
ggplot() + \
geom_bar(aes(x="State_Full", y="armed_people_killed_per_year"), data=df_14, sampling="none" if df_14.size < 50 else sampling_pick(n=50), color="#d6eeaa", fill="#d6eeaa", stat="identity") + \
ggtitle("Armed people killed by police per state in 2020")  +\
ylab("armed people killed per year") + \
ggsize(900, 600)

# ### Observations:
# <br>
# In 2020, in between the 5th and 7th top states on guns sales, it's where we can find the biggest number of armed people killed by the police. Wich suggests causation between armed population and killing rate by police over armed individuals.


# SQL (bigquery) request
df_15 = None # TODO: execute the following query:
# -- Unarmed people killed per state in 9 years, from 2013-2022.
# 
# select State_Full, sum(Unarmed_Did_Not_Have_an_Actual_Weapon_People_Killed_by_Police) unarmed_people_killed_2013_2022 from voltaic-mantra-364014.us_police.state where State_Full is not null group by State_Full order by unarmed_people_killed_2013_2022 desc


# ### Observations:
# 
# <br>
# 
# Most States where occurred killings by police for unarmed individuals are also the states with overall high death rates by police kills.


%%html
    <div class='tableauPlaceholder' id='viz1677923256469' style='position: relative'><noscript><a href='#'><img alt='Violent Crimes Between 2013-2022 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022Distributionsbydanger&#47;ViolentCrimesRate2013-2022&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='USCrime2013-2022Distributionsbydanger&#47;ViolentCrimesRate2013-2022' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022Distributionsbydanger&#47;ViolentCrimesRate2013-2022&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='pt-BR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1677923256469');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

# SQL (bigquery) request
df_16 = None # TODO: execute the following query:
# select * from voltaic-mantra-364014.us_police.PD


# SQL (bigquery) request
df_17 = None # TODO: execute the following query:
# select State, sum(Violent_Crime_Rate) violent_crime_rate 
# from voltaic-mantra-364014.us_police.PD where State is not null and (State !='100 Cities') and (State !='All') 
# group by State 
# order by violent_crime_rate desc


from lets_plot import * 
ggplot() + \
geom_area(aes(x="State", y="violent_crime_rate"), data=df_17, sampling="none" if df_17.size < 2500 else sampling_systematic(n=2500), color="#c2c0de", fill="#c2c0de", stat="identity", position="identity") + \
ggtitle("Violent Crime per State")  + \
ggsize(900, 400)

# ### Observations:
# <br>
# Also states where violent crime rate is high are the states with most high deaths rate by police killings, and where firearms sales are also high.


# SQL (bigquery) request
df_25 = None # TODO: execute the following query:
# -- Look for most unprepared police departments for deaths of unarmed people from 2013-2022.
# 
# select Agency_responsible_for_death,Armed_Unarmed_Status, Alleged_Weapon__Source__WaPo_and_Review_of_Cases_Not_Included_in_WaPo_Database_,  Cause_of_death, COUNT(Cause_of_death) total_cause 
# from voltaic-mantra-364014.us_police.police 
# where Armed_Unarmed_Status = 'Unarmed/Did Not Have Actual Weapon' 
# group by Agency_responsible_for_death, Armed_Unarmed_Status, Alleged_Weapon__Source__WaPo_and_Review_of_Cases_Not_Included_in_WaPo_Database_, Cause_of_death 
# order by total_cause desc


%%html
    <div class='tableauPlaceholder' id='viz1677924156704' style='position: relative'><noscript><a href='#'><img alt='Deaths of people Killed by Police with symptoms of mental Ileness in 2022 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022Symptomsofmentalilness&#47;SymptomsofmentalIlness&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='USCrime2013-2022Symptomsofmentalilness&#47;SymptomsofmentalIlness' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022Symptomsofmentalilness&#47;SymptomsofmentalIlness&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='pt-BR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1677924156704');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

%%html
    <div class='tableauPlaceholder' id='viz1677923046825' style='position: relative'><noscript><a href='#'><img alt='Average Arrests Between 2013-2022 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022CrimesArrests&#47;AverageArrests2013-2022&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='USCrime2013-2022CrimesArrests&#47;AverageArrests2013-2022' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;US&#47;USCrime2013-2022CrimesArrests&#47;AverageArrests2013-2022&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='pt-BR' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1677923046825');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

# ### *Q) 3. What community is more affected?*


# SQL (bigquery) request
df_20 = None # TODO: execute the following query:
# 
# -- Comparishon between black individuals killed and white individuals killed wich were armed per state from 2013-2022.
# 
# select State_Full, black_people_killed_by_police, __White_people_killed, sum(armed_people) armed_and_killed 
# from voltaic-mantra-364014.us_police.state 
# where State_Full is not null and (State_Full != '2020 Census Data and Mapping Police Violence Data from 1/1/2013 - 2/11/2022. Census Source Link: https://data.census.gov/cedsci/table?q=Race%20and%20Ethnicity&g=0100000US%240400000&y=2020') 
# group by State_Full, black_people_killed_by_police, __White_people_killed 
# order by armed_and_killed desc


from lets_plot import * 
ggplot() + \
geom_point(aes(x="black_people_killed_by_police", y="__White_people_killed", color="State_Full"), data=df_20, sampling="none" if df_20.size < 2500 else sampling_systematic(n=2500)) + \
ggtitle("Both white and black people killed by police per state")  +\
xlab("black people killed by police") +\
ylab("White people killed") + \
ggsize(1000, 400)

# SQL (bigquery) request
df_21 = None # TODO: execute the following query:
# -- View vitcim's deaths that were armed per race and type of execution.
# 
# select State, Victim_s_race, Cause_of_death, COUNT(Armed_Unarmed_Status) armed 
# from voltaic-mantra-364014.us_police.police 
# where (Armed_Unarmed_Status = 'Allegedly armed') and (victim_s_race != 'Unknown race') 
# group by State, Victim_s_race, Cause_of_death 
# order by armed desc


from lets_plot import * 
ggplot() + \
geom_bar(aes(x="Victim_s_race", y="armed", color="Victim_s_race", fill="Victim_s_race"), data=df_21, sampling="none" if df_21.size < 50 else sampling_pick(n=50), stat="identity") + \
ggtitle("Victim's killed that were armed per Race")  + \
ggsize(800, 400)

# SQL (bigquery) request
df_23 = None # TODO: execute the following query:
# select * from voltaic-mantra-364014.us_police.police  limit 10


# SQL (bigquery) request
df_22 = None # TODO: execute the following query:
# -- View victim's unarmed killed per race and type of execution.
# 
# select State, Victim_s_race, Agency_responsible_for_death, Cause_of_death, COUNT(Armed_Unarmed_Status) unarmed, (Body_Camera__Source__WaPo_ ) body_camera
# from voltaic-mantra-364014.us_police.police 
# where (Armed_Unarmed_Status = 'Unarmed/Did Not Have Actual Weapon') and (victim_s_race != 'Unknown race') and (Body_Camera__Source__WaPo_ is not null) and (Body_Camera__Source__WaPo_ != 'Yes') and (Body_Camera__Source__WaPo_ !='no')
# group by State, Victim_s_race, Cause_of_death, Body_Camera__Source__WaPo_, Agency_responsible_for_death
# order by unarmed desc


from lets_plot import * 
ggplot() + \
geom_bar(aes(x="Victim_s_race", y="unarmed", color="Victim_s_race", fill="Victim_s_race"), data=df_22, sampling="none" if df_22.size < 50 else sampling_pick(n=50), stat="identity") + \
ggtitle("Victim's killed Unarmed per Race")  + \
ggsize(1000, 400)

from lets_plot import * 
ggplot() + \
geom_bar(aes(x="body_camera", y="unarmed"), data=df_22, sampling="none" if df_22.size < 50 else sampling_pick(n=50), color="#e64219", fill="#e64219", stat="identity") + \
ggtitle("Officer using Body Camera for Unarmed Deaths")  + \
ggsize(800, 400)

# SQL (bigquery) request
df_26 = None # TODO: execute the following query:
# select * 
# from voltaic-mantra-364014.us_police.state 
# where State_Full is not null and (State_Full != '2020 Census Data and Mapping Police Violence Data from 1/1/2013 - 2/11/2022. Census Source Link: https://data.census.gov/cedsci/table?q=Race%20and%20Ethnicity&g=0100000US%240400000&y=2020')


# SQL (bigquery) request
df_27 = None # TODO: execute the following query:
# -- View SUM() of race victim's by its population per state.
# 
# select State_Full, Black_Population, SUM(black_people_killed_by_police) total_blk_people_killed, White_Population, SUM(__White_people_killed) total_wt_killed, Hispanic_Population, SUM(__Hispanic_people_killed) total_latin_killed 
# from voltaic-mantra-364014.us_police.state 
# where State_Full != '2020 Census Data and Mapping Police Violence Data from 1/1/2013 - 2/11/2022. Census Source Link: https://data.census.gov/cedsci/table?q=Race%20and%20Ethnicity&g=0100000US%240400000&y=2020' 
# group by State_Full, Black_Population, White_Population, Hispanic_Population
# order by total_blk_people_killed desc


# #### *Calculating Percentage of deaths per Race by its population, We'll be focusing on 3 major dominant race type communities:*
# 
# <b>
# 
# 1. White individuals;
# 2. Black individuals;
# 3. Hispanic individuals.


# -- Create table view to store modificated valeu from Black_Population column type string. 
# 
# `create view voltaic-mantra-364014.us_police.percent_blk_pop as
# select State_Full, black_people_killed_by_police, Black_Population, REPLACE(Black_Population, '.', '') as blk_pop 
# from voltaic-mantra-364014.us_police.state 
# where State_Full != '2020 Census Data and Mapping Police Violence Data from 1/1/2013 - 2/11/2022. Census Source Link: https://data.census.gov/cedsci/table?q=Race%20and%20Ethnicity&g=0100000US%240400000&y=2020'`


# SQL (bigquery) request
df_30 = None # TODO: execute the following query:
# -- Result table view.
# 
# select * from voltaic-mantra-364014.us_police.percent_blk_pop


# -- Create table view with changed type of Black_Population to numeric and calculated percentage of black people killed per its population by state.
# 
# `create view voltaic-mantra-364014.us_police.blk_pct as
# SELECT State_Full, Black_Population, black_people_killed_by_police, SUM(black_people_killed_by_police)* 100/ROUND(CAST(SUBSTRING(blk_pop, 1, LENGTH(blk_pop)-1) as numeric)) AS percentage_blk_killed 
# from voltaic-mantra-364014.us_police.percent_blk_pop 
# group by State_Full, blk_pop, Black_Population, black_people_killed_by_police 
# order by percentage_blk_killed desc`


# SQL (bigquery) request
df_33 = None # TODO: execute the following query:
# -- Round percentage of black people killed per its population by state to 2 decimal.
# 
# select State_Full, Black_Population, black_people_killed_by_police, ROUND(percentage_blk_killed, 2) as pct_blk_killed 
# from voltaic-mantra-364014.us_police.blk_pct 
# order by pct_blk_killed desc


# SQL (bigquery) request
df_34 = None # TODO: execute the following query:
# -- Total percentage of black people killed per its total population from 2013 to 2022.
# 
# select SUM(ROUND(percentage_blk_killed, 2)) as total_pct_blk_killed_by_popultation from voltaic-mantra-364014.us_police.blk_pct 


# -- Create table view to store modificated values from White Population column type string. 
# 
# `create view voltaic-mantra-364014.us_police.percent_wt_pop as
# select State_Full, __White_people_killed, White_Population, REPLACE(White_Population, '.', '') as wt_pop 
# from voltaic-mantra-364014.us_police.state 
# where State_Full != '2020 Census Data and Mapping Police Violence Data from 1/1/2013 - 2/11/2022. Census Source Link: https://data.census.gov/cedsci/table?q=Race%20and%20Ethnicity&g=0100000US%240400000&y=2020'`


# -- Create table view with changed type of White_Population to numeric and calculated percentage of white people killed per its population by state.
# 
# `create view voltaic-mantra-364014.us_police.wt_pct as
# SELECT State_Full, White_Population, __White_people_killed, SUM(__White_people_killed)* 100/ROUND(CAST(SUBSTRING(wt_pop, 1, LENGTH(wt_pop)-1) as numeric)) AS percentage_wt_killed 
# from voltaic-mantra-364014.us_police.percent_wt_pop 
# group by State_Full, wt_pop, White_Population, __White_people_killed 
# order by percentage_wt_killed desc
# `


# SQL (bigquery) request
df_37 = None # TODO: execute the following query:
# -- Round percentage of white people killed per its population by state to 2 decimal from 2013 to 2022.
# 
# select State_Full, White_Population, __White_people_killed, ROUND(percentage_wt_killed, 2) as pct_wt_killed 
# from voltaic-mantra-364014.us_police.wt_pct 
# order by pct_wt_killed desc


# SQL (bigquery) request
df_38 = None # TODO: execute the following query:
# -- Total percentage of white people killed per its total population from 2013 to 2022.
# 
# select SUM(ROUND(percentage_wt_killed, 2)) as total_pct_wt_killed_by_popultation from voltaic-mantra-364014.us_police.wt_pct 


# -- Create table view to store modificated values from Hispanic Population column type string. 
# 
# `create view voltaic-mantra-364014.us_police.percent_latin_pop as
# select State_Full, __Hispanic_people_killed, Hispanic_Population, REPLACE(Hispanic_Population, '.', '') as latin_pop from voltaic-mantra-364014.us_police.state where State_Full != '2020 Census Data and Mapping Police Violence Data from 1/1/2013 - 2/11/2022. Census Source Link: https://data.census.gov/cedsci/table?q=Race%20and%20Ethnicity&g=0100000US%240400000&y=2020'`


# -- Create table view with changed type of Hispanic_Population to numeric and calculated percentage of white people killed per its population by state.
# 
# `create view voltaic-mantra-364014.us_police.latin_pct as
# SELECT State_Full, Hispanic_Population, __Hispanic_people_killed, SUM(__Hispanic_people_killed)* 100/ROUND(CAST(SUBSTRING(latin_pop, 1, LENGTH(latin_pop)-1) as numeric)) AS percentage_latin_killed from voltaic-mantra-364014.us_police.percent_latin_pop group by State_Full, latin_pop, Hispanic_Population, __Hispanic_people_killed order by percentage_latin_killed desc`


# SQL (bigquery) request
df_42 = None # TODO: execute the following query:
# select State_Full, Hispanic_Population, __Hispanic_people_killed, ROUND(percentage_latin_killed, 2) pct_latin_killed 
# from voltaic-mantra-364014.us_police.latin_pct 
# order by pct_latin_killed desc


# SQL (bigquery) request
df_41 = None # TODO: execute the following query:
# -- Total percentage of hispanic people killed per its total population from 2013 to 2022.
# 
# 
# select SUM(ROUND(percentage_latin_killed, 2)) as total_pct_latin_killed_by_popultation from voltaic-mantra-364014.us_police.latin_pct 


# 
# `create table voltaic-mantra-364014.us_police.percent_all_race_killed as
# SELECT black_individuals.percentage_blk_killed, white_individuals.percentage_wt_killed, hispanic_individuals.percentage_latin_killed
# FROM voltaic-mantra-364014.us_police.blk_pct black_individuals
# INNER JOIN voltaic-mantra-364014.us_police.wt_pct white_individuals
# ON black_individuals.State_Full = white_individuals.State_Full
# INNER JOIN voltaic-mantra-364014.us_police.latin_pct hispanic_individuals
# ON white_individuals.State_Full = hispanic_individuals.State_Full`


# SQL (bigquery) request
df_44 = None # TODO: execute the following query:
# select SUM(ROUND(percentage_blk_killed, 2)) Black, SUM(ROUND(percentage_wt_killed, 2)) White, SUM(ROUND(percentage_latin_killed,2)) Hispanic 
# from voltaic-mantra-364014.us_police.percent_all_race_killed


# SQL (bigquery) request
df_45 = None # TODO: execute the following query:
# -- Unpivot table for plot.
# 
# select Race, sum(round(Percent, 2)) Percentage
#     from 
#         (select percentage_blk_killed, percentage_wt_killed, percentage_latin_killed from voltaic-mantra-364014.us_police.percent_all_race_killed
#         
#             ) x
#     unpivot
#         (Percent for Race  in
#             (percentage_blk_killed, percentage_wt_killed, percentage_latin_killed) 
# 
#         ) as unpvt
#         group by Race, Percent 
#         order by Percent desc


from lets_plot import * 
ggplot() + \
geom_bar(aes(x="Race", y="Percentage", color="Race", fill="Race"), data=df_45, sampling="none" if df_45.size < 50 else sampling_pick(n=50), stat="identity") + \
ggtitle("Percentage of Deaths per Race by  its Population")  + \
ggsize(800, 400)

# ## *Analysis:*
# 
# <br>
# 
# ##### Descriptive:
# 
# <br>
# 
# What are the most deadly states?<p>
# 
# <br>
# 
#     1) California, Texas and Florida had the most overall death rates.
#     2) California, Texas, Arizona, Nevada and Florida had the most armed people killed by police from 2013 to 2022.
# 
# <br>
# 
# Why are the executions high for those states?<p>
# 
# <br>
# 
#     1) In 2020, in between the 5th and 7th top states on guns sales, it's where we can find the biggest number of armed people killed by the police. Wich suggests causation between armed population and killing rate by police over armed individuals.
#     2) Most States where occurred killings by police for unarmed individuals are also the states with overall high death rates by police kills.
#     3) Also states where violent crime rate is high are the states with most high deaths rate by police killings, and where firearms sales and reported as lost or stolen are also high.
# 
# <br>
# 
# What community is more affected?
# 
# <br>
# 
#     White individuals had the most deaths by the police wich were armed and also unarmed as it is the group that have more deaths by the police, although black individuals and its community have a big disparity in terms of deaths comparing to other ethnic groups by proportion of each population group that makes being the most affected group. 
# 
# <br>
# 
# ##### *Prescriptive:*
# 
# <br>
# 
# Mainly, there are three major factors that seem to strongly contribute to such mortality rate in critical states, which are: High rate for sales and stolen guns reported in high violent crime rate states, unprepared police behavior, especially by dealing with the task to secure, prevent and identify levels of threat to act accordly, and incapability to deal with mental health issues for compulsive arrests.<p>
# 
# <br>
# 
# Recommendations:
# 
# <br>
# 
# Review policy and restrictions for firearm trading and licencing for states with high rates of violent crime, which are also the states that reportedly have the most number of lost/thiefed firearms reported.
# 
# Provide extensive training recruitment in California, Georgia, Arizona, Florida, New York and Texas which were the states that executed more unarmed people and people with mental illness symptoms.
# 
# Review, investigate and provide right equipment such as BodyCams for **Los Angeles County Sheriff's Department, Los Angeles Police Department, Phoenix Police Department, Atlanta Police Department, Jacksonville Sheriff's Office, New York Police Department and California Highway Patrol**. Those were the police departments that had the most executions for unarmed people and for all the executions, there wasn't any BodyCam available and poorly fatal encounter reports. 
# 
# <br>


