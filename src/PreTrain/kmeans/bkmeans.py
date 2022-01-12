
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances


def bkmeans(x_train, y_train, boxes, eps=0.05):

    classes = np.unique(y_train)
    counter = 0
    flag = 0
    

    if len(classes)<=2:
        # Analyzed patterns
        pos = np.where(classes[1] == y_train)[0]
        x = x_train[pos, :]

        # Initial Number of Clusters
        c_num = boxes[counter]

        # Appliying KMeans to the selected class
        kmeans = KMeans(init = 'k-means++', n_clusters = c_num, n_init = 10, max_iter = 100)
        kmeans.fit(x)
        pattern_labels = kmeans.labels_ 
        clusters = np.unique(pattern_labels)
        print("Clusters n",clusters)
                    
        for cluster in clusters:
           
            indices = np.where(cluster == pattern_labels)[0]
            cluster_points = x[indices,:]
            print("clusters",cluster_points)
            print("Dimensiones",len(cluster_points[0]))
            
            
            for d in range(len(cluster_points[0])):
            
                    cluster_d = cluster_points[:,d:d+1]
                   
                    if flag == 0:
                        Wmin_arr = min(cluster_d)-eps
                        Wmax_arr = max(cluster_d)+eps

                    else:
                        Wmin_arr = np.concatenate((Wmin_arr, min(cluster_d)-eps), axis = 0)
                        Wmax_arr = np.concatenate((Wmax_arr, max(cluster_d)+eps), axis = 0)
                    flag += 1 
                        
#        
    
    if len(classes)>2:
        for classe in classes:

            # Analyzed patterns
            pos = np.where(classe == y_train)[0]
            x = x_train[pos, :]

            # Initial Number of Clusters
            c_num = boxes[counter]

            # Appliying KMeans to the selected class
            kmeans = KMeans(init = 'k-means++', n_clusters = c_num, n_init = 10, max_iter = 100)
            kmeans.fit(x)
            pattern_labels = kmeans.labels_ 
            clusters = np.unique(pattern_labels)
            
            
            for cluster in clusters:
               

                indices = np.where(cluster == pattern_labels)[0]
                cluster_points = x[indices,:]
                
                
                #Para cada dimension de cada cluster
                for d in range(len(cluster_points[0])):
                    cluster_d = cluster_points[:,d:d+1]
              
                    if flag == 0:
                        Wmin_arr = min(cluster_d)-eps
                        Wmax_arr = max(cluster_d)+eps

                    else:
                        Wmin_arr = np.concatenate((Wmin_arr, min(cluster_d)-eps), axis = 0)
                        Wmax_arr = np.concatenate((Wmax_arr, max(cluster_d)+eps), axis = 0)
                    flag += 1 

            counter += 1
           

    dendrite = Wmin_arr, Wmax_arr         
    return dendrite

