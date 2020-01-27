#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import plotly
import pandas as pd
import numpy as np
import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--freqs", metavar="allele_frequences", required=True, action="store")
args = parser.parse_args()

f = args.freqs
prefix = os.path.split(f)[1].split(".")[0] 

data= []

with open(f, 'r') as ad:
    for line in ad:
        if len(line.split(",")) > 3:
            continue
        else:
            data.append([x.strip() for x in line.split(",")])

freqs = pd.DataFrame(data, columns=["ref_count", "var_count", "NON_REF"], dtype=float)

freqs["total"] = freqs.apply(lambda row: row.ref_count+row.var_count+row.NON_REF, axis=1)
freqs["ref_af"] = freqs.apply(lambda row: np.true_divide(row.ref_count, row.total), axis=1)
freqs["var_af"] = freqs.apply(lambda row: np.true_divide(row.var_count, row.total), axis=1)

freqs = freqs[ (freqs["ref_af"] > 0) & (freqs["ref_af"] < 1) ] 

hist = px.histogram( x=pd.concat([freqs.ref_af, freqs.var_af]), nbins = 1000)
#hist.show()

plotly.io.orca.config.executable = '/usr/local/bin/orca'
hist.write_image(format = "pdf", file=f"{prefix}_af.pdf")

