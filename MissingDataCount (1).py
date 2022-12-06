#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('data.csv')


# In[3]:


data_missing = data.isna()


# In[4]:


data_missing.sum()


# In[ ]:




