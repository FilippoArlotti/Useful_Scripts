# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
import time

#Do you want to use input/output mode:
Input_Output_Mode = False

# WE MOVE INTO THE WORKING FOLDER:
directory = os.getcwd()

# WE SHOULD CHECK THAT THE FILE OF INTEREST IS IN THE DIRECTORY:
path ='GC2Dt_diffusion_gc.txt'
isExist = os.path.exists(path)
if not isExist == True:
    raise Exception('The file "GC2Dt_diffusion_gc.txt" is not in the current folder or may have a different name, please check...')

# WE IMPORT THE DATAFRAME FROM DIFFUSION OUTPUT OF THE CODE:
variables = ['A', 'rho', 'eta', 'Trapped','Diffusive','D_diff', 'a_diff', 'b_diff', 'R2(diff)_d','R2(interp)_d','Ballistic','D_ball', 'a_ball', 'b_ball', 'R2(diff)_ball','R2(interp)_ball']
data = pd.read_table('GC2Dt_diffusion_gc.txt',sep = ' ', skiprows = 2, names = variables)

# CHECK THAT THE DATAFRAME SEEMS CORRECT
print('The original dataframe is the following: \n')
print(data.head(10), '\n \n \n Check the possible values of the parameters that you can fix. \n \n')

# WHAT ARE THE POSSIBLE VALUES OF THE PARAMETER WE WANT TO FIX?
A_values = pd.unique(data[['A']].values.ravel())
rho_values = pd.unique(data[['rho']].values.ravel())
eta_values = pd.unique(data[['eta']].values.ravel())
print('The possible values of A are: \n A = ', A_values, '\n \n')
print('The possible values of rho are: \n rho = ', rho_values, '\n \n')
print('The possible values of eta are: \n eta = ', eta_values, '\n \n')


###############################################################################
## INPUT OUTPUT MODE (Doesn't work at Cadarache)                             ##
###############################################################################
if Input_Output_Mode:
    
    # SET THE PARAMETER YOU WANT TO FIX AND ITS VALUE:
    print('Which is the parameter that you want to fix? \n \n')
    Fix = input('Eneter the parameter in the following format: data.parameter \n')
    print('You entered:  ', Fix, '\n \n')
    #time.sleep(3)
    print('Remainding its possible values: \n')
    if Fix == data.A:
        print('The possible values of A are: \n A = ', A_values, '\n')
    elif Fix == data.rho:
        print('The possible values of rho are: \n rho = ', rho_values, '\n')
    elif Fix == data.eta:
        print('The possible values of eta are: \n eta = ', eta_values, '\n')
    else:
        Exception(ValueError("You didn't chose a parameter correctly" ))
    time.sleep(3)
    print('Which is the value of the parameter that you want to fix? \n \n')
    Value = input('Enter the value, chose between teh above-showed:  \n')
    print('You entered:  ', Value)
    time.sleep(2)
    
###############################################################################
## END OF INPUT OUTPUT MODE (Doesn't work at Cadarache)                      ##
###############################################################################

else:
    # SET THE PARAMETER YOU WANT TO FIX AND ITS VALUE:
    Fix = data.rho
    Value = 0.05

# wE CAN NOW FILTER THE DATAFRAME:
data_desired = data[Fix == Value]
# CHECK THAT THE NEW DATAFRAME SEEMS CORRECT:
print(data_desired.head(10))
# WRITE INTO THE NEW .TXT FILE:
data_desired.to_csv('GC2Dt_diffusion_gc_Desired_Lines.txt', sep = ' ', index=False)
