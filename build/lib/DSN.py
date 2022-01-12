#!/usr/bin/env python
# coding: utf-8

# In[6]:


from keras.engine.topology import Layer
from keras import activations
from keras.initializers import RandomUniform
from keras import backend as K
import numpy as np
import tensorflow as tf
from keras import initializers

class DSNlayer(Layer):
    
    def __init__(self, spheres, dendrites = [], activation = None, **kwargs):
        
        self.spheres = spheres
        self.dendrites = dendrites
        self.activation = activations.get(activation)
        if len(dendrites) == 2:
            self.spheres = len(dendrites[1])
        
        
        
        super(DSNlayer, self).__init__(**kwargs)

        
    def build(self, input_shape):
        
        
        if len(self.dendrites) == 0:
           
            
            self.centroid = self.add_weight(name='Centroids', 
                                      shape=(self.spheres,1,input_shape[1]), 
                                      initializer = RandomUniform(minval=-1, maxval=1, seed=None),
                                      trainable = True)
           
        
            self.radius = self.add_weight(name = 'Radius', 
                                      shape = (self.spheres,1),
                                      initializer = RandomUniform(minval=-1, maxval=1, seed=None),
                                      trainable = True)
           
            
        if len(self.dendrites) == 2:
            
                
            self.centroid = self.add_weight(name='Centroids', 
                                      shape=(self.spheres,1,input_shape[1]), 
                                      initializer = initializers.Constant(value = self.dendrites[0]),
                                      trainable = True)
            
        
            self.radius = self.add_weight(name = 'Radius', 
                                      shape = (self.spheres,1),
                                      initializer = initializers.Constant(value = self.dendrites[1]),
                                      trainable = True)
                
        
        super(DSNlayer, self).build(input_shape) 

    
    def call(self, x):
        
        x = K.expand_dims(x, axis = 0)
       
        x = K.repeat_elements(x,int(np.shape(self.centroid)[0]),0)
      
        dif = x-self.centroid
       
        distance = tf.norm(dif,axis=2)
      
        
        output=self.radius-(distance)
        output = K.permute_dimensions(output, (1, 0))
        
        if self.activation is not None:
          output = self.activation(output)
        return output
    
    def compute_output_shape(self, input_shape):
        
        return (input_shape[0], int(np.shape(self.radius)[0]))
      
    def get_config(self):
        
        config = super().get_config().copy()
        config.update({
            'spheres' : self.spheres,
            'activation' : self.activation,
        })
        return config


# In[ ]:




