#!/usr/bin/env python
# coding: utf-8

# In[88]:


import pandas as pd
import numpy as np


# In[89]:


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}


# In[90]:


df = pd.DataFrame(people)


# In[91]:


df


# In[92]:


df.dropna()


# In[93]:


df.dropna(axis='index',how='any')


# In[94]:


df.dropna(axis='index',how='all')


# In[95]:


df.dropna(axis='columns',how='any')


# In[96]:


df.dropna(axis='index',how='any',subset=['email'])


# In[97]:


df.dropna(axis='index',how='any',subset=['email','age'])


# In[98]:


df


# In[99]:


df.replace('NA',np.nan,inplace=True)


# In[100]:


df


# In[132]:


df.dropna(axis='index',how='any',subset=['email','age'])


# In[101]:


df.replace('Missing',np.nan,inplace=True)


# In[102]:


df


# In[137]:


df.replace('None',np.nan,inplace=True)
df


# In[138]:


df.dropna()


# In[139]:


df.isna()


# In[140]:


df.fillna('Missing')


# In[141]:


df


# In[142]:


df.fillna(0)


# In[143]:


df.dtypes


# In[144]:


df['age'].mean()


# In[145]:


# df['age'] = df['age'].astype(int)


# In[ ]:





# In[146]:


df['age'] = df['age'].astype(float)


# In[147]:


df


# In[148]:


avgage = df['age'].mean()
avgage


# In[149]:


df


# In[150]:


df


# In[151]:


df.replace('Missing',np.nan,inplace=True)


# In[152]:



df


# In[153]:


df.replace('None',np.nan,inplace=True)


# In[154]:


df


# In[155]:


df.replace("NaN",0,inplace = True)


# In[156]:


df


# In[159]:


ageavg = df['age'].mean()
ageavg


# In[165]:


df['age'].fillna(ageavg,inplace=True)
df

