#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import pandas as pd
import os

hist = pd.read_csv(
    "bbtools/97196_23.khist",
    sep="\t"
)
hist["sample"] = "97196"
peaks = pd.read_csv("bbtools/97196_23.peaks", sep="\t", skiprows=range(0,13))
hist


# In[2]:


samples = set([x.split("_")[0] for x in os.listdir("bbtools")])
for s in samples:
    if "khist" in s or "peaks" in s:
        continue
    add = pd.read_csv(
        f"bbtools/{s}_23.khist",
        sep="\t"
    )
    add["sample"] = s
    hist = hist.append(add)


# In[3]:


est_hap_size = {
    "97191": 252599320,
    "97192": 39621812,
    "97194": 47861606,
    "97195": 37168017,
    "97196": 80979084,
    "97197": 57659519,
    "97198": 88609641,
}
fig = px.line(hist, x="#Depth", y="Count", facet_col="sample")
fig.update_xaxes(range=[0,150], title = "Depth")
fig.update_yaxes(range=[0,max(peaks["max"])*1.25])
for a in fig.layout.annotations:
    a.text = a.text.split("=")[1]
    a.text = f"{a.text}-{est_hap_size[a.text]/1e6:.2f} Mbp"

fig.show()


# In[69]:


# This is supposed to be diploid yeast? Only one peak though...
cntrl = pd.read_csv("cntrl/SRX6085507_23.khist", sep = "\t")
cpeaks = pd.read_csv("cntrl/SRX6085507_23.peaks", sep="\t", skiprows=range(0,14))

fig = px.line(cntrl, x="#Depth", y="Count")
fig.update_xaxes(range=[0,300], title = "Depth")
fig.update_yaxes(range=[0,max(cpeaks["max"])*1.25])
print(cpeaks)
fig.show()


# In[21]:


# C. elegans genome sequencing read library - has to be diploid
cntrl = pd.read_csv("cntrl/ERX3525517.khist", sep = "\t")
cpeaks = pd.read_csv("cntrl/ERX3525517.peaks", sep="\t", skiprows=range(0,14))

print(cpeaks)

fig = px.line(cntrl, x="#Depth", y="Count", title="C. elegans (ERX3525517)")
fig.update_xaxes(range=[0,100], title = "Depth")
fig.update_yaxes(range=[0,max(cpeaks["max"])*1.25])
print(cpeaks)
fig.show()


# In[12]:


# Human genome sequencing read library - has to be diploid
cntrl = pd.read_csv("cntrl/DRX135491.khist", sep = "\t")
cpeaks = pd.read_csv("cntrl/DRX135491.peaks", sep="\t", skiprows=range(0,13))


fig = px.line(cntrl, x="#Depth", y="Count", title="C. elegans (ERX3525517)")
fig.update_xaxes(range=[0,600], title = "Depth")
fig.update_yaxes(range=[0,max(cpeaks["max"])*1.25])
#fig.update_yaxes(range=[0,5e6])

fig.show()


# In[1]:


# On krapbook with Tim's known haploid/diploid yeasts
import plotly.express as px
import plotly
import pandas as pd
import os


# In[4]:


cntrl = pd.read_csv("para_23.khist", sep = "\t")
cpeaks = pd.read_csv("para_23.peaks", sep="\t", skiprows=range(0,14))


fig = px.line(cntrl, x="#Depth", y="Count", title="Paraphysoderma sp. (diploid)")
fig.update_xaxes(range=[0,600], title = "Depth")
fig.update_yaxes(range=[0,max(cpeaks["max"])*1.25])
#fig.update_yaxes(range=[0,5e6])

fig.show()
plotly.io.orca.config.executable = '/usr/local/bin/orca'
fig.write_image(file="para_kmers.pdf", format="pdf")
#plotly.offline.plot(fig, filename='para_kmers.html')


# In[10]:


cntrl = pd.read_csv("69521_23.khist", sep = "\t")
cpeaks = pd.read_csv("69521_23.peaks", sep="\t", skiprows=range(0,13))


fig = px.line(cntrl, x="#Depth", y="Count", title="69521 (haploid)")
fig.update_xaxes(range=[0,600], title = "Depth")
fig.update_yaxes(range=[0,max(cpeaks["max"])*1.25])
#fig.update_yaxes(range=[0,5e6])

fig.show()
plotly.offline.plot(fig, filename='69521.html')


# In[ ]:




