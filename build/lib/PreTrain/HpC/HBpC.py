#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np


def generateWB(P,M):
    if(len(P)==1):
        print("Can't genarete an Hyperbox with one pattern")
    elif(len(P)==0):
        print("Can't genarete an Hyperbox with no patterns")
       
    Wmin = []
    Wmax = []
    
    for i in range(len(P[0])):
        Pclass_x = P[:,i] 
        
        Wmin.append(min(Pclass_x.tolist())-M)
        
        Wmax.append(max(Pclass_x.tolist())+M)   
    return Wmin,Wmax

def HBpC(P,T,M=0):
    classes = np.unique(T)
    
    dendrite = []
    counter = 0
    
    if (len(classes)<=2 and len(classes)>0):
        print("Estamos dentro")
        print(classes)
        for c in range(1):
            indexClasses = np.where(T==c)[0]
            
            if(len(indexClasses)==1):
                continue
            Pclass = P[indexClasses]
                      
            Wmin,Wmax = generateWB(Pclass,M)
            print("Wmin:",Wmin,"Wmax:",Wmax)
            
            if counter == 0:
                Wmin_arr = Wmin
                Wmax_arr = Wmax

#             else:
#                 Wmin_arr = np.concatenate((Wmin_arr, Wmin), axis = 0)
#                 Wmax_arr = np.concatenate((Wmax_arr, Wmax), axis = 0)

#             counter += 1
    
    
    if (len(classes)>2):
        for c in classes:
            indexClasses = np.where(T==c)[0]
            
            if(len(indexClasses)==1):
                continue
            Pclass = P[indexClasses]
                      
            Wmin,Wmax = generateWB(Pclass,M)
            print("Wmin:",Wmin,"Wmax:",Wmax)
            
            if counter == 0:
                Wmin_arr = Wmin
                Wmax_arr = Wmax

            else:
                Wmin_arr = np.concatenate((Wmin_arr, Wmin), axis = 0)
                Wmax_arr = np.concatenate((Wmax_arr, Wmax), axis = 0)

            counter += 1
            
    dendrite = Wmin_arr,Wmax_arr       
    return dendrite




# def generateWB(P,M):
#     if(len(P)==1):
#         print("Can't genarete an Hyperbox with one pattern")
#     elif(len(P)==0):
#         print("Can't genarete an Hyperbox with no patterns")
       
#     Wmin = []
#     Wmax = []
    
#     for i in range(len(P[0])):
#         Pclass_x = P[:,i] 
        
#         Wmin.append(min(Pclass_x.tolist())-M)
        
#         Wmax.append(max(Pclass_x.tolist())+M)   
#     return Wmin,Wmax

# def HBpC(P,T,M=0):
#     classes = np.unique(T)
    
#     dendrite = []
#     counter = 0
    
#     if (len(classes)<=2 and len(classes)>0):
      
#         for c in range(1,2):
#             indexClasses = np.where(T==c)[0]
            
#             if(len(indexClasses)==1):
#                 continue
#             Pclass = P[indexClasses]
                      
#             Wmin,Wmax = generateWB(Pclass,M)
           
            
#             if counter == 0:
#                 Wmin_arr = Wmin
#                 Wmax_arr = Wmax

    
    
#     if (len(classes)>2):
#         for c in classes:
#             indexClasses = np.where(T==c)[0]
            
#             if(len(indexClasses)==1):
#                 continue
#             Pclass = P[indexClasses]
                      
#             Wmin,Wmax = generateWB(Pclass,M)
            
            
#             if counter == 0:
#                 Wmin_arr = Wmin
#                 Wmax_arr = Wmax

#             else:
#                 Wmin_arr = np.concatenate((Wmin_arr, Wmin), axis = 0)
#                 Wmax_arr = np.concatenate((Wmax_arr, Wmax), axis = 0)

#             counter += 1
            
#     dendrite = Wmin_arr,Wmax_arr       
#     return dendrite

