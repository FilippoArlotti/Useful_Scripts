# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
# WE MOVE INTO THE WORKING FOLDER:
directory = os.getcwd()
# WE SHOULD CHECK THAT THE FILE OF INTEREST IS IN THE DIRECTORY:
path ='GC2Dt_diffusion_gc.txt'
isExist = os.path.exists(path)
if not isExist == True:
    raise('The file "GC2Dt_diffusion_gc.txt" is not in the current folder, please check...')
# WE IMPORT THE DATAFRAME FROM DIFFUSION OUTPUT OF THE CODE:
variables = ['A', 'rho', 'eta', 'Trapped','Diffusive','D_diff', 'a_diff', 'b_diff', 'R2(diff)_d','R2(interp)_d','Ballistic','D_ball', 'a_ball', 'b_ball', 'R2(diff)_ball','R2(interp)_ball']
data = pd.read_table('GC2Dt_diffusion_gc.txt',sep = ' ', skiprows = 2, names = variables)
# CHECK THAT THE DATAFRAME SEEMS CORRECT
print('the original dataframe is the following: \n')
print(data.head(10))
# WHAT ARE THE POSSIBLE VALUES OF THE PARAMETER WE WANT TO FIX?
print(pd.Series({rho:data[rho].unique() for rho in data}))
# SET THE PARAMETER YOU WANT TO FIX:
a = data.rho
# SET ITS VALUE:
b = 0.050000
# wE CAN FILTER THE DATAFRAME:
data_desired = data[a == b]
# CHECK THAT THE NEW DATAFRAME SEEMS CORRECT:
print(data_desired.head(10))
# WRITE INTO THE NEW .TXT FILE:
data_desired.to_csv('GC2Dt_diffusion_gc_Desired_Lines.txt', sep = ' ', index=False)
