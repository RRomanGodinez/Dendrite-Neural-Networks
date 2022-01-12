#!/usr/bin/env python
# coding: utf-8

# In[2]:


from keras.engine.topology import Layer
from keras import backend as K
from keras.initializers import Constant
from keras.initializers import RandomUniform
from keras import activations
import numpy as np

class DMNlayer(Layer):
    def __init__(self, units,dendrites = [], activation=None, **kwargs):
        
        
        self.units = units   #Number of dendrites
        self.dendrites = dendrites
        self.activation = activations.get(activation)
        if len(dendrites) == 2:
            self.units = int(len(dendrites[0]))
    
        super(DMNlayer, self).__init__(**kwargs)

    def build(self, input_shape):
        
        
        if len(self.dendrites) == 0:
            
            self.Wmin = self.add_weight(name='Wmin', 
                                      shape=(self.units, input_shape[1]),
                                      initializer=RandomUniform(minval=-2, maxval=-0.1, seed=None),
                                      trainable=True)
            self.Wmax = self.add_weight(name='Wmax', 
                                      shape=(self.units, input_shape[1]),
                                      initializer=RandomUniform(minval=0.1, maxval=0.5, seed=None),
                                      trainable=True)

        if len(self.dendrites) == 2:
            
            self.Wmin = self.add_weight(name='Wmin', 
                                      shape=(int(self.units/input_shape[1]), input_shape[1]),
                                      initializer = Constant(value = self.dendrites[0]),
                                      trainable=True)
           
            self.Wmax = self.add_weight(name='Wmax', 
                                      shape=(int(self.units/input_shape[1]), input_shape[1]),
                                      initializer= Constant(value = self.dendrites[1]),
                                      trainable=True)
        
        
            
            
        super(DMNlayer, self).build(input_shape) 

    def call(self, x):
        
        Q = K.int_shape(x)[0]
        if Q is None: Q = 1
        
      
       
        X = K.repeat(x,np.shape(self.Wmin)[0])
        
        Wmin = K.permute_dimensions(K.repeat(self.Wmin, Q), (1,0,2))
       
        L1 = K.min(X - Wmin, axis=2)
       
        Wmax = K.permute_dimensions(K.repeat(self.Wmax, Q), (1,0,2))
        L2 = K.min(Wmax - X, axis=2)
        output = K.minimum(L1,L2)
        if self.activation is not None:
            output = self.activation(output)
        return output
        
        
    
    def compute_output_shape(self, input_shape):
        return (input_shape[0],self.units) 

    def get_config(self):
        config = super(DMNlayer, self).get_config()
        config.update({"units": self.units,
                       "activation":self.activation})
        return config
    
    def valWmin(self):
        print("Wmin:",self.Wmin)
    
    def valWmax(self):
        print("Wmax:",self.Wmax)


