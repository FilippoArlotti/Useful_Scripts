# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:10:15 2022

@author: filip
"""
import glob, os
import matplotlib.pyplot as plt
import numpy as xp
import pandas as pd

#os.system('cls')
#plt.close()

####### EDITABLE PART ######################################
#Plot Style Setting
font_title = 40
font_axis = 0.60*font_title
font_info = 0.60*font_title
L = 10
cols = ['b','r','k','m']
cols_dot = [':bo',':ro',':ko',':mo']
#2D Plots Mode
HEATMAP = 0
CONTOURF = 0
SURF = 0
SURF_2 = 0
CONTOURF_2 = 0
#1D Plots mode
Heatmap = 'on'
Grid = 'on'
#Fixed Parameter
Fixed = 'A'# OPTIONS: A  // ETA // RHO
#Now we define the palette of color of certain plots and we define
# the xlim and ylim certain graphs:
col = [0.0000, 0.4470, 0.7410, 0.4667, 0.6745, 0.1882,
0.4667, 0.6745, 0.1882, 0.4941, 0.1843, 0.5569, 1.0000,
0.0000, 0.0000, 1.0000, 0.0000, 0.0000]
grad_col = 50

lim_y_min  = [0.00, 0.00,  0.00, 0.00,  0.00, 0.99, 0.99, 0.00, 0.00, 0.00, 1.00, 0.99,  0.99]
lim_y_max  = [0.50, 0.60,  0.10, 0.10,  2.00, 1.00, 1.00, 0.40, 1.50, 1.00, 3.00, 1.00,  1.00]
lim_y_min2 = [0.00, 0.00,  0.00, 0.00,  0.65, 0.99, 0.99, 0.00, 0.00, 0.00, 1.00, 0.99,  0.99]
lim_y_max2 = [0.43, 0.50, 0.075, 0.075, 2.00, 1.00, 1.00, 0.40, 1.50, 1.00, 3.00, 1.00,  1.00]
sy = ['Trapped (\#)','Diffusive (\#)','$D$','$a$','$b$','$R^2(diff)$','$R^2(interp)$','Ballistic (\#)','$D$','$a$','$b$','$R^2(diff)$','$R^2(interp)$']

####### END OF EDITABLE PART ######################################

#Diffusion Table Importing And Reading

if HEATMAP + SURF + SURF_2 + CONTOURF + CONTOURF_2 > 1:
    raise ValueError('Only 1 type of graph allowed')
#os.chdir("wdir")
for file in glob.glob("*.txt"):
    print(file)
VarNames = ['A', 'rho', 'eta', 'Trapped','Diffusive','D_diff', 'a_diff', 'b_diff', 'R2(diff)_d','R2(interp)_d','Ballistic','D_ball', 'a_ball', 'b_ball', 'R2(diff)_ball','R2(interp)_ball']
tab = pd.read_table(file, header=None, skiprows=[0, 1], sep=' ')
tab.columns =  ['A', 'rho', 'eta', 'Trapped','Diffusive','D_diff', 'a_diff', 'b_diff', 'R2(diff)_d','R2(interp)_d','Ballistic','D_ball', 'a_ball', 'b_ball', 'R2(diff)_ball','R2(interp)_ball']
vars = ['$A$', '$\rho$', '$\eta$', 'Trapped ($\%$)','Diffusive ($\%$)','$D\_diff$','$a\_diff$','$b\_diff$','$R^2(diff)\_diff$','$R^2(interp)\_diff$','Ballistic ($\%$)','$D\_ball$','$a\_ball$','$b\_ball$','$R^2(diff)\_ball$','$R^2(interp)\_ball$']
#0.800000(tab)

#Nella seguente minisezione si costruiscono tre vettori colonna associati ad
# e  contenente tutti i possibili valori di questi ultimi ritrovati nel file.
A = tab['A'].unique()
rho = tab['rho'].unique()
eta = tab['eta'].unique()
#Array conversion
tab_array = tab.to_numpy()
#print(tab_array)
#DATA PLOTS
#This part of code is needed to fix one of the parameters. We may want to plot different figures while fixing one of 
#the values despite the fact we have different values of this in the txt file. From a very big simulation we can get only certain data. 
#If we simulate with one of the parameter fixed then it is required to chose p as that parameter. Strictly necessary.
#If we simulate with all parameters varying then p is fixing the parameter of which all possible values will be detected.
#The number of these ones is equal to the number of tables that will be built, one for each value of the fixed parameter.
#From each of these tables it is possible to plot the figures to compare how the others parameters influence the solution 
#for different values of the fixed one, may happen that for example  influence more if eta is high.... 

#REMINDER:    1 = A // 2 = rho / 3 = eta

if Fixed == 'A':
    p = 0
elif Fixed == 'RHO':
    p = 1
elif Fixed == 'ETA':
    p = 2
else:
    raise ValueError("You didn't fix a parameter correctly, check line 33 of the code")
if p == 2:
    p1 = 0
    p2 = 1
    xy = [chr(vars[0]), chr(vars[1]), chr(vars[2])];
    fixed = eta
    par1 = A
    par2 = rho
    Tval = tab.eta
elif p == 1:
    p1 = 0
    p2 = 2
    xy = [vars[0], vars[2], vars[1]]
    fixed = rho
    par1 = A
    par2 = eta
    Tval = tab.rho
elif p == 0:
    p1 = 1
    p2 = 2
    xy = [vars[1], vars[2], vars[0]]
    fixed = A
    par1 = rho
    par2 = eta
    Tval = tab.A
#The following lines generate a table for each value of the fixed parameter. The parameter 
#on the right of the fixed one determines the sorting of the rows. A table for a fixed value 
#of  is sorted on the values of  for example not on ... Check it out in variable TAB 
#TAB = xp.array(xp.zeros(int(xp.size(tab_array,0) / xp.size(fixed,0)),16,xp.size(fixed,0) ))
#TAB = xp.array([[[0 for k in range(xp.size(tab_array,0))] for j in range(16)] for i in range(xp.size(fixed,0))])
TAB = xp.array(xp.zeros((xp.size(tab_array,0),xp.size(tab_array,0))))
#print(TAB)

TAB = TAB.reshape(xp.size(TAB,0),16,xp.size(fixed,0))
#print(xp.shape(TAB))
for i in range(xp.size(tab_array,0)):
    for j in range(xp.size(fixed,0)):
        if Tval[i]==fixed[j]:
        #TAB[i-j*int(xp.size(TAB,0) / xp.size(fixed,0)),:,j] = tab_array[i,:]
            TAB[i,:,j] = tab_array[i,:]
    #if Tval[i]==fixed[1]:
        #TAB[i,:,1] = tab_array[i,:]
#print(xp.shape(TAB))
#print(TAB[:,:,0])
#print(TAB[:,:,1])
a = 3
#Generating data matrices:
#The data matrices are generated from TAB, with this procedure we eliminate the rows of TABs who have zero lines.
# This happens when in the simulations we didn't vary all three parameters and I am not fixing in line 19 the 
#parameter that was fixed in the simulations. It let be available matrices that otherwise would have been not usable.
#TAB = TAB.reshape(xp.size(TAB,0),16,xp.size(fixed,0))
data = xp.array(xp.zeros((int(xp.size(tab_array,0) / xp.size(fixed,0)),xp.size(tab_array,0))))
data = data.reshape(int(xp.size(tab_array,0) / xp.size(fixed,0)),16,xp.size(fixed,0))
for k in range(xp.size(TAB,2)):
    j = 0
    for r in range(xp.size(TAB,0)):
        if not xp.average(TAB[r,:,k],0) == 0:
            data[j,:,k] = TAB[r,:,k]
            j = j + 1
#  SINGLE MATRIX ANALYSIS
#Now it start the analysis of each matrix generated by the fixing of a parameter:
for k in range(xp.size(TAB,2)):
    I = xp.argsort(data[:,p1,k])
    data[:,p1,k] = xp.sort(data[:,p1,k])
    data[:,p2,k] = data[I,p2,k]
    for h in range(3,int(xp.size(data[0,:,k]))):
        data[:,h,k] = data[I,h,k]
        
        
mat_y, mat_z = xp.zeros((4,4)), xp.zeros((4,4))
x, y = xp.zeros((len(par1),int(xp.size(tab_array,1))-3)), xp.zeros((len(par2),int(xp.size(tab_array,1))-3))
z = xp.zeros(len(par1)*len(par2)*(int(xp.size(tab_array,1))-3))
z = xp.reshape(z,(len(par1),len(par2),int(xp.size(tab_array,1))-3))
for k in range(xp.size(TAB,2)):
    vx, vy = data[:,p1,k], data[:,p2,k]
    for h in range(3,int(xp.size(data[0,:,k]))):
        vz = data[:,h,k]
        counter = 0
        for ii in range(0, len(par1)):
            for jj in range(0, len(par2)):
                mat_y[ii, jj] = vy[counter + jj -1]
                mat_z[ii, jj] = vz[counter + jj -1]
            mat_y[ii, :], I2 = xp.sort(mat_y[ii, :]), xp.argsort(mat_y[ii, :])
            mat_z[ii, :] = mat_z[ii, I2]
            counter = counter + len(par2)
        
        hh = h - 4 + 1
        x[:,hh] = xp.unique(vx)
        y[:,hh] = mat_y[0,:]
        z[:,:,hh] = xp.transpose(mat_z)
        
        
       