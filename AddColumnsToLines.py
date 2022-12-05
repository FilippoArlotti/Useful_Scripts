# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:47:24 2022

@author: filip
"""
import shutil

add = ' 0 0 0 0 0 0\n'
i = 0
temp = open('temp', 'w')
with open('GC2Dt_diffusion_gc.txt','r') as myfile:
    for line in myfile:
        if i > 1:
            if len(line) < 144:
                line = line.strip('\n')
                newline = line + add
                temp.write(newline)
            else:
                temp.write(line)
        else:
            temp.write(line)
        i = i + 1
temp.close()
shutil.move('temp','GC2Dt_diffusion_gc.txt')

#with open('GC2Dt_diffusion_gc.txt') as myfile:
#   for line in myfile:
#        print(len(line))