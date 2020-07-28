#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import numpy as np


# In[35]:


file_to_load = "Resources/purchase_data.csv"
purchase_data = pd.read_csv(file_to_load)


# In[36]:


# Total Number of Players
total_players = len(purchase_data["SN"].value_counts())

player_count = pd.DataFrame({"Total Players":[total_players]})
player_count


# In[37]:


# Purchasing analysis
number_of_unique_items = len((purchase_data["Item ID"]).unique())
average_price = (purchase_data["Price"]).mean()
number_of_purchases = (purchase_data["Purchase ID"]).count()
total_revenue = (purchase_data["Price"]).sum()


summary_df = pd.DataFrame({"Number of Unique Items":[number_of_unique_items],
                           "Average Price":[average_price], 
                           "Number of Purchases": [number_of_purchases], 
                           "Total Revenue": [total_revenue]})

# Currency format
summary_df.style.format({'Average Price':"${:,.2f}",
                         'Total Revenue': '${:,.2f}'})


# In[38]:


# Gender Demographics
##Percentage and Count of Male Players
##Percentage and Count of Female Players
##Percentage and Count of Other / Non-Disclosed

gender_stats = purchase_data.groupby("Gender")
total_count_gender = gender_stats.nunique()["SN"]
percentage_of_players = total_count_gender / total_players * 100

gender_demographics = pd.DataFrame({"Percentage of Players": percentage_of_players, "Total Count": total_count_gender})

gender_demographics.index.name = None
gender_demographics.sort_values(["Total Count"], ascending = False).style.format({"Percentage of Players":"{:.2f}"})


# In[39]:


# Count the total purchases by gender 
## The below each broken by gender

### Purchase Count
### Average Purchase Price
### Total Purchase Value
### Average Purchase Total per Person by Gender

purchase_count = gender_stats["Purchase ID"].count()

avg_purchase_price = gender_stats["Price"].mean()

avg_purchase_total = gender_stats["Price"].sum()

avg_purchase_per_person = avg_purchase_total/total_count_gender

# Create data frame
gender_demographics = pd.DataFrame({"Purchase Count": purchase_count, 
                                    "Average Purchase Price": avg_purchase_price,
                                    "Average Purchase Value":avg_purchase_total,
                                    "Avg Purchase Total per Person": avg_purchase_per_person})
gender_demographics.index.name = "Gender"

# Currency format
gender_demographics.style.format({"Average Purchase Value":"${:,.2f}",
                                  "Average Purchase Price":"${:,.2f}",
                                  "Avg Purchase Total per Person":"${:,.2f}"})


# In[40]:


# Age Demographics

##The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)

### Purchase Count
### Average Purchase Price
### Total Purchase Value
### Average Purchase Total per Person by Age Group

age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

purchase_data["Age Group"] = pd.cut(purchase_data["Age"],age_bins, labels=group_names)
purchase_data

age_grouped = purchase_data.groupby("Age Group")

total_count_age = age_grouped["SN"].nunique()

percentage_by_age = (total_count_age/total_players) * 100

# Create data frame 
age_demographics = pd.DataFrame({"Percentage of Players": percentage_by_age, "Total Count": total_count_age})
age_demographics.index.name = None

# Style format
age_demographics.style.format({"Percentage of Players":"{:,.2f}"})


# In[41]:


# Top Spenders

## Identify the the top 5 spenders in the game by total purchase value, then list (in a table):

### SN
### Purchase Count
### Average Purchase Price
### Total Purchase Value

purchase_count_age = age_grouped["Purchase ID"].count()

avg_purchase_price_age = age_grouped["Price"].mean()

total_purchase_value = age_grouped["Price"].sum()

avg_purchase_per_person_age = total_purchase_value/total_count_age

# Create data frame
age_demographics = pd.DataFrame({"Purchase Count": purchase_count_age,
                                 "Average Purchase Price": avg_purchase_price_age,
                                 "Total Purchase Value":total_purchase_value,
                                 "Average Purchase Total per Person": avg_purchase_per_person_age})
age_demographics.index.name = None

# Currency format
age_demographics.style.format({"Average Purchase Price":"${:,.2f}",
                               "Total Purchase Value":"${:,.2f}",
                               "Average Purchase Total per Person":"${:,.2f}"})


# In[42]:


# Most Popular Items

##Identify the 5 most popular items by purchase count, then list (in a table):

###Item ID
### Item Name
### Purchase Count
### Item Price
### Total Purchase Value
spender_stats = purchase_data.groupby("SN")

purchase_count_spender = spender_stats["Purchase ID"].count()

avg_purchase_price_spender = spender_stats["Price"].mean()

purchase_total_spender = spender_stats["Price"].sum()

# Create data frame
top_spenders = pd.DataFrame({"Purchase Count": purchase_count_spender,
                            "Average Purchase Price": avg_purchase_price_spender,
                            "Total Purchase Value":purchase_total_spender})
formatted_spenders = top_spenders.sort_values(["Total Purchase Value"], ascending=False).head()

# Currency format
formatted_spenders.style.format({"Average Purchase Total":"${:,.2f}",
                                "Average Purchase Price":"${:,.2f}", 
                                "Total Purchase Value":"${:,.2f}"})


# In[46]:


# Most Profitable Items

## Identify the 5 most profitable items by total purchase value, then list (in a table):

### Item ID
### Item Name
### Purchase Count
### Item Price
### Total Purchase Value
items = purchase_data[["Item ID", "Item Name", "Price"]]

item_stats = items.groupby(["Item ID","Item Name"])

purchase_count_item = item_stats["Price"].count()

purchase_value = (item_stats["Price"].sum()) 

item_price = purchase_value/purchase_count_item

# Create data frame
most_popular_items = pd.DataFrame({"Purchase Count": purchase_count_item, 
                                   "Item Price": item_price,
                                   "Total Purchase Value":purchase_value})
popular_formatted = most_popular_items.sort_values(["Purchase Count"], ascending=False).head()

# Currnency format
popular_formatted.style.format({"Item Price":"${:,.2f}",
                                "Total Purchase Value":"${:,.2f}"})


# In[ ]:





# In[ ]:




