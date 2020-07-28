#!/usr/bin/env python
# coding: utf-8

# In[71]:


# Import Dependencies
import pandas as pd
import numpy as np


# In[72]:



school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()


# In[73]:


school_data.head()


# In[74]:


student_data.head()


# In[75]:


# District Summary

## Create a high level snapshot (in table form) of the district's key metrics, including:

### Total Schools
### Total Students
### Total Budget
### Average Math Score
### Average Reading Score
### % Passing Math (The percentage of students that passed math.)
### % Passing Reading (The percentage of students that passed reading.)
### % Overall Passing (The percentage of students that passed math and reading.)

total_schools=school_data["school_name"].count()
total_schools

total_students=student_data["student_name"].count()
total_students

total_budget=school_data["budget"].sum()
total_budget

avg_math=student_data[("math_score")].mean()
avg_math

avg_reading=student_data[("reading_score")].mean()
avg_reading

overall_avg=((avg_math + avg_reading) /2)
overall_avg

perc_math_pass=(school_data_complete["math_score"]>70).sum() / school_data_complete["math_score"].count()* 100
perc_math_pass 

perc_reading_pass= (school_data_complete["reading_score"]>70).sum() / school_data_complete["reading_score"].count()* 100
perc_reading_pass


# In[76]:


# Summary
District_Summary = pd.DataFrame({"Total Schools":[total_schools], "Total Students":[total_students],"Total Budget":[total_budget],
                                "Average Math Score":[avg_math], "Average Reading Score":[avg_reading], "% Passing Math":[perc_math_pass],
                                "% Passing Reading":[perc_reading_pass],"% Overall Passing Rate":[overall_avg]})
District_Summary


# In[77]:


# School Summary
## Create an overview table that summarizes key metrics about each school, including:

### School Name
### School Type 
### Total Students 
### Total School Budget
### Per Student Budget
### Average Math Score
### Average Reading Score
### % Passing Math
### % Passing Reading
### Overall Passing Rate (Average of the above two)
### Create a dataframe to hold the above results

sch_count= len(school_data_complete["school_name"].unique())
sch_count


# In[78]:


#School Name
sch_types=school_data.set_index(["school_name"])["type"]


# In[81]:


# Total Students 

stu_per_sch=school_data_complete["school_name"].value_counts()
stu_per_sch.head()


# In[82]:


#Total School Budget
sch_budget=school_data_complete.groupby(["school_name"])["budget"].mean()
sch_budget.head()


# In[83]:


#Per Student Budget
per_stu_bud=sch_budget/stu_per_sch
per_stu_bud


# In[84]:


#Average Math Score
avg_math_perSch=school_data_complete.groupby(["school_name"])["math_score"].mean()
avg_math_perSch.head()


# In[85]:


#Average Reading Score
avg_red_perSch= school_data_complete.groupby(["school_name"])["reading_score"].mean()
avg_red_perSch.head()


# In[86]:


#% Passing Math Score
pas_math_scor=school_data_complete.loc[school_data_complete["math_score"]>=70]
pas_math_scor

group_math_sch=pas_math_scor["school_name"].value_counts()
group_math_sch.head()

percent_math=group_math_sch/stu_per_sch*100
percent_math


# In[87]:


# % Passing Reading score
read_scor=school_data_complete.loc[school_data_complete["reading_score"]>=70]

by_read_PerSch= read_scor["school_name"].value_counts()
by_read_PerSch.head()

percent_read=by_read_PerSch/stu_per_sch*100
percent_read


# In[88]:


# % Overall Passing Rate (Average of the above two)
overall=percent_math + percent_read/stu_per_sch
overall


# In[89]:


#New df for School_summery
school_summery_df = pd.DataFrame({"School Type":sch_types, "Total Students":stu_per_sch, "Total School Budget":sch_budget
                                ,"Per Student Budget":per_stu_bud ,"Average Math Score" :avg_math_perSch,
                             "Average Reading Score":avg_red_perSch,
                             "% Passing Math":percent_math, "% Passing Reading":percent_read,
                            "% Overall Passing Rate":overall})
school_summery_df.head()


# In[90]:


#Top Performing Schools (By Passing Rate)
TopSch_df=school_summery_df.sort_values(["% Passing Math","% Passing Reading","% Overall Passing Rate" ], 
                                        ascending=False)
TopSch_df.head()


# In[91]:


# Mapping Top Performing Schools (By Passing Rate)
TopSch_df["Total School Budget"]=TopSch_df["Total School Budget"].map("${:,.2f}".format)
TopSch_df["Per Student Budget"]=TopSch_df["Per Student Budget"].map("${:,.2f}".format)

TopSch_df


# In[92]:


# Bottom Performing Schools (By Passing Rate)
## Sort and display the five worst-performing schools

BottomSch_df=school_summery_df.sort_values("% Overall Passing Rate")
BottomSch_df.head()


# In[93]:


# Math Scores by Grade**

## Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

math_9th=student_data.loc[student_data["grade"] == "9th"].groupby(["school_name"])['math_score'].mean()
math_9th.head()
math_10th=student_data.loc[student_data["grade"] == "10th"].groupby(["school_name"])['math_score'].mean()
math_10th.head()
math_11th=student_data.loc[student_data["grade"] == "11th"].groupby(["school_name"])["math_score"].mean()
math_11th.head()
math_12th=student_data.loc[student_data["grade"] == "12th"].groupby(["school_name"])["math_score"].mean()
math_12th.head()

math_byGrad=pd.DataFrame({"9th":math_9th, "10th": math_10th, "11th":math_11th, "12th":math_12th })
math_byGrad


# In[94]:


# Reading Scores by Grade

## Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

read_9th=student_data.loc[student_data["grade"] == "9th" ].groupby(["school_name"])["reading_score"].mean()
read_10th=student_data.loc[student_data["grade"] == "10th" ].groupby(["school_name"])["reading_score"].mean()
read_11th=student_data.loc[student_data["grade"] == "11th" ].groupby(["school_name"])["reading_score"].mean()
read_12th=student_data.loc[student_data["grade"] == "12th" ].groupby(["school_name"])["reading_score"].mean()

reading_byGrade=pd.DataFrame({"9th":read_9th,"10th":read_10th, "11th":read_11th, "12th":read_12th })
reading_byGrade


# In[95]:


# Scores by School Spending

## Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:

### Average Math Score
### Average Reading Score
### % Passing Math (The percentage of students that passed math.)
### % Passing Reading (The percentage of students that passed reading.)
### % Overall Passing (The percentage of students that passed math and reading.)

school_summery_df.head()


# In[97]:


bins = [10, 582, 629, 640, 650]
group_names = ["<=$582", "$582-629", "$629-640", ">$650"]

school_summery_df["Spending Ranges (Per Student)"]=pd.cut(school_summery_df["Total School Budget"]/school_summery_df["Total Students"]
                                            ,bins , labels=group_names)
school_summery_df.head()
scores_by_sch=school_summery_df .drop(columns=["Total Students", "Total School Budget","School Type", "Per Student Budget"])
scores_by_sch


# In[98]:


# Scores by School Size
## erform the same operations as above, based on school size.
school_summery_df.head()


# In[99]:


size_bins = [500, 1000, 2500, 5000]
group_names = ["Small (<1000)", "Medium (1000-2500)", "Large (2500-5000)"]


# In[101]:


school_summery_df["School Size"]=pd.cut(school_summery_df["Total Students"],size_bins , labels=group_names)
                                
scores_by_sch["School Size"]=pd.cut(school_summery_df["Total Students"],size_bins , labels=group_names)
scores_by_sch.head()


# In[102]:


#Scores by School Type

### Repeat the above breakdown, but this time group schools based on school type (Charter vs. District).

scores_by_type= school_summery_df.drop(columns=["Total Students","Total School Budget", "Per Student Budget"])
scores_by_type.head()


# In[103]:



by_schType = scores_by_type.groupby(["School Type"])
by_schType.mean()


# In[ ]:




