#!/usr/bin/env python
# coding: utf-8

# # Analysis of Housing, Technology, and Social Conditions in Urbana, IL and Champaign County
# ## Import necessary libraries

# In[1]:


# import necessary libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd # library for data structures and operations
import numpy as np # library for scientific computing
import matplotlib.pyplot as plt # library for plotting
import seaborn as sns # library for plotting
from plotnine import * # the following libraries are for interactive plotly graphics
import plotly
from plotly import graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import tools
import plotly.figure_factory as ff
# Also install ggplot by doing any of the following:
    # $ pip install -U ggplot
    # or
    # $ conda install -c conda-forge ggplot
    # or
    # pip install git+https://github.com/yhat/ggplot.git


# ## Import datasets

# In[2]:


# Import all of the datasets
# adjust file path to whatever your file path is

housing_df = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Housing/ACS_5Y_2018_Housing_Characteristics/ACS_5Y_2018_data_with_overlays.csv')
computer_no_phone = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Technology/CDC_Households_with_Computer_No_Phone/Percent_Computer_No_Phone_County_2013-2017.csv')
no_internet = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Technology/CDC_Households_with_No_Internet_Access/Percent_No_Internet_County_2013-2017.csv')
only_smartphone = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Technology/CDC_Households_with_Only_Smartphones/Percent_HHs_Only_Smartphone_County_2013-2017.csv')
smartphone = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Technology/CDC_Households_with_Smartphones/Percent_Smartphone_County_2013-2017.csv')
social_df = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Community/ACS_5Y_2018_Social_Characteristics/ACS_5Y_2018_data_with_overlays_social.csv')


# # Analysis of Selected Housing Characteristics
# ## Census Bureau American Community Service (ACS) 2018 5-Year Estimates, Table DP04

# In[3]:


housing_df.head()


# In[4]:


# rename the geographies
housing_df.GEO_NAME[2]='Champaign County'
housing_df.GEO_NAME[3]='Urbana'


# In[5]:


# Housing Stock

# create a dictionary of races to compare across geographies
# also create a key for labels to identify the geography
data = {
    "detached": housing_df.one_unit_detached.to_list(),
    "one": housing_df.one_unit_attached.to_list(),
    "two": housing_df.two_units.to_list(),
    "three": housing_df.three_or_four_units.to_list(),
    "five": housing_df.five_to_nine_units.to_list(),
    "ten": housing_df['10_to_19_units'].to_list(),
    "twenty": housing_df['20_or_more_units'].to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

# this will create an interactive graphic showing race by geography
# used a gray scale color scheme, however, this can be adjusted by changing
# the marker_color rgb value

fig = go.Figure(
    data=[
        go.Bar(
            name="One Unit Detached",
            x=data["labels"],
            y=data["detached"],
            offsetgroup=0,
            marker_color='rgb(260, 260, 260)'
        ),
        go.Bar(
            name="One Unit Attached",
            x=data["labels"],
            y=data["one"],
            offsetgroup=1,
            marker_color='rgb(50, 50, 50)'
        ),
        go.Bar(
            name="Two Units Attached",
            x=data["labels"],
            y=data["two"],
            offsetgroup=2,
            marker_color='rgb(120, 120, 120)'
        ),
        go.Bar(
            name="Three or Four Units Attached",
            x=data["labels"],
            y=data["three"],
            offsetgroup=3,
            marker_color='rgb(0, 0, 0)'
        ),
         go.Bar(
            name="Five to Nine Units Attached",
            x=data["labels"],
            y=data["five"],
            offsetgroup=4,
            marker_color='rgb(170, 170, 170)'
        ),
         go.Bar(
            name="Ten to Nineteen Units Attached",
            x=data["labels"],
            y=data["ten"],
            offsetgroup=5,
            marker_color='rgb(30, 30, 30)'
        ),
         go.Bar(
            name="Twenty or More Units Attached",
            x=data["labels"],
            y=data["twenty"],
            offsetgroup=6,
            marker_color='rgb(240, 240, 240)'
        ),
    ],
    layout=go.Layout(
        title="Housing Stock by Geography",
        yaxis_title="Percent",
        xaxis_title="Geography"
    ),

)

# create an black border on the bars to improve visual clarity
fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)

# to ensure that the interactive graphic appears in nbviewer
fig.show("notebook")

# to save the image as html, uncomment the following and change the html name:
# fig.write_html("figure_name.html")

# NOTE: all interactive plots similar to this won't include comments since the same pattern
# is followed. However, I will add comments for plots that involve different code


# Urbana's population occupies less one unit detached housing structures, or what we would consider normal houses, than the other geographies listed. However, Urbana occupies more housing structures with twenty or more units attached, which would include large apartment buildings that students or young adults may occupy. 

# In[6]:


# Urbana Only Housing Stock
# Same data as before

# Donut Chart
labels = ['1 unit attached', 
          '2 units', '3-4 units', '5-9 units','10-19 units', '20 or more units','1 unit detached']
values = [housing_df['one_unit_attached'][3],
         housing_df['two_units'][3],housing_df['three_or_four_units'][3],
         housing_df['five_to_nine_units'][3],housing_df['10_to_19_units'][3],housing_df['20_or_more_units'][3],housing_df['one_unit_detached'][3]]
#colors
colors = ["#56B4E9", "#E69F00", "#CC79A7", "#009E73", 
           "#F0E442", "#0072B2", "#D55E00"]
# Explosion: creates spaces between categories
# I decided not to use this, but you can uncomment the following comments related to "explode" to see what it does
# explode = (0.01,0.01,0.01,0.01,0.01,0.01,0.01)
fig, ax1 = plt.subplots(figsize = (10,7))
wedges, texts, autotexts = ax1.pie(values, colors = colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85) #, explode = explode)
ax1.legend(wedges, labels,
          title="Housing Stock Type",
          loc="upper left",
          bbox_to_anchor=(1, 0, 0.5, 1))
#draw circle
center_circle = plt.Circle((0,0),0.60,fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
#plt.legend()
ax1.axis('equal')  
plt.tight_layout()
# plt.savefig('housing_stock_breakdown.png')
plt.show()


# In[7]:


# Housing Construction Year
data = {
    "1939": housing_df['1939_earlier'].to_list(),
    "1940": housing_df['1940-1949_unit'].to_list(),
    "1950":  housing_df['1950-1959_unit'].to_list(),
    "1960": housing_df['1960-1969_unit'].to_list(),
    "1970":  housing_df['1970-1979_unit'].to_list(),
    "1980":  housing_df['1980-1989_unit'].to_list(),
    "1990":  housing_df['1990-1999_unit'].to_list(),
    "2000":  housing_df['2000-2009_unit'].to_list(),
    "2010":  housing_df['2010-2013_unit'].to_list(),
    "2014":  housing_df['2014_unit'].to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

fig = go.Figure(
    data=[
        go.Bar(
            name="1939 or earlier",
            x=data["labels"],
            y=data["1939"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="1940-1949",
            x=data["labels"],
            y=data["1940"],
            offsetgroup=1,
            marker_color='rgb(90, 50, 0)'
        ),
        go.Bar(
            name="1950-1959",
            x=data["labels"],
            y=data["1950"],
            offsetgroup=2,
            marker_color='rgb(140, 81, 10)'
        ),
        go.Bar(
            name="1960-1969",
            x=data["labels"],
            y=data["1960"],
            offsetgroup=3,
            marker_color='rgb(191, 129, 45)'
        ),
        go.Bar(
            name="1970-1979",
            x=data["labels"],
            y=data["1970"],
            offsetgroup=4,
            marker_color='rgb(223, 194, 125)'
        ),
         go.Bar(
            name="1980-1989",
            x=data["labels"],
            y=data["1980"],
            offsetgroup=5,
            marker_color='rgb(246, 232, 195)'
        ),
         go.Bar(
            name="1990-1999",
            x=data["labels"],
            y=data["1990"],
            offsetgroup=6,
            marker_color='rgb(245, 245, 245)'
        ),
        
         go.Bar(
            name="1990-1999",
            x=data["labels"],
            y=data["1990"],
            offsetgroup=7,
            marker_color='rgb(199, 234, 229)'
        ),
         go.Bar(
            name="2000-2009",
            x=data["labels"],
            y=data["2000"],
            offsetgroup=8,
            marker_color='rgb(128, 205, 193)'
        ),
         go.Bar(
            name="2010-2013",
            x=data["labels"],
            y=data["2010"],
            offsetgroup=9,
            marker_color='rgb(53, 151, 143)'
        ),  
         go.Bar(
            name="2014 or Later",
            x=data["labels"],
            y=data["2014"],
            offsetgroup=10,
            marker_color='rgb(1, 102, 94)'
        ),
    ],
    layout=go.Layout(
        title="Housing Construction Year by Geography",
        yaxis_title="Percent",
        xaxis_title="Geography"
    ),

)

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)

fig.show("notebook")


# The construction year of housing structures in Urbana is relatively similar to that of Champaign County, indicating that there isn't anything unique about Urbana's housing construction compared to the nearby area. Around 13% of housing units were built before 1939, 16% were built 1970-1979, and about 16% were built from 2000-2009. The construction years of 1970-1979 and 2000-2009 align with times of incredible economic growth during the years of heavy inflation in the 70s and the housing bubble of the 2000s. 

# In[8]:


# Urbana Only Housing Construction Year
labels = ['1939 or Earlier','1940-1949', '1950-1959', '1960-1969','1970-1979', '1980-1989','1990-1999',
         '2000-2009','2010-2013','2014 or Later']
values = [housing_df['1939_earlier'][3],
         housing_df['1940-1949_unit'][3],housing_df['1950-1959_unit'][3],
         housing_df['1960-1969_unit'][3],housing_df['1970-1979_unit'][3],
         housing_df['1980-1989_unit'][3],housing_df['1990-1999_unit'][3],
         housing_df['2000-2009_unit'][3],housing_df['2010-2013_unit'][3],
         housing_df['2014_unit'][3]]

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(14,7))
ax1 = sns.barplot(labels,values,palette="GnBu_d",alpha = 0.9)
for p in ax1.patches:
    ax1.annotate(format(p.get_height(), '.1f'),
               (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', 
               xytext = (0, 10), textcoords = 'offset points')
right_side = ax1.spines["right"]
right_side.set_visible(False) 
top_side = ax1.spines["top"]
top_side.set_visible(False) 
left_side = ax1.spines["left"]
left_side.set_visible(False) 
ax.set_ylabel('Percent (%)')
ax.set_xlabel('Construction Year')
# plt.savefig('housing_construction_year.png')
plt.show()


# In[9]:


# Number of Rooms by Geography
data = {
    "one": housing_df['one_room'].to_list(),
    "two": housing_df['two_rooms'].to_list(),
    "three":  housing_df['three_rooms'].to_list(),
    "four": housing_df['four_rooms'].to_list(),
    "five":  housing_df['five_rooms'].to_list(),
    "six":  housing_df['six_rooms'].to_list(),
    "seven":  housing_df['seven_rooms'].to_list(),
    "eight":  housing_df['eight_rooms'].to_list(),
    "nine":  housing_df['nine_more_rooms'].to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

fig = go.Figure(
    data=[
        go.Bar(
            name="1 room",
            x=data["labels"],
            y=data["one"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="2 rooms",
            x=data["labels"],
            y=data["two"],
            offsetgroup=1,
            marker_color='rgb(90, 50, 0)'
        ),
        go.Bar(
            name="3 rooms",
            x=data["labels"],
            y=data["three"],
            offsetgroup=2,
            marker_color='rgb(140, 81, 10)'
        ),
        go.Bar(
            name="4 rooms",
            x=data["labels"],
            y=data["four"],
            offsetgroup=3,
            marker_color='rgb(191, 129, 45)'
        ),
        go.Bar(
            name="5 rooms",
            x=data["labels"],
            y=data["five"],
            offsetgroup=4,
            marker_color='rgb(223, 194, 125)'
        ),
         go.Bar(
            name="6 rooms",
            x=data["labels"],
            y=data["six"],
            offsetgroup=5,
            marker_color='rgb(246, 232, 195)'
        ),
         go.Bar(
            name="7 rooms",
            x=data["labels"],
            y=data["seven"],
            offsetgroup=6,
            marker_color='rgb(245, 245, 245)'
        ),
        
         go.Bar(
            name="8 rooms",
            x=data["labels"],
            y=data["eight"],
            offsetgroup=7,
            marker_color='rgb(199, 234, 229)'
        ),
         go.Bar(
            name="9 rooms or more",
            x=data["labels"],
            y=data["nine"],
            offsetgroup=8,
            marker_color='rgb(128, 205, 193)'
        ),
    ],
    layout=go.Layout(
        title="Number of Rooms in Housing Unit",
        yaxis_title="Percent",
        xaxis_title="Geography"
    ),

)


fig.update_traces(opacity=0.8)
fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)

fig.show("notebook")


# Urbana has significantly more housing units with only one room compared to the United States and Illinois. This, again, is likely due to the need for more units to house university students, but it's unclear how much this population contributes to the overall statistic. 

# In[10]:


# Urbana Only: Number of Rooms in Housing Unit
labels = ['1 room', '2 rooms', '3 rooms', '4 rooms',
          '5 rooms', '6 rooms','7 rooms','8 rooms', '9 rooms or more']

values = [housing_df['one_room'][3], housing_df['two_rooms'][3],housing_df['three_rooms'][3],
         housing_df['four_rooms'][3],housing_df['five_rooms'][3],housing_df['six_rooms'][3],
          housing_df['seven_rooms'][3],housing_df['eight_rooms'][3],housing_df['nine_more_rooms'][3]]
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(14,7))
ax1 = sns.barplot(labels,values,palette="GnBu_d",alpha = 0.9)
for p in ax1.patches:
    ax1.annotate(format(p.get_height(), '.1f'),
               (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', 
               xytext = (0, 10), textcoords = 'offset points')
right_side = ax1.spines["right"]
right_side.set_visible(False) 
top_side = ax1.spines["top"]
top_side.set_visible(False) 
left_side = ax1.spines["left"]
left_side.set_visible(False) 
ax.set_ylabel('Percent (%)')
ax.set_xlabel('Number of Rooms')
# plt.savefig('number_of_rooms.png')
plt.show()


# In[11]:


# Number of Vehicles per Housing Unit
data = {
    "none": housing_df['no_vehicles'].to_list(),
    "one": housing_df['one_vehicle'].to_list(),
    "two":  housing_df['two_vehicles'].to_list(),
    "three": housing_df['three_more_vehicles'].to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

fig = go.Figure(
    data=[
        go.Bar(
            name="No vehicle",
            x=data["labels"],
            y=data["none"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="1 vehicle",
            x=data["labels"],
            y=data["one"],
            offsetgroup=1,
            marker_color='rgb(90, 50, 0)'
        ),
        go.Bar(
            name="2 vehicles",
            x=data["labels"],
            y=data["two"],
            offsetgroup=2,
            marker_color='rgb(140, 81, 10)'
        ),
        go.Bar(
            name="3 or more vehicles",
            x=data["labels"],
            y=data["three"],
            offsetgroup=3,
            marker_color='rgb(191, 129, 45)'
        ),
    ],
    layout=go.Layout(
        title="Vehicles for Occupied Housing Units",
        yaxis_title="Percent",
        xaxis_title="Geography"
    ),

)


fig.update_traces(opacity=0.8)
fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)

fig.show("notebook")


# There are more people in Urbana with no vehicle and one vehicle compared to the other areas listed. This suggests the idea that there are less families or/and more young families. It could also suggest that vehicles are less necessary in Urbana due to better access to alternate means of transportation.

# In[12]:


# Urbana Only: Number of Vehicles
labels = ['No vehicle','1 vehicle', '2 vehicles', '3 vehicles or more']

values = [housing_df['no_vehicles'][3], housing_df['one_vehicle'][3], housing_df['two_vehicles'][3],housing_df['three_more_vehicles'][3]]

sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(14,7))
ax1 = sns.barplot(labels,values,palette="GnBu_d", alpha = 0.9)

for p in ax1.patches:
    ax1.annotate(format(p.get_height(), '.1f'),
               (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', 
               xytext = (0, 10), textcoords = 'offset points')
    
right_side = ax1.spines["right"]
right_side.set_visible(False) 
top_side = ax1.spines["top"]
top_side.set_visible(False) 
left_side = ax1.spines["left"]
left_side.set_visible(False) 
ax.set_ylabel('Percent (%)')
ax.set_xlabel('')
ax.set_ylim(0,50)
# plt.savefig('number_of_vehicles.png')
plt.show()


# # Technology
# ## Collected from CDC National Environmental Public Health Tracking Network <https://ephtracking.cdc.gov/DataExplorer/#/>
# ### Note: Data was collected on a county-by-county level, however, data can be collected on a Census track level. 

# In[13]:


# Households with a computer but no phone
computer_no_phone.head()


# In[14]:


# Values right now are as strings which we don't want. 
# We want the values as floats
print(type(computer_no_phone.Value[0]))


# In[15]:


# get rid of percentage sign on string and turn value into a float
# define a new column called percents
computer_no_phone['percents'] = computer_no_phone['Value'].str.replace('%', '').astype('float')
computer_no_phone.head()


# In[16]:


# Choose a colorscale: one I chose is blue scale, but you can adjust this
colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
# Choose the range of values for your color scale to start and end
endpts = list(np.linspace(15, 46, len(colorscale) - 1))

# Create the interactive map
fig = ff.create_choropleth(fips=computer_no_phone.countyFIPS, # Put 5-digit FIPs code
                           scope=['Illinois'], # Choose area for the map. In our case, IL
                           binning_endpoints=endpts, # Range of bins
                           colorscale=colorscale, # Blue colorscale defined earlier
                           values=computer_no_phone.percents, # Values for plotting
                           title='IL Households With a Computer But No Phone', 
                           legend_title='% Households')
fig.layout.template = None
# fig.write_html("computer_no_phone.html") # save interactive map as html
fig.show("notebook") 


# 35% of households in Champaign County have a computer but no phone. This is a relatively high percentage compared to the rest of the state.

# In[17]:


# No internet
no_internet.head()


# In[18]:


# get rid of percentage sign on string and turn value into a float
# define a new column called percents
no_internet['percents'] = no_internet['Value'].str.replace('%', '').astype('float')
no_internet.head()


# In[19]:


colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(3, 55, len(colorscale) - 1))

fig = ff.create_choropleth(fips=no_internet.countyFIPS, 
                           scope=['Illinois'],
                           binning_endpoints=endpts,
                           colorscale=colorscale,
                           values=no_internet.percents, 
                           title='IL Households with No Internet', 
                           legend_title='% Households')
fig.layout.template = None
# fig.write_html("households_with_no_internet.html")
fig.show('notebook')


# Champaign County has 13% of households with no internet. This is a relatively low percentage compared to the rest of the state, especially compared to the southern tip of Illinois that has over 50% of households having no internet. 

# In[20]:


# Percentage of Households with Only Smartphones
only_smartphone.head()


# In[21]:


# get rid of percentage sign on string and turn value into a float
# define a new column called percents
only_smartphone['percents'] = only_smartphone['Value'].str.replace('%', '').astype('float')
only_smartphone.head()


# In[22]:


colorscale = ["#f7fbff","#deebf7","#d2e3f3","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(0, 12, len(colorscale) - 1))

fig = ff.create_choropleth(fips=only_smartphone.countyFIPS, 
                           scope=['Illinois'],
                           binning_endpoints=endpts,
                           colorscale=colorscale,
                           values=only_smartphone.percents, 
                           title='IL Households with Smartphone but No Other Device', 
                           legend_title='% Households')
fig.layout.template = None
# fig.write_html("house_with_only_smart_phone.html")
fig.show("notebook")


# Only 3.2% of Champaign County has a smartphone but no other device. This is a relatively low percentage which is encouraging because it implies that most of Champaign County has access to more devices than just a smartphone.

# In[23]:


# Households with smartphones
smartphone.head()


# In[24]:


# There are 2 columns that need to be deleted: Data Comment and Unnamed
smartphone = smartphone.drop(['Data Comment', 'Unnamed: 7'], axis=1)
# Add percents column
smartphone['percents'] = smartphone['Value'].str.replace('%', '').astype('float')
smartphone.head()


# In[25]:


colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(40, 85, len(colorscale) - 1))

fig = ff.create_choropleth(fips=smartphone.countyFIPS, 
                           scope=['Illinois'],
                           binning_endpoints=endpts,
                           colorscale=colorscale,
                           values=smartphone.percents, 
                           title='IL Households with a Smartphone', 
                           legend_title='% Households')
fig.layout.template = None
# fig.write_html("house_with_smart_phone.html")
fig.show("notebook")


# # Social Characteristics
# ## Census Bureau American Community Survey 2014-2018 5-Year Estimates, Table DP02

# In[26]:


social_df.head()


# In[27]:


# Rename geographies
social_df.GEO_NAME[2] = "Champaign County"
social_df.GEO_NAME[3] = "Urbana"


# In[28]:


ggplot(aes(x="GEO_NAME", weight="ave_hh_size"), social_df) + geom_bar(alpha = 0.8) +    ylim(0,3)+ labs(title= "Average Household Size by Geography",
                      y="Average Household Size", x = "Geography")


# Urbana's average household size is lower than the other geographies. It doesn't appear to be significantly different than Champaign County's average household size, however, indicating that it is consistent with the nearby area.

# In[29]:


# Place of Birth

data = {
    "native": social_df.native_pob.to_list(),
    "foreign": social_df.foreign_pob.to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

fig = go.Figure(
    data=[
        go.Bar(
            name="Native",
            x=data["labels"],
            y=data["native"],
            offsetgroup=0,
            marker_color='rgb(200, 200, 200)'
        ),
        go.Bar(
            name="Foreign",
            x=data["labels"],
            y=data["foreign"],
            offsetgroup=1,
            marker_color='rgb(100, 100, 100)'
        ),
    ],
    layout=go.Layout(
        title="Native and Foreign Place of Birth Breakdown by Geography",
        yaxis_title="Percent of Population",
        xaxis_title="Geography"
    ),

)

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)


fig.show("notebook")


# Urbana has more foreign-born individuals than the United States, Illinois, and Champaign County. About 20% of Urbana's population is foreign-born, while Champaign County's population is only 12% foreign born. This could be attributable to the large immigrant population in Urbana and foreign university population.

# In[30]:


# Language Spoken at Home

data = {
    "english": social_df.home_english_only.to_list(),
    "other": social_df.home_other_lang.to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

fig = go.Figure(
    data=[
        go.Bar(
            name="English",
            x=data["labels"],
            y=data["english"],
            offsetgroup=0,
            marker_color='rgb(200, 200, 200)'
        ),
        go.Bar(
            name="Other",
            x=data["labels"],
            y=data["other"],
            offsetgroup=1,
            marker_color='rgb(100, 100, 100)'
        ),
    ],
    layout=go.Layout(
        title="Language Spoken at Home by Geography",
        yaxis_title="Percent of Population",
        xaxis_title="Geography"
    ),

)



fig.show("notebook")


# There are less people in Urbana that speak English than in the other regions listed, however, it doesn't appear to be significantly different than the percentage of English speakers in Illinois. Compared to Champaign County, however, Urbana does have much more people who don't speak English at home.

# In[31]:


# Non-English Languages spoken at home
data = {
    "spanish": social_df.home_spanish.to_list(),
    "indo": social_df.home_indo_euro.to_list(),
    "asian": social_df.home_asian.to_list(),
    "other": social_df.home_none_of_above.to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

fig = go.Figure(
    data=[
        go.Bar(
            name="Spanish",
            x=data["labels"],
            y=data["spanish"],
            offsetgroup=0,
            marker_color='rgb(170, 170, 170)'
        ),
        go.Bar(
            name="Other Indo-European",
            x=data["labels"],
            y=data["indo"],
            offsetgroup=1,
            marker_color='rgb(70, 70, 70)'
        ),
        go.Bar(
            name="Asian/Pacific Islander",
            x=data["labels"],
            y=data["asian"],
            offsetgroup=2,
            marker_color='rgb(0, 0, 0)'
        ),
        go.Bar(
            name="Other",
            x=data["labels"],
            y=data["other"],
            offsetgroup=3,
            marker_color='rgb(240, 240, 240)'
        )
    ],
    layout=go.Layout(
        title="Breakdown of Non-English Languages Spoken at Home by Language and Geography" ,
        yaxis_title="Percent of Population",
        xaxis_title="Geography"
    ),

)
fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.02)','paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.8)


fig.show("notebook")


# There are significantly more people speaking Asian languages in Urbana compared to other geographic regions. This makes sense because there is a large Asian immigrant population in Urbana. This also likely explains why the percentages of households speaking Spanish and other Indo-European languages are lower. 

# In[ ]:




