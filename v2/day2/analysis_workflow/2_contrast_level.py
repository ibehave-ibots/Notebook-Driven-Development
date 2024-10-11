#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install pandas hvplot


# In[2]:


import pandas as pd
import hvplot.pandas


# ## Contrast Analysis: EDA of Steinmetz Active Trials
# 
# We'll examine the contrast variable of Steinmetz experiment.
# 
# This notebook assumes that `1_data_access.ipynb` notebook is already run producing `steinmetz_active.csv` file

# Reading `steinmetz_active.csv`

# In[3]:


df = pd.read_csv('data_analysis/steinmetz_active.csv')
df.head()


# ### Different contrast levels

# In[4]:


df['contrast_left'].unique()


# In[5]:


df['contrast_right'].unique()


# There are four different contrast levels for both left and right stimulus

# ## Trials with different contrast levels

# Trials for each contrast left 

# In[6]:


df.groupby('contrast_left').size()


# Trial for each contrast right level

# In[7]:


df.groupby('contrast_right').size()


# Trials with each combination of contrast_left and contrast_right

# In[8]:


df.groupby(['contrast_left', 'contrast_right']).size()


# Plotting a heatmap showing number of contrast left and contrast right trials

# In[9]:


heatmap_data = df.groupby(['contrast_left', 'contrast_right']).size().reset_index(name='count')
heatmap_data.hvplot.heatmap(x='contrast_right', y='contrast_left', C='count')

