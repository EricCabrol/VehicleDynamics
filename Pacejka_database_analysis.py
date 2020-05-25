# -*- coding: utf-8 -*-
# E. Cabrol - May 25, 2020
# Analysis of tire database with Pandas

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import re
import numpy as np

# function used to scrape filepath
def scrape(filepath):
    gotIt = re.search(r"^(\w+?)_(.+?)/(.+?)/(.+?)/(.+?)/(.+?)/(.+)",filepath)
    return gotIt.group(1),gotIt.group(2),gotIt.group(3),gotIt.group(4),gotIt.group(6),gotIt.group(7)


# Definitions
params_longi=("PCX1","PDX1","PDX2","PEX1","PEX2","PEX3","PEX4","PKX1","PKX2","PKX3","PHX1","PHX2","PVX1","PVX2")


# Import database as dataframe
# na_values argument to avoid some useless lines
df = pd.read_csv('BD_tire_ALL.txt',sep='\t',encoding = "ISO-8859-1",na_values='#DIV/0!')

# Remove useless columns
df=df.drop(columns=['FILE_TYPE', 'FILE_FORMAT','LENGTH','FORCE','ANGLE','MASS','TIME','PROPERTY_FILE_FORMAT','MFSAFE1','MFSAFE2','MFSAFE3',
                  'VXLOW','LONGVL','TYPE','ASPECT_RATIO','VERTICAL_DAMPING','KPUMIN','KPUMAX','ALPMIN','ALPMAX','CAMMIN','CAMMAX',
                  'LFZO','LCX','LMUX','LEX','LKX','LHX','LVX','LCY','LVY','LMUY','LEY','LKY','LHY','LVY','LGAY','LTR','LRES','LGAZ','LXAL','LYKA','LVYKA',
                  'LS','LSGKP','LSGAL','LGYR','LMX','LMY','LGAX','LVMX','QTZ1','MBELT','FileIdent','FileCreator'])

# Add new columns

for index,row in df.iterrows():
    filepath=df.loc[index,'File']
    (tire_oem,tire_model,tire_dim,tire_dot,tire_measure,tire_tirfile)= scrape(filepath)
    match_object = re.search(r"P(\d+)bar",tire_tirfile)
    if match_object:
        pressure=float(match_object.group(1))/10
    else:
        pressure="NULL"
    df.loc[index,'OEM']=tire_oem
    df.loc[index,'Model']=tire_model
    df.loc[index,'Dim']=tire_dim
    df.loc[index,'DOT']=tire_dot
    df.loc[index,'Pressure']=pressure
    df.loc[index,'Measure']=tire_measure
    df.loc[index,'tirfile']=tire_tirfile

    
# LONGITUDINAL - Only "Use mode = 4"

df_mode4 = df[df['USE_MODE']==4]
stats_mode4=df_mode4.loc[:,'PCX1':'PKX3'].describe()


# A few plots
plt.figure(1)
df.PCX1.plot(kind='hist',bins=40,title='PCX1')

plt.figure(2)
df.PDX1.plot(kind='hist',bins=40,title='PDX1')

plt.show()

#%%
# Check for outliers

# The following section classifies as outliers all tires for which the difference with the mean is greater than
# coef_nok times the standard deviation
coef_nok=2.0

df_nok=pd.DataFrame() # create an empty dataframe

headers=["name","min","1%","25%","mean","75%","99%","max","std"]
headers_format = "{:^10s}" * len(headers)
print(headers_format.format(*headers))

for param in params_longi:
    # print table of statistical data for each parameter
    print("{:^10s}".format(param), end='')
    values=[df_mode4[param].min(),df_mode4[param].quantile(0.01),df_mode4[param].quantile(0.25),df_mode4[param].mean(),df_mode4[param].quantile(0.75),df_mode4[param].quantile(0.99),df_mode4[param].max(),df_mode4[param].std()]
    values_format="{:^10.2f}" * len(values)
    print(values_format.format(*values),end='')
    
    # check if (max-mean) or (mean-min) are greater than accepted threshold
    upperHalfRange=df_mode4[param].max()-df_mode4[param].mean()
    lowerHalfRange=df_mode4[param].mean()-df_mode4[param].min()   
    if  upperHalfRange >= coef_nok*df_mode4[param].std() or lowerHalfRange >= coef_nok*df_mode4[param].std():
        print("\tKO")
        #append the NOK indexes (for this param) to the df_nok dataframe
        df_nok=df_nok.append(df_mode4[np.abs(df_mode4[param]-df_mode4[param].mean()) >= (coef_nok*df_mode4[param].std())])
    else:
        print("\t-")

# Remove duplicates from df_nok since some indexes may have been counted multiple times
df_nok.drop_duplicates(inplace=True)
# Create a "clean" dataframe
df_clean=df_mode4.drop(df_nok.index)
# Plot a scatter matrix for this dataframe
scatter_matrix(df_clean.loc[:,'PCX1':'PKX3'],figsize=(12,12))
