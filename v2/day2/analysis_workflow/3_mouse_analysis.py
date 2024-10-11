#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install pandas hvplot


# In[2]:


import pandas as pd
import hvplot.pandas


# ## Mouse Analysis: EDA of Steinmetz Active Trials
# 
# We'll examine the mouse variable of Steinmetz experiment.
# 
# This notebook assumes that `1_data_access.ipynb` notebook is already run producing `steinmetz_active.csv` file

# Reading `steinmetz_active.csv`

# In[3]:


df = pd.read_csv('data_analysis/steinmetz_active.csv')
df.head()


# ## Different Mice

# In[4]:


df['mouse'].nunique()


# In[5]:


df['mouse'].unique()


# In[6]:


df['mouse'].value_counts()


# There are 10 mice each with number of trials as given in the table above.

# ## Visualization

# In[7]:


df['mouse'].value_counts().hvplot.barh()

