#!/usr/bin/env python
# coding: utf-8

# # Analysis of Demographic, Economic, and Health Conditions in Urbana, IL and Champaign County
# 
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
# NOTE: You will likely need to adjust the file path to whatever your file path is.
    # This will likely include changing "/Users/haliegonzalez/" to whatever your file path is

demo_data = pd.read_excel('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Community/ACS_5Y_2018_data_with_overlays_demo_with_chart.xlsx')
ec_data = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Economy/ACS_5Y_2018_Economic_Characteristics/ACS_5Y_2018_data_with_overlays_ec.csv')
saipe_df = pd.read_excel('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Economy/SAIPE_Poverty_2009_to_2018.xlsx')
saipe_school_df = pd.read_excel('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Economy/SAIPES_School_District_2009_to_2018.xlsx')
benefits = pd.read_excel('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Health/Health Care Benefits - IHFS/Comprehensive Benefits.xlsx')
health_rankings = pd.read_excel('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Health/2020 County Health Rankings Illinois.xlsx', sheet_name = 'Data')
svi_df = pd.read_csv('/Users/haliegonzalez/Downloads/Comprehensive-Plan/data/Health/CDC Data - SVI/Illinois_Social_Vulnerability_Index/cdc_social_vulnerability_by_county.csv')


# #  Analysis of Selected Demographic Characteristics
# ## Data collected from Census Bureau American Community Survey (ACS) 2014-2018 5-Year Estimates; Table S0101 

# In[3]:


# demo_data dataframe has a lot of excess rows, so delete everything but the first 4 rows
demo_data = demo_data[0:4]


# In[4]:


## Percentage of Population by Race by Geography

# create a dictionary of races to compare across geographies
# also create a key for labels to identify the geography
data = {
    "white": demo_data.White.to_list(),
    "black": demo_data.Black.to_list(),
    "asian": demo_data.Asian.to_list(),
    "american_indian": demo_data['American Indian and Native Alaskan'].to_list(),
    "hawaiian": demo_data['Hawaiian or Pacific Islander'].to_list(),
    "other":demo_data.Other.to_list(),
    "two_or_more" :demo_data['Two or More Races'].to_list(),
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
            name="White",
            x=data["labels"],
            y=data["white"],
            offsetgroup=0,
            marker_color='rgb(200, 200, 200)'
        ),
        go.Bar(
            name="Black",
            x=data["labels"],
            y=data["black"],
            offsetgroup=1,
            marker_color='rgb(60, 60, 60)'
        ),
        go.Bar(
            name="Asian",
            x=data["labels"],
            y=data["asian"],
            offsetgroup=2,
            marker_color='rgb(240, 240, 240)'
        ),
        go.Bar(
            name="Indian",
            x=data["labels"],
            y=data["american_indian"],
            offsetgroup=3,
            marker_color='rgb(80, 80, 80)'
        ),
        go.Bar(
            name="Hawaiian",
            x=data["labels"],
            y=data["hawaiian"],
            offsetgroup=4,
            marker_color='rgb(160, 160, 160)'
        ),
        go.Bar(
            name="Other",
            x=data["labels"],
            y=data["other"],
            offsetgroup=5,
            marker_color='rgb(0, 0, 0)'
        ),
        go.Bar(
            name="Two or More Races",
            x=data["labels"],
            y=data["two_or_more"],
            offsetgroup=7,
           marker_color='rgb(280, 280, 280)'
        ),
    ],
    layout=go.Layout(
        title="Percentage of Population by Race",
        yaxis_title="Percentage",
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


# Urbana has a racially diverse population with a larger Black and Asian population than the rest of the geographies listed above. 

# # Analysis of Select Economic Characteristics
# ## Census Bureau American Community Survey (ACS) 2018 5-Year Estimates, Table S2503

# In[5]:


# Now let's look at the economic dataset
ec_data.head()


# In[6]:


# two of the columns have long names, so I'm going to rename them
ec_data = ec_data.rename(columns={'Estimate!!EMPLOYMENT STATUS!!Population 16 years and over': "pop_16yrs_older",
                   "Margin of Error!!EMPLOYMENT STATUS!!Population 16 years and over": "me_pop_16yrs_older"})


# In[7]:


# rename the GEO_NAME columns
ec_data['GEO_NAME'][2] = 'Champaign County'
ec_data['GEO_NAME'][3] = 'Urbana'


# In[8]:


ec_data.head() # now we see that the columns have short names


# In[9]:


# Labor Force 

# create a dictionary of races to compare across geographies
# also create a key for labels to identify the geography

data = {
    "employed": ec_data.pop_civilian_lf_employed.to_list(),
    "unemployed": ec_data.pop_civilian_lf_unemployed.to_list(),
    "armed_forces": ec_data.pop_lf_armed_services.to_list(),
    "not_in_lf": ec_data.pop_not_in_lf.to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana "
    ]
}

# this will create an interactive graphic showing race by geography
# used a gray scale color scheme, however, this can be adjusted by changing
# the marker_color rgb value


fig = go.Figure(
    data=[
        go.Bar(
            name="Employed",
            x=data["labels"],
            y=data["employed"],
            offsetgroup=0,
            marker_color='rgb(200, 200, 200)'
        ),
        go.Bar(
            name="Not In Labor Force",
            x=data["labels"],
            y=data["not_in_lf"],
            offsetgroup=1,
            marker_color='rgb(50, 50, 50)'
        ),
        go.Bar(
            name="Unemployed",
            x=data["labels"],
            y=data["unemployed"],
            offsetgroup=2,
            marker_color='rgb(120, 120, 120)'
        ),
        go.Bar(
            name="Armed Forces",
            x=data["labels"],
            y=data["armed_forces"],
            offsetgroup=3,
            marker_color='rgb(0, 0, 0)'
        ),
    ],
    layout=go.Layout(
        title="Labor Force Breakdown of Total Population",
        yaxis_title="Percent of Total Population",
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


# The breakdown of the labor force shows that Urbana has less employed individuals and more individuals not in the labor force. 

# In[10]:


# Unemployment Rate
ggplot(aes(x="GEO_NAME", weight="unemployment"), ec_data) + geom_bar(alpha = 0.8) + labs(title= "Unemployment Rate",
                      y="Percent Unemployment", x = "Geography")


# The unemployment rate of Urbana is higher than that of Champaign County. It is higher than the United States unemployment rate as well, but lower than the unemployment rate in Illinois. This is likely because of the large university population in Urbana. 

# In[11]:


# Occupation 
data = {
    "mbsa": ec_data.mbsa_occ.to_list(),
    "service": ec_data.service_occ.to_list(),
    "sale_ofc": ec_data.sale_ofc_occ.to_list(),
    'constr': ec_data.constr_occ.to_list(),
    'trans': ec_data.trans_occ.to_list(),
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
            name="Management, Business, Science, & Arts",
            x=data["labels"],
            y=data["mbsa"],
            offsetgroup=0,
            marker_color='rgb(280, 280, 280)'
        ),
        go.Bar(
            name="Service",
            x=data["labels"],
            y=data["service"],
            offsetgroup=1,
            marker_color='rgb(50, 50, 50)'
        ),
        go.Bar(
            name="Sales and Office",
            x=data["labels"],
            y=data["sale_ofc"],
            offsetgroup=2,
            marker_color='rgb(120, 120, 120)'
        ),
        go.Bar(
            name="Construction, Maintenance, & Natural Resources",
            x=data["labels"],
            y=data["constr"],
            offsetgroup=3,
            marker_color='rgb(0, 0, 0)'
        ),
        go.Bar(
            name="Production, Transportation, & Material Moving ",
            x=data["labels"],
            y=data["trans"],
            offsetgroup=4,
            marker_color='rgb(200, 200, 200)'
        ),
    ],
    layout=go.Layout(
        title="Occupations of Working Population 16 Years and Older by Geography",
        yaxis_title="Percent of Working Population",
        xaxis_title="Geography"
    ),

)


fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig.show("notebook")


# The majority of Urbana's working population is involved in "management, business, science, and arts" occupations. The percentage of the working population in this occupation is much higher than in other geographical areas. This is likely because of the influence of the University of Illinois U-C and world class health facilities existing in Urbana. 

# In[12]:


# Industry 

data = {
    "ag": ec_data.ag_ind.to_list(),
    "constr": ec_data.constr_ind.to_list(),
    "manu": ec_data.manu_ind.to_list(),
    "whole": ec_data.wholesale_ind.to_list(),
    'retail': ec_data.retail_ind.to_list(),
    'trans': ec_data.trans_ind.to_list(),
    'info': ec_data.info_ind.to_list(),
    'finance': ec_data.finance_ind.to_list(),
    'prof': ec_data.prof_ind.to_list(),
    'educ': ec_data.educ_ind.to_list(),
    'recreation': ec_data.recreation_ind.to_list(),
    'other': ec_data.other_ind.to_list(),
    'public': ec_data.public_admin_ind.to_list(),
    "labels": [
        "United States",
        "Illinois",
        "Champaign County",
        "Urbana"
    ]
}

# For this figure I utilized a modified BrBg color palette due
# to the Black-White color range being more difficult to distinguish with 
# so many categories. I chose BrBg because this palette is color-blind
# friendly

fig = go.Figure(
    data=[
        go.Bar(
            name="Agriculture, Forestry, Fishing & Hunting, & Mining",
            x=data["labels"],
            y=data["ag"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="Construction",
            x=data["labels"],
            y=data["constr"],
            offsetgroup=1,
            marker_color='rgb(90, 50, 0)'#rgb(191, 129, 45)'
        ),
        go.Bar(
            name="Manufactoring",
            x=data["labels"],
            y=data["manu"],
            offsetgroup=2,
            marker_color='rgb(140, 81, 10)'
        ),
        go.Bar(
            name="Wholesale Trade",
            x=data["labels"],
            y=data["whole"],
            offsetgroup=3,
            marker_color='rgb(191, 129, 45)'
        ),
        go.Bar(
            name="Retail Trade",
            x=data["labels"],
            y=data["retail"],
            offsetgroup=4,
            marker_color='rgb(223, 194, 125)'
        ),
        go.Bar(
            name="Transportation & Warehousing, & Utilities",
            x=data["labels"],
            y=data["trans"],
            offsetgroup=5,
            marker_color='rgb(246, 232, 195)'
        ),
        go.Bar(
            name="Information",
            x=data["labels"],
            y=data["info"],
            offsetgroup=6,
            marker_color='rgb(245, 245, 245)'
        ),
        go.Bar(
            name="Finance & Insurance, & Real Estate & Rental & Leasing",
            x=data["labels"],
            y=data["finance"],
            offsetgroup=7,
            marker_color='rgb(199, 234, 229)'
        ),
        go.Bar(
            name="Professional, Scientific, & Management, & Administrative & Waste Management Service",
            x=data["labels"],
            y=data["prof"],
            offsetgroup=8,
            marker_color='rgb(128, 205, 193)'
        ),
        go.Bar(
            name="Education Services, & Health Care & Social Assistance",
            x=data["labels"],
            y=data["educ"],
            offsetgroup=9,
            marker_color='rgb(53, 151, 143)'
        ),
        go.Bar(
            name="Arts, Entertainment, & Recreation, & Accomodation & Food Services",
            x=data["labels"],
            y=data["recreation"],
            offsetgroup=10,
            marker_color='rgb(1, 102, 94)'
        ),
        go.Bar(
            name="Other Services, Except Public Administration",
            x=data["labels"],
            y=data["other"],
            offsetgroup=11,
        marker_color='rgb(1, 75, 54)'
        ),
        go.Bar(
            name="Public Administration",
            x=data["labels"],
            y=data["public"],
            offsetgroup=12,
            marker_color='rgb(102, 145, 61)'
        ),
    ],
    layout=go.Layout(
        title="Industries of Working Population 16 Years and Older by Geography",
        yaxis_title="Percent of Working Population",
        xaxis_title="Geography"
    ),

)


# decrese size of legend font
fig.update_layout(legend=dict(
    font = dict(
            size=9,
            color="black")
))


fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)

fig.show("notebook")


# The most common industry in Urbana is in "education services and health care & social assistance" at 49%, which is over twice the percentage in the United States and Illinois. This is likely due to the high number of people employed at the local universities and hospitals.

# In[13]:


# class of worker 
data = {
    "priv": ec_data.priv_wage.to_list(),
    "gov": ec_data.gov_wkrs.to_list(),
    "self_empl": ec_data.self_empl.to_list(),
    "unpaid": ec_data.unpaid_fam.to_list(),
    
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
            name="Private Wage and Salary Workers",
            x=data["labels"],
            y=data["priv"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="Government Workers",
            x=data["labels"],
            y=data["gov"],
            offsetgroup=1,
            marker_color='rgb(100, 100, 100)'
        ),
        go.Bar(
            name="Self-Employed in Own, Not Inc. Business Workers",
            x=data["labels"],
            y=data["self_empl"],
            offsetgroup=2,
            marker_color='rgb(160, 160, 160)'
        ),
        go.Bar(
            name="Unpaid Family Workers",
            x=data["labels"],
            y=data["unpaid"],
            offsetgroup=3,
            marker_color='rgb(230, 230, 230)'
        ),
    ],
    layout=go.Layout(
        title="Classes of Working Population 16 Years and Older by Geography",
        yaxis_title="Percent of Working Population",
        xaxis_title="Geography"
    ),

)


fig.update_layout(legend=dict(
    font = dict(
            size=9,
            color="black")
))

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig.show("notebook")


# Urbana has less private wage and salary workers and more government workers than in Champaign County, Illinois, and the United States. 

# In[14]:


# Income by Geography

data = {
    "10k": ec_data.inc_10k.to_list(),
    "10k_15k": ec_data.inc_10k_15k.to_list(),
    "15k_25k": ec_data.inc_15k_25k.to_list(),
    "25k_35k": ec_data.inc_25k_35k.to_list(),
    "35k_50k": ec_data.inc_35k_50k.to_list(),
    "50k_75k": ec_data.inc_50k_75k.to_list(),
    "75k_100k": ec_data.inc_75k_100k.to_list(),
    "100k_150k": ec_data.inc_100k_150k.to_list(),
    "150k_200k": ec_data.inc_150k_200k.to_list(),
    "200k": ec_data.inc_200k_more.to_list(),
    
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
            name="Less than $10,000",
            x=data["labels"],
            y=data["10k"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="$10,000-14,999",
            x=data["labels"],
            y=data["10k_15k"],
            offsetgroup=1,
            marker_color='rgb(40, 40, 40)'
        ),
        go.Bar(
            name="$15,000-24,999",
            x=data["labels"],
            y=data["15k_25k"],
            offsetgroup=2,
            marker_color='rgb(80, 80, 80)'
        ),
        go.Bar(
            name="$25,000-34,999",
            x=data["labels"],
            y=data["25k_35k"],
            offsetgroup=3,
            marker_color='rgb(120, 120, 120)'
        ),
        go.Bar(
            name="$35,000-49,999",
            x=data["labels"],
            y=data["35k_50k"],
            offsetgroup=4,
            marker_color='rgb(160, 160, 160)'
        ),
        go.Bar(
            name="$50,000-74,999",
            x=data["labels"],
            y=data["50k_75k"],
            offsetgroup=5,
            marker_color='rgb(200, 200, 200)'
        ),
        go.Bar(
            name="$75,000-99,999",
            x=data["labels"],
            y=data["75k_100k"],
            offsetgroup=6,
            marker_color='rgb(240, 240, 240)'
        ),
        go.Bar(
            name="$100,000-149,999",
            x=data["labels"],
            y=data["100k_150k"],
            offsetgroup=7,
            marker_color='rgb(222, 218, 200)'
        ),
        go.Bar(
            name="$150,000-199,999",
            x=data["labels"],
            y=data["150k_200k"],
            offsetgroup=8,
            marker_color='rgb(150, 121, 97)'
        ),
        go.Bar(
            name="$200,000 or more",
            x=data["labels"],
            y=data["200k"],
            offsetgroup=9,
            marker_color='rgb(106, 78, 56)'
        ),
    ],
    layout=go.Layout(
        title="Household Yearly Income in 2018 Inflation-Adjusted Dollars by Geography",
        yaxis_title="Percent of Households",
        xaxis_title="Geography"
    ),

)

fig.update_layout(legend=dict(
    font = dict(
            size=9,
            color="black")
))

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig.show("notebook")


# The most common household yearly income group in Urbana is the 10,000 dollars or less group at over 20 percent. This is almost certainly because of the university population, however it is difficult to separate the influence of the university population from permanent Urbana residents who are deeply struggling financially. The next largest group is the 50,000-74,999 dollars per year group at approximately 14%.  The income distribution, aside from the less than 10,000 dollars group, follows a normal distribution. Comparing the income distribution of Urbana to other geographies, we can see that there are many more people under the poverty line. Again, this is influenced by the student population in Urbana.

# In[15]:


# Median and Mean Income
data = {
    "median": ec_data.median_hh_income.to_list(),
    "mean": ec_data.mean_hh_income.to_list(),
    
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
            name="Median Income",
            x=data["labels"],
            y=data["median"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="Mean Income",
            x=data["labels"],
            y=data["mean"],
            offsetgroup=1,
            marker_color='rgb(150, 150, 150)'
        ),
    ],
    layout=go.Layout(
        title="Household Median & Mean Income in 2018 Inflation-Adjusted Dollars by Geography",
        yaxis_title="Household Income in Dollars",
        xaxis_title="Geography"
    ),

)


fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig.show("notebook")


# Urbana has lower median and mean income than the other geographies. The difference between the median and mean incomes in Urbana is about 20,000 dollars which aligns with the income disparities seen in the other geographies. This doesn't mean that the income disparity is acceptable, but it means that the income disparity isn't unusually large. 

# In[16]:


# Commuting Breakdown of Working Population 16 Years and Older
data = {
    "alone": ec_data['Drove Alone'].to_list(),
    "carpool": ec_data.Carpooled.to_list(),
    "public": ec_data['Public Transportation'].to_list(),
    'walk': ec_data.Walked.to_list(),
    'other_trans': ec_data['Other Transportation'].to_list(),
    'home': ec_data['Work at Home'].to_list(),
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
            name="Drive Alone",
            x=data["labels"],
            y=data["alone"],
            offsetgroup=0,
            marker_color='rgb(220, 220, 220)'
        ),
        go.Bar(
            name="Carpool",
            x=data["labels"],
            y=data["carpool"],
            offsetgroup=1,
            marker_color='rgb(50, 50, 50)'
        ),
        go.Bar(
            name="Public Transportation",
            x=data["labels"],
            y=data["public"],
            offsetgroup=2,
            marker_color='rgb(120, 120, 120)'
        ),
        go.Bar(
            name="Walk to Work",
            x=data["labels"],
            y=data["walk"],
            offsetgroup=3,
            marker_color='rgb(0, 0, 0)'
        ),
        go.Bar(
            name="Other Transportation",
            x=data["labels"],
            y=data["other_trans"],
            offsetgroup=4,
            marker_color='rgb(180, 180, 180)'
        ),
        go.Bar(
            name="Work at Home",
            x=data["labels"],
            y=data["home"],
            offsetgroup=5,
            marker_color='rgb(260, 260, 260)'
        ),
    ],
    layout=go.Layout(
        title="Means of Transportation of Workers 16 Years and Older by Geography",
        yaxis_title="Percent of Working Population",
        xaxis_title="Geography"
    ),

)

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)

fig.show("notebook")


# The means of transportation in Urbana is very different than the means used in other geographies. There are significantly less workers driving alone and more workers using public transportation and walking. This indicate that Urbana is likely more walkable and easy to traverse than other geographies listed above.

# In[17]:


# Donut chart of Means of Transportation
# This is the same as above, but just for Urbana and in a different chart

# create labels to represent types of transportation. this will create the categories of the pie chart

labels = ['Car, truck, or van', 'Walked', 
          'Public transportation, excluding taxis', 'Other means', 'Worked at home']

# The sizes are the percentages for each category
# Create a list of the values for Urbana Only
# Note that I added drive alone and carpool because those are both driving with a car, truck, or van

sizes = [ec_data['Drove Alone'][ec_data.GEO_NAME == 'Urbana']+ec_data['Carpooled'][ec_data.GEO_NAME == 'Urbana'],
         ec_data['Walked'][ec_data.GEO_NAME == 'Urbana'],ec_data['Public Transportation'][ec_data.GEO_NAME == 'Urbana'],
        ec_data['Other Transportation'][ec_data.GEO_NAME == 'Urbana'],ec_data['Work at Home'][ec_data.GEO_NAME == 'Urbana']]

# In order not to get a warning, need to reshape the list into a 1-D numpy array

sizes = np.reshape(np.array(sizes), -1)

# Choose your color scheme. I chose one that is color blind friendly

colors = ['#F0E442','#40B0A6','#CC6677','#E65D09', '#88CCEE', '#882255']

# Explosion of categories. This will create separations between the categories
# You can include this if you want, but I decided not to. You can uncomment the following lines to see what explode does
# explode = (0.05,0.05,0.05,0.05,0.05)

# plot 
fig, ax1 = plt.subplots()
plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85) #, explode = explode)

# create the 'donut' by putting a center citcle within the pie chart
center_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
# save figure as a png
# Uncomment the following line if you'd like to save the png
# plt.savefig('commuting_breakdown.png')
plt.show()


# In[18]:


# Mean travel time to work
ggplot(aes(x="GEO_NAME", weight="mean_travel_time_wk"), ec_data) + geom_bar(alpha = 0.8) + labs(title= "Mean Travel Time to Work by Geography",
                      y="Mean Travel Time (Minutes)", x = "Geography")


# The mean travel times to work in Champaign County and Urbana are much lower than in Illinois and the United States. Urbana's mean travel time of approximately 15 minutes are lower than Champaign County's mean travel time of approximately 18 minutes. This adds to the idea that Urbana is an accessible city with quick means of transportation. 

# In[19]:


# Household Benefits by Geography

data = {
    "earnings": ec_data.hh_with_earnings.to_list(),
    "ss": ec_data.hh_with_ss.to_list(),
    "retirement": ec_data.hh_with_retirement.to_list(),
    "ssi": ec_data.hh_with_ssi.to_list(),
    "public": ec_data.hh_with_public_assist.to_list(),
    "food stamps": ec_data.hh_with_food_stamps.to_list(),
    
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
            name="Social Security",
            x=data["labels"],
            y=data["ss"],
            offsetgroup=0,
            marker_color='rgb(0, 0, 0)'
        ),
        go.Bar(
            name="Retirement Income",
            x=data["labels"],
            y=data["retirement"],
            offsetgroup=1,
            marker_color='rgb(200, 200, 200)'
        ),
        go.Bar(
            name="Supplemental Security Income",
            x=data["labels"],
            y=data["ssi"],
            offsetgroup=2,
            marker_color='rgb(60, 60, 60)'
        ),
        go.Bar(
            name="Cash Public Assistance Income",
            x=data["labels"],
            y=data["public"],
            offsetgroup=3,
            marker_color='rgb(130, 130, 130)'
        ),
        go.Bar(
            name="Food Stamp/SNAP Benefits in the Past 12 Months",
            x=data["labels"],
            y=data["food stamps"],
            offsetgroup=4,
            marker_color='rgb(245, 245, 245)'
        ),
    ],
    layout=go.Layout(
        title="Household Benefits by Geography",
        yaxis_title="Percent of Households",
        xaxis_title="Geography"
    ),

)


fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig.show("notebook")


# There are less people in Urbana using benefits than in other geographies listed above. There are significantly less people with social security and retirement income in Urbana than the United States and Illinois. This could be because of the younger population of Urbana that aren't using these benefits.

# In[20]:


# Median male and female income
data = {
    "median_male": ec_data.median_male_inc.to_list(),
    "median_female": ec_data.median_female_inc.to_list(),
    
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
            name="Female",
            x=data["labels"],
            y=data["median_female"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="Male",
            x=data["labels"],
            y=data["median_male"],
            offsetgroup=1,
            marker_color='rgb(150, 150, 150)'
        ),
    ],
    layout=go.Layout(
        title="Median Earnings for Full-Time, Year-Round Workers in 2018 Inflation-Adjusted Dollars by Geography and Sex",
        yaxis_title="Earnings in Dollars",
        xaxis_title="Geography"
    ),

)

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig.show("notebook")


# The income disparity between sexes still exists in Urbana, but it is much less than in other geographies. The difference in incomes is approximately 3,000 dollars while in Illionis and the United States, the difference is in the tens of thousands of dollars.

# In[21]:


# Type of Health Insurance by Geography
data = {
    "private": ec_data.priv_health_ins.to_list(),
    "public": ec_data.public_health_ins.to_list(),
    "none": ec_data.no_health_ins.to_list(),
    
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
            name="Private",
            x=data["labels"],
            y=data["private"],
            offsetgroup=0,
            marker_color='rgb(0,0,0)'
        ),
        go.Bar(
            name="Public",
            x=data["labels"],
            y=data["public"],
            offsetgroup=1,
            marker_color='rgb(120, 120, 120)'
        ),
        go.Bar(
            name="No Insurance",
            x=data["labels"],
            y=data["none"],
            offsetgroup=2,
            marker_color='rgb(240, 240, 240)'
        ),
    ],
    layout=go.Layout(
        title="Health Insurance Coverage of Civilian Noninstitutionalized Population by Geography",
        yaxis_title="Percent of CNP",
        xaxis_title="Geography"
    ),

)

fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig.show("notebook")


# The breakdown of health insurance shows that there are more people in Urbana with private insurance than in the other geographies listed and less people using public health coverage. Champaign County and Urbana have very similar percentages of people with no insurance, showing that Urbana's percentage is consistent with the area.

# In[22]:


# Employment Status by Insurance Status and Geography

# make subplots
trace1 = go.Bar(
    x=ec_data.GEO_NAME.to_list(),
    y=ec_data.employed_health_ins.to_list(),
    name='Employed',
    marker_color='rgb(0,0,0)'
)
trace2 = go.Bar(
    x=ec_data.GEO_NAME.to_list(),
    y=ec_data.unemployed_health_ins.to_list(),
    name='Unemployed',
    marker_color='rgb(120,120,120)'
)
trace3 = go.Bar(
  x=ec_data.GEO_NAME.to_list(),
  y=ec_data.not_lf_health_ins.to_list(),
  name='Not In Labor Force',
  marker_color='rgb(230,230,230)'
  )

trace4 = go.Bar(
    x=ec_data.GEO_NAME.to_list(),
    y=ec_data.employed_no_health_ins.to_list(),
    name='Employed',
    marker_color='rgb(0,0,0)'
)
trace5 = go.Bar(
    x=ec_data.GEO_NAME.to_list(),
    y=ec_data.unemployed_no_health_ins.to_list(),
    name='Unemployed',
    marker_color='rgb(120,120,120)'
)
trace6 = go.Bar(
  x=ec_data.GEO_NAME.to_list(),
  y=ec_data.not_lf_no_health_ins.to_list(),
  name='Not In Labor Force',
  marker_color='rgb(230,230,230)'
  )


fig = tools.make_subplots(rows=1, cols=2, subplot_titles=("Insured","Uninsured"))
fig.update_layout(barmode='group',height=500, width=1000, title = "Health Insurance Status of CNP Ages 19-94 by Employment Status and Geography")

fig.append_trace(trace1, 1,1)
fig.append_trace(trace2, 1, 1)
fig.append_trace(trace3,1,1)
fig.append_trace(trace4, 1,2)
fig.append_trace(trace5, 1, 2)
fig.append_trace(trace6,1,2)

fig.update_xaxes(title_text="Geography", row=1, col=1)
fig.update_xaxes(title_text="Geography", row=1, col=2)

# # Update yaxis properties
fig.update_yaxes(title_text="Percent of CNP", row=1, col=1)
fig.update_yaxes(title_text="Percent of CNP", row=1, col=2)
fig.update_traces(marker_line_color='rgb(0,0,0)',
                  marker_line_width=.5, opacity=0.9)
fig['layout'].update(height=500, width=1000)
fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0.04)','paper_bgcolor': 'rgba(0, 0, 0, 0)',},font=dict(size=11))


fig.show()


# The percentage of unemployed individuals and the percentage of individuals not in the labor force in Urbana with no insurance are consistent with those of Champaign County and significantly less than those of the United States. The percentage of individuals insured, regardless of employment status, is higher in Urbana than the other geographies listed.

# # Census Bureau Small Area Income and Poverty Estimates (SAIPE)
# ## Dataset containing single-year estimates of income and poverty for all U.S. states and counties as well as estimates of school-age children in poverty for all 13,000+ school districts.
# ## <https://www.census.gov/programs-surveys/saipe.html>

# In[23]:


saipe_df.head()


# In[24]:


# This dataset contains data on the entire United States
# Look at Champaign County only
champaign_df = saipe_df[saipe_df['County ID'] == 17019]
champaign_df.head()


# In[25]:


# Drop columns with NaNs
clean_champaign_df = champaign_df.dropna(axis='columns')
clean_champaign_df.head()


# In[26]:


# All ages in poverty
# Using seaborn; another plotting library

sns.set(style="whitegrid")
plt.plot(clean_champaign_df['Year'], clean_champaign_df['All Ages in Poverty Percent'], marker='o', alpha=0.75)
plt.xticks(np.arange(min(clean_champaign_df['Year']), max(clean_champaign_df['Year'])+1, 1.0))
plt.ylabel('Percent', fontsize = 12)
plt.xlabel('Year', fontsize = 12)
plt.ylim(18,25)

# to save plot as a png:
# plt.savefig('all_ages_in_poverty_percent.png')
plt.show()


# It appears that the percentage of people in poverty has generally decreased over time. From 2009-2018, the greatest percentage of people in poverty was in 2011 at about 23% and has remained stable at about 19% in 2018. 

# In[27]:


# Now let's look at SAIPE for school districts in Champaign County
# let's start by dropping columns with NaNs
clean_df_school = saipe_school_df.dropna(axis='columns')
clean_df_school.head()


# In[28]:


# Plot poverty ratio of the two school districts
sns.set(style="whitegrid")

g = sns.catplot(x="Year", y="Relevant age 5 to 17 Ratio", hue="District Name", data=clean_df_school,
                height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_ylabels("Poverty Ratio")
plt.show()


# It appears that the poverty ratio in Urbana School District 116 is higher than that of Champaign Community Unit School District 4. More research should be done to determine why this is and may be insightful for determining income inequities within the permanent resident population of Urbana.

# # Health: Comprehensive Benefits in Champaign County
# ## Illinois Department of Healthcare and Family Services 
# Number of Persons Enrolled in Comprehensive Benefits

# In[29]:


benefits.head()


# In[30]:


# Change the index to be the benefit enrollee column
benefits.set_index('Comprehensive Benefit Enrollees')


# In[31]:


# Create lists for each of the types of enrollees for all of the years
children = []
adults_disabled = []
aca = []
other_adults = []
seniors = []
for i in range(0,5):
    children.append(benefits[f'FY20{15+i}'][0])
    adults_disabled.append(benefits[f'FY20{15+i}'][1])
    aca.append(benefits[f'FY20{15+i}'][2])
    other_adults.append(benefits[f'FY20{15+i}'][3])
    seniors.append(benefits[f'FY20{15+i}'][4])
    
# plot the enrollee lists just to get an idea of the data
years = ['2015','2016','2017','2018','2019']
plt.plot(years, children, marker = 'o', label = 'Children')
plt.plot(years, adults_disabled, marker = 'o', label = 'Disabled Adults')
plt.plot(years, aca, marker = 'o', label = 'ACA')
plt.plot(years, other_adults, marker = 'o', label = 'Other Adults')
plt.plot(years, seniors, marker = 'o', label = 'Seniors')
plt.legend()
plt.show()


# The group with the most comprehensive benefits are children. Children receive significantly more than the other groups. Since the number of people in each group are so high, looking at how the number of people in each category changed over time may be more interesting.

# In[32]:


# Since values are so large, it will likely be more insightful to look at percentage change in benefits
# First make lists into arrays. Make sure values are floats
children_arr = np.array(children, dtype = float)
adults_disabled_arr = np.array(adults_disabled, dtype = float)
aca_arr = np.array(aca, dtype = float)
other_adults_arr = np.array(other_adults, dtype = float)
seniors_arr = np.array(seniors, dtype = float)

# Create function to calculate percent change 
def percent_change(array):
    return np.diff(array)/array[:-1]*100.
# Calculate percent change for child
child_pct_change = percent_change(children_arr)
child_pct_change


# In[33]:


# Insert a value of 0 for the first year
child_pct_change = np.insert(child_pct_change, 0,0)
child_pct_change


# In[34]:


# Do the same for all of the other enrollee categories
disabled_pct_change = percent_change(adults_disabled_arr)
disabled_pct_change = np.insert(disabled_pct_change, 0,0)
aca_pct_change = percent_change(aca_arr)
aca_pct_change= np.insert(aca_pct_change, 0,0)
other_pct_change = percent_change(other_adults_arr)
other_pct_change = np.insert(other_pct_change, 0,0)
seniors_pct_change = percent_change(seniors_arr)
seniors_pct_change = np.insert(seniors_pct_change, 0,0)

# plot percent change for enrollee benefits for each type of enrollee
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize = (10,7))

years = ['2015','2016','2017','2018','2019']

ax.plot(years,child_pct_change, marker = 'o', label = 'Children')
ax.plot(years,disabled_pct_change, marker = 'o', label = 'Disabled adults')
ax.plot(years,aca_pct_change, marker = 'o', label = 'ACA')
ax.plot(years,other_pct_change, marker = 'o', label = 'Other adults')
ax.plot(years,seniors_pct_change, marker = 'o', label = 'Seniors')
plt.title('Percent Growth in Benefits')
plt.ylabel('Percent Change')
plt.ylim(-20,20)

# plt.savefig('percent_growth_in_benefits.png')
plt.legend()
plt.show()


# The group of individuals with the largest percentage decrease in benefits was the other adults group at -6%. In 2019, all benefits decreased for children, disabled adults, ACA, and seniors, as well. Disabled adults saw significant growth in benefits in 2018, but saw decreased benefits in 2019. It would be interesting to delve deeper into why this is the case and how this is affecting the population of Urbana, specifically. 

# # Health Rankings by County
# ## University of Wisconsin Population Health Institute 2020 County Health Rankings <https://www.countyhealthrankings.org/app/illinois/2020/overview>
# 

# In[35]:


# Health Rankings by County
health_rankings.head()


# In[36]:


# The percentages are up to 6 decimal places. Round to zero decimal places. 
health_rankings = np.round(health_rankings, 0)

# Illinois total row is ful of NaNs...save Illinois data separately for comparison and delete from data frame

# save Illinois total data for reference
illinois_total = health_rankings.iloc[0]

# delete Illinois row (index 0)
health_rankings_new = health_rankings.drop(health_rankings.index[0])
health_rankings_new.head()

# There are quite a few NaN values...I'm going to fill those in on a case-by-case basis.
    # ie. if there are very few NaN values, I will replace it with the mean value
    # however if there are a lot of NaN values, I will consider not evaluating that metric or
    # mapping without those counties


# 15% of Champaign County is food insecure which is an above average percentage. If we are concerned about equity, it is important to consider whether people in a community have access to basic necessities like food. More research would need to be done to see how food insecure Urbana is, but for now, we do see that there could be improvements. 

# In[37]:


'''
Average traffic volume per meter of major roadways
    - Average traffic volume per meter of major roadways in the county.
    - EJSCREEN: Environmental Justice Screening and Mapping Tool, 2018
    - Illinois average is 508
'''
colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(0, 250, len(colorscale) - 1))

fig = ff.create_choropleth(fips=health_rankings_new['FIPS'], 
                           scope=['Illinois'],
                           binning_endpoints=endpts,
                           colorscale=colorscale,
                           values=health_rankings_new['Average Traffic Volume per Meter of Major Roadways'], 
                           title='Average Traffic Volume per Meter of Major Roadways', 
                           legend_title='Traffic Volume')
fig.layout.template = None
# fig.write_html("ave_traffic_volume.html")
fig.show("notebook")


# Average traffic volume in Champaign County is relatively high at a value of 214. 

# # Social Vulnerability Index (SVI)
# ## Center for Disease Control
# SVI is a metric used by the CDC to describe an area’s resilience to external stresses such as human health, natural or man-made disasters, and disease outbreaks. The SVI is measured using 15 Census variable that are broken down into the following four themes: Socioeconomic Status, Household Composition/Disability, Race/Ethnicity/Language, and Housing/Transportation. Areas are ranked using a percentile rank method where a percentile rank of 0 indicates least vulnerable and percentile rank of 1 indicates the most vulnerable. All Census tracts are ranked between 0 and 1. In addition, the ranking for each of the four themes are also included. 
# 

# In[38]:


svi_df.head()


# In[39]:


# Calculate Illinois Mean SVI for the years 2010, 2014, and 2016
ave_2010 = np.mean(svi_df.Value[svi_df.Year == 2010])
ave_2014 = np.mean(svi_df.Value[svi_df.Year == 2014])
ave_2016 = np.mean(svi_df.Value[svi_df.Year == 2016])

# Create a list of the averages for Illinois
averages = [ave_2010, ave_2014, ave_2016]

# Create a list of the median SVIs from 2010, 2014, and 2016 for Illinois
medians = [np.median(svi_df.Value[svi_df.Year == 2010]), np.median(svi_df.Value[svi_df.Year == 2014]), np.median(svi_df.Value[svi_df.Year == 2016])]

sns.set(style="whitegrid")

fig, ax = plt.subplots(figsize=(10,7))

ax.bar(svi_df.Year[svi_df.County == 'Champaign'], svi_df.Value[svi_df.County == 'Champaign'], alpha = 0.5)
ax.plot(svi_df.Year[svi_df.County == 'Champaign'], svi_df.Value[svi_df.County == 'Champaign'],label = 'Champaign County SVI',color='darkgreen',  marker = 'o')
ax.plot(svi_df.Year[svi_df.County == 'Champaign'], averages, label = 'IL Mean SVI', color = 'darkorange', marker = 'o')
ax.plot(svi_df.Year[svi_df.County == 'Champaign'], medians, label = 'IL Median SVI', color = 'darkblue', marker = 'o')
plt.ylim(0,1)
plt.ylabel('Social Vulnerability Index')
plt.legend()
# plt.savefig('social_vul_index.png')
plt.show()


# Champaign County has a higher Social Vulnerability Index score than the average and median Illinois Social Vulnerability Index. This pattern has remained consistent from 2010-2016. It is important to note that the SVI score in Champaign County isn't necessarily reflective of Urbana and could be inflated by the large university population.

# In[40]:


# Create color map for SVI scores in Illinois 2016
colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(0,1, len(colorscale) - 1))

fig = ff.create_choropleth(fips=svi_df.countyFIPS[svi_df.Year == 2016], 
                           scope=['Illinois'],
                           binning_endpoints=endpts,
                           colorscale=colorscale,
                           values=svi_df.Value[svi_df.Year == 2016], 
                           title='IL Social Vulnerability Index by County', 
                           legend_title='Social Vulnerability Index')
fig.layout.template = None
# fig.write_html("svi.html")
fig.show("notebook")


# Champaign County's SVI is at the center of the SVI distribution of values from 0 to 1. This indicates that Champaign County could likely improve factors to decrease the SVI score, but it also isn't performing badly either. More research needs to be done to determine specific areas that are more socially vulnerable than others. This can be done by examining the Census track level data that would provide more specific information about Urbana. 

# In[ ]:




