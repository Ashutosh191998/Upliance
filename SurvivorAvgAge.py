#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as nm


# In[13]:


SurvivorData = pd.read_csv('data.csv')
SurvivorData.head()


# In[14]:


AvgSurvivorAge = SurvivorData.groupby(['Survived']).Age.agg(['mean'])


# In[15]:


AvgSurvivorAge


# In[ ]:




