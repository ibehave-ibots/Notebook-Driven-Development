#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install pandas


# In[2]:


import pandas as pd


# ## Data Access
# 
# In the experiment reported in by [Steinmetz et al, 2019](https://www.nature.com/articles/s41586-019-1787-x) in Nature, mice were tasked with turning a wheel to the left or right based on the relative contrast levels of two simultaneously-presented gradient stimuli. 
# 
# The data is curated and available on iBOTS Sciebo. 

# In[3]:


url = "https://uni-bonn.sciebo.de/s/3ZbmkolHLQu1ADa/download"
df = pd.read_csv(url)
df.head()


# Some information about the columns

# In[4]:


df.columns


# Dropping 'Unnamed: 0' column

# In[5]:


df = df.drop(columns=['Unnamed: 0'])
df.head()


# We are only selecting active trials

# In[6]:


df = df[df["active_trials"]]
df.head()


# Saving to a file called 'steinmetz_active.csv'

# In[7]:


df.to_csv('data_analysis/steinmetz_active.csv', index=False)

