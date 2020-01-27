#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import plotly
import pandas as pd
import numpy as np


# In[2]:


data= []

#f = "66955_S288C_AD.vcf"
#f = "69521_S288C_AD.vcf"
f = "para_AD"

with open(f, 'r') as ad:
    for line in ad:
        if len(line.split(",")) > 3:
            continue
        else:
            data.append([x.strip() for x in line.split(",")])


# In[3]:


freqs = pd.DataFrame(data, columns=["ref_count", "var_count", "NON_REF"], dtype=float)


# In[4]:



freqs["total"] = freqs.apply(lambda row: row.ref_count+row.var_count+row.NON_REF, axis=1)
freqs["ref_af"] = freqs.apply(lambda row: np.true_divide(row.ref_count, row.total), axis=1)
freqs["var_af"] = freqs.apply(lambda row: np.true_divide(row.var_count, row.total), axis=1)


# In[5]:


hist = px.histogram( x=pd.concat([freqs.ref_af, freqs.var_af]), nbins = 1000)
hist.show()


# In[13]:


plotly.io.orca.config.executable = '/usr/local/bin/orca'
hist.write_image(format = "pdf", file="para_af.pdf")
#plotly.offline.plot(hist, filename='para_af.html', auto_open=False)


# In[ ]:




