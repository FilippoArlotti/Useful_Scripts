# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:10:15 2022

@author: filip
"""
import glob, os
import matplotlib.pyplot as plt
import numpy as xp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#os.system('cls')
#plt.close()

####### EDITABLE PART ######################################

#MODES:
PLOT1D_MODE = False   
PLOT2D_MODE = True
 
#1D Plots Mode
PLOT_PARAM = True

#2D Plots Mode
HEATMAP_MODE = True
CONTOURF = 0
SURF = 0
SURF_2 = 0
CONTOURF_2 = 0

#Nan instead of zeros?
Convert_Zeros = 'on'

#Parameter 1D PARAM PLOT
Parameter = 'RHO'# OPTIONS: A  // ETA // RHO

#Fixed Parameter 2D Plot mode
Fixed_Parameter = 'A'

#Plot Style Setting
Grid = True

#Do you want to save the figures?
SaveFigure = True
Grid = True
dpi = 800

#Manual Axis Range:
Manual_axis = False
if Manual_axis:
    lim_y_min  = [0.00, 0.00,  0.00, 0.00,  0.00, 0.99, 0.99, 0.00, 0.00, 0.00, 0.70    , 0.99,  0.99]
    lim_y_max  = [0.50, 0.60,  0.10, 0.10,  2.00, 1.00, 1.00, 0.40, 1.50, 1.00, 3.00, 1.00,  1.00]
    lim_y_min2 = [0.00, 0.00,  0.00, 0.00,  0.65, 0.99, 0.99, 0.00, 0.00, 0.00, 1.00, 0.99,  0.99]
    lim_y_max2 = [0.43, 0.50, 0.075, 0.075, 2.00, 1.00, 1.00, 0.40, 1.50, 1.00, 3.00, 1.00,  1.00]

sy = ['$Trapped (\%)$','$Diffusive (\%)$','$D$ $diffusive$','$a$ $diffusive$','$b$ $diffusive$','$R^2(diff)$ $diffusive$','$R^2(interp)~diffusive$','$Ballistic (\%)$','$D$ $ballistic$','$a$ $ballistic$','$b$ $ballistic$','$R^2(diff)~ballistic$','$R^2(interp)~ballistic$']


####### END OF EDITABLE PART ######################################

#Diffusion Table Importing And Reading

#os.chdir("wdir")
for file in glob.glob("*.txt"):
    print(file)
VarNames = ['A', 'rho', 'eta', 'Trapped','Diffusive','D_diff', 'a_diff', 'b_diff', 'R2(diff)_d','R2(interp)_d','Ballistic','D_ball', 'a_ball', 'b_ball', 'R2(diff)_ball','R2(interp)_ball']
tab = pd.read_table(file, header=None, skiprows= 2, sep=' ')
tab.columns =  ['A', 'rho', 'eta', 'Trapped','Diffusive','D_diff', 'a_diff', 'b_diff', 'R2(diff)_d','R2(interp)_d','Ballistic','D_ball', 'a_ball', 'b_ball', 'R2(diff)_ball','R2(interp)_ball']
vars = ['$A$', r'$\rho$', '$\eta$', '$Trapped$ ($\%$)','$Diffusive$ ($\%$)','$D\_diff$','$a\_diff$','$b\_diff$','$R^2(diff)\_diff$','$R^2(interp)\_diff$','$Ballistic$ ($\%$)','$D\_ball$','$a\_ball$','$b\_ball$','$R^2(diff)\_ball$','$R^2(interp)\_ball$']


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
if PLOT1D_MODE:
    if Parameter == 'A':
        par = 0
        Par = A
        Tval = tab.A
        P1 = rho
        p1 = 1
        P2 = eta
        p2 =2
    elif Parameter == 'RHO':
        par = 1
        Par = rho
        Tval = tab.rho
        P1 = eta
        p1 = 2
        P2 = A
        p2 =0
    elif Parameter == 'ETA':
        par = 2
        Par = eta
        Tval = tab.eta
        P1 = A
        p1 = 0
        P2 = rho
        p2 =1
    else:
        raise ValueError("You didn't fix a parameter correctly, check line 33 of the code")
    if len(xp.unique(P1)) > 1 and len(xp.unique(P2)) == 1:
        Varying = P1
        Fixed = P2
        column_varying = p1
        column_fixed = p2
        axe = vars[p1]
        fixed_caption = vars[p2]
    elif len(xp.unique(P2)) > 1 and len(xp.unique(P1)) == 1:
        Varying = P2
        Fixed = P1
        column_varying = p2
        column_fixed = p1
        axe = vars[p2]
        fixed_caption = str(vars[p1])
    else:
        raise ValueError("One of the three parameter is not fixed, consider modify .txt file")
    Fixed_string = "%.3f" %Fixed 
if PLOT2D_MODE:
    if Fixed_Parameter == 'A':
        par = 0
        Par = A
        Tval = tab.A
        P1 = rho
        p1 = 1
        P2 = eta
        p2 =2
    elif Fixed_Parameter == 'RHO':
        par = 1
        Par = rho
        Tval = tab.rho
        P1 = eta
        p1 = 2
        P2 = A
        p2 =0
    elif Fixed_Parameter == 'ETA':
        par = 2
        Par = eta
        Tval = tab.eta
        P1 = A
        p1 = 0
        P2 = rho
        p2 =1
    else:
        raise ValueError("You didn't fix a parameter correctly, check line 40 of the code")
    fixed_caption = str(vars[par])
    Xlabel = str(vars[p1])
    Ylabel = str(vars[p2])
#The following lines generate a table for each value of the fixed parameter. The parameter 
#on the right of the fixed one determines the sorting of the rows. A table for a fixed value 
#of  is sorted on the values of  for example not on ... Check it out in variable TAB 

TAB = xp.array(xp.zeros((int(xp.size(tab_array,0) * xp.size(Par,0)),xp.size(tab_array,1))))
TAB = TAB.reshape(int(xp.size(TAB,0) / xp.size(Par,0)) ,xp.size(tab_array,1),xp.size(Par,0))

for i in range(xp.size(tab_array,0)):
    for j in range(xp.size(Par,0)):
        if Tval[i]==Par[j]:
            TAB[i,:,j] = tab_array[i,:]

#Generating data matrices:
#The data matrices are generated from TAB, with this procedure we eliminate the rows of TABs who have zero lines.
# This happens when in the simulations we didn't vary all three parameters and I am not fixing in line 19 the 
#parameter that was fixed in the simulations. It let be available matrices that otherwise would have been not usable.
#TAB = TAB.reshape(xp.size(TAB,0),16,xp.size(fixed,0))
data = xp.array(xp.zeros((xp.size(tab_array,0), xp.size(tab_array, 1))))
data = data.reshape(int(xp.size(tab_array, 0) / xp.size(Par, 0) ),xp.size(tab_array, 1),xp.size(Par, 0))
for k in range(xp.size(TAB,2)):
    j = 0
    for r in range(xp.size(TAB,0)):
        if not xp.average(TAB[r,:,k],0) == 0:
            data[j,:,k] = TAB[r,:,k]
            j = j + 1
#  SINGLE MATRIX ANALYSIS
#Now it start the analysis of each matrix generated by the fixing of a parameter:
if PLOT1D_MODE:
    for k in range(xp.size(TAB,2)):
        I = xp.argsort(data[:, column_varying, k], axis= -1, kind='stable')
        data[:, column_varying, k] = data[I, column_varying, k]
        data[:, column_fixed, k] = data[I, column_fixed, k]
        for h in range(3,int(xp.size(data[0,:,k]))):
            data[:,h,k] = data[I,h,k]

if PLOT2D_MODE:
    for k in range(xp.size(TAB,2)):
        I = xp.argsort(data[:, p1, k], axis= -1, kind='stable')
        data[:, p1, k] = data[I, p1, k]
        data[:, p2, k] = data[I, p2, k]
        for h in range(3,int(xp.size(data[0,:,k]))):
            data[:,h,k] = data[I,h,k]

#We convert zeros to nan if requested:
if Convert_Zeros == 'on':
    tab_array[tab_array == 0.] = xp.nan
    print('The zeros inside the dataframe have been replaced \n')        
 #ANALISI 2D Non Riesco ad ordinare la matrice mat_y allo stesso 
#modo di matlab, I2 e' diverso ==> BOH       
if PLOT2D_MODE:
    a = 0
    mat_y, mat_z = xp.zeros((len(P1),len(P2))), xp.zeros((len(P1),len(P2)))
    x, y = xp.zeros((len(P1),int(xp.size(tab_array,1))-3)), xp.zeros((len(P2),int(xp.size(tab_array,1))-3))
    z = xp.zeros(len(P1)*len(P2)*(int(xp.size(tab_array,1))-3))
    z = xp.reshape(z,(len(P1),len(P2),int(xp.size(tab_array,1))-3))
    for k in range(xp.size(TAB,2)):
        vx, vy = data[:,p1,k], data[:,p2,k]
        for h in range(3,int(xp.size(data[0,:,k]))):
            vz = data[:,h,k]
            counter = 0
            for ii in range(0, len(P1)):
                for jj in range(0, len(P2)):
                    mat_y[ii, jj] = vy[counter + jj -1]
                    mat_z[ii, jj] = vz[counter + jj -1]
                I2 =  xp.argsort(mat_y[ii, :])
                mat_y[ii, :] = mat_y[ii, I2]
                mat_z[ii, :] = mat_z[ii, I2]
                counter = counter + len(P2)      
            hh = h - 4 + 1
            x[:,hh] = xp.unique(vx)
            y[:,hh] = mat_y[0,:]
            #z[:,:,hh] = mat_z.transpose()
            z[:,:,hh] = mat_z
        z = z.transpose((1, 0, 2))

#We convert zeros to nan if requested:
if Convert_Zeros == 'on':
    z[z == 0.] = xp.nan
    print('The zeros inside the dataframe have been replaced \n') 

        
if PLOT1D_MODE:
    if PLOT_PARAM:
        LegendStrings =[None] * xp.size(TAB,2)
        for k in range(xp.size(TAB,2)):
            Parameter_string = "%.3f" %Par[k]
            LegendStrings[k] = str(Parameter) + ' = ' + Parameter_string 
        vx = data[:, column_varying, :]
        for h in range(3,xp.size(TAB,1)):
            vy = data[:,h,:]
            fig, axs = plt.subplots(1,1)
            for k in range(xp.size(TAB,2)):
                plt.plot(vx[:,k],vy[:,k], linestyle='dashed', linewidth = 1, marker='o', markersize=3, label = LegendStrings[k])
            plt.xlabel(axe)
            plt.ylabel(vars[h])
            plt.title('{} ; {} = {} '.format(sy[h-4+1], fixed_caption, Fixed_string))
            if Grid:
                plt.grid(linestyle='--', linewidth = 0.5)
            if Manual_axis:
                plt.ylim([lim_y_min[h-4+1], lim_y_max[h-4+1]])
            else:
                axs.set_aspect('auto', 'box')
            plt.legend(loc = 'best', ncol=2)
            fig.tight_layout()
            plt.show()
            
if PLOT2D_MODE:
    if HEATMAP_MODE:
        a =2
        for k in range(xp.size(TAB,2)):
            Fixed_string = "%.3f" %Par[k]
            Plots =[3, 4, 10, 5, 6, 7, 11, 12, 13]
            for h in Plots:
                hh = h - 4 + 1
                Caption = '{} ; {} = {} '.format(sy[hh], fixed_caption, Fixed_string)
                fig, axs = plt.subplots(1, 1)
                z[:,:,hh] = xp.flip(z[:, :, hh], axis = 0)
                x_axis_labels = xp.linspace(x[0, hh], x[-1, hh], 3)
                y_axis_labels = xp.linspace(y[0, hh], y[-1, hh], 2)
                sns.heatmap(z[:, :, hh], xticklabels = False, yticklabels = False, cmap="viridis")
                axs.set(title = Caption, xlabel = Xlabel, ylabel = Ylabel)
                sns.set(font_scale = 1.2)
                              