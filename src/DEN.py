#!/usr/bin/env python
# coding: utf-8

# In[4]:


from keras.engine.topology import Layer
from keras import backend as K
from keras import initializers
from keras.initializers import RandomUniform
from keras import activations
import numpy as np
import tensorflow as tf

class DENlayer(Layer):
    
    def __init__(self,ellipses=0, dendrites = [] , activation = None, *args , **kwargs):
        
        self.ellipses = ellipses
        self.dendrites = dendrites
        self.activation = activations.get(activation)
        
        if len(dendrites) == 2:
            self.ellipses =int(np.shape(self.dendrites[0])[0])     
                   
        
        super(DENlayer, self).__init__(**kwargs)
       

            
    def build(self, input_shape):
      
        
        if len(self.dendrites) == 0:
           
            self.Centroids = self.add_weight(name='Centroids', 
                                         shape=(self.ellipses, 1, input_shape[1]), 
                                         initializer = RandomUniform(minval=-0.5, maxval=0.5, seed=None),
                                         trainable = True)
        
            self.Sigmas = self.add_weight(name = 'Sigmas', 
                                          shape = (self.ellipses, input_shape[1], input_shape[1]),
                                          initializer = RandomUniform(minval=0.01, maxval=1, seed=None),
                                          trainable = True)
            
            
        if len(self.dendrites) == 2:
           
            
            self.Centroids = self.add_weight(name='Centroids', 
                                  shape=([self.ellipses, int(np.shape(self.dendrites[1])[1]), int(np.shape(self.dendrites[1])[2])]), 
                                  initializer = initializers.Constant(value = self.dendrites[1]),
                                  trainable = True)
        
            self.Sigmas = self.add_weight(name = 'Sigmas', 
                                  shape = ([self.ellipses, int(np.shape(self.dendrites[0])[1]),
                                            int(np.shape(self.dendrites[0])[2])]),
                                            initializer = initializers.Constant(value = self.dendrites[0]),
                                            trainable = True)
           
           
        
        super(DENlayer, self).build(input_shape) 

    
    def call(self, x):
        
        x = K.expand_dims(x, axis = 0)
        
        x = K.repeat_elements(x, int(np.shape(self.Centroids)[0]), 0)
        
        
        
        dif = x - self.Centroids
        
        difT = K.permute_dimensions(dif, (0, 2, 1))
                
        mah = K.batch_dot(dif, tf.linalg.inv(self.Sigmas))
        mah = K.batch_dot(mah, difT)

        
        diag = tf.linalg.diag_part(mah)
        output = K.permute_dimensions(diag, (1, 0))

       
        if self.activation is not None:
            
           output = self.activation(output)

        return output

    
    def compute_output_shape(self, input_shape):
        
        return (input_shape[0], int(np.shape(self.Centroids)[0]))
      
    def get_config(self):
        
        config = super().get_config().copy()
        config.update({
            'ellipses' : self.ellipses,
            'activation' : self.activation,
        })
        return config
    
    def printWeights(self):
        print("centroids:",self.Centroids)
        print("sigmas:",self.Sigmas)
         

  
    







