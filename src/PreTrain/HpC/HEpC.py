#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import math
def generateWB(P,M):
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
   
    return center

def HEpC(P,T,M=0):
    dendrite = []
    counter = 0
    classes = np.unique(T)
    
    if (len(classes)>0  and len(classes)<=2):
        covariances = np.zeros((1,np.shape(P)[1],np.shape(P)[1]))
        centroids = np.zeros((1,1,np.shape(P)[1]))
        for c in range(1):
            indexClasses = np.where(T==c)[0]
            covariances[c] = np.cov(P[indexClasses, :].T)
           

            if(len(indexClasses)==1):
                continue
            Pclass = P[indexClasses]

            center = generateWB(Pclass,M)
            

            if counter == 0:
                center_arr = center
        centroids[0][0] = np.array(center_arr)
   
      
            
    if (len(classes)>2):
        covariances = np.zeros((len(classes),np.shape(P)[1],np.shape(P)[1]))
        centroids = np.zeros((len(classes),1,np.shape(P)[1]))
        for c in classes:
            indexClasses = np.where(T==c)[0]
            covariances[c] = np.cov(P[indexClasses, :].T)
           

            if(len(indexClasses)==1):
                continue
            Pclass = P[indexClasses]

            center = generateWB(Pclass,M)
          
            centroids[counter][0] = np.array(center)
                

            counter += 1
    
    dendrite = covariances,centroids       
    return dendrite