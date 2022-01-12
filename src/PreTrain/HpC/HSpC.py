#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import math


def generateCR(P,M):
    if(len(P)==1):
        print("Can't genarete an Hypersphere with one pattern")
    elif(len(P)==0):
        print("Can't genarete an Hypersphere with no patterns")
       
    center = []
     
    aux_point = [0]*len(P[0])
    
  
    for i in range(len(P[0])):
        Pclass_x = P[:,i] 
        vmax = max(Pclass_x.tolist())
        vmin = min(Pclass_x.tolist())
        dst = (vmax - vmin) / 2.0
        centroid = vmin + dst
        aux_point[i] = vmax
        center.append(centroid)
       
    suma = 0
    for j in range(len(P[0])):
        suma = suma + (aux_point[j] - center[j])**2
    radius =  math.sqrt( suma   )+M
    return center,radius


def HSpC(P,T,M=0):
    dendrite = []
    counter = 0
    classes = np.unique(T)
    
    if (len(classes)>0 and len(classes)<=2):
        for c in classes:
            indexClasses = np.where(T==c)[0]
            
            if(len(indexClasses)==1):
                continue
            Pclass = P[indexClasses]
                      
            center,rad = generateCR(Pclass,M)
            
           
            if counter == 0:
                center_arr = center
                rad_arr = [rad]

            
    if (len(classes)>2):
        for c in classes:
            indexClasses = np.where(T==c)[0]
            
            if(len(indexClasses)==1):
                continue
            Pclass = P[indexClasses]
                      
            center,rad = generateCR(Pclass,M)
          
           
            if counter == 0:
                center_arr = center
                rad_arr = [rad]

            else:
                center_arr = np.concatenate((center_arr, center), axis = 0)
                rad_arr.append(rad)

            counter += 1
            
    dendrite = center_arr,rad_arr       
    return dendrite