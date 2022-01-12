
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

def skmeans(x_train, y_train, ellipses, eps=0.05):

    classes = np.unique(y_train)
    counter = 0
    
    if len(classes)<=2:
        # Analyzed patterns
        pos = np.where(classes[0] == y_train)[0]
        x = x_train[pos, :]

        # Initial Number of Clusters
        c_num = ellipses[counter]

        # Appliying KMeans to the selected class
        kmeans = KMeans(init = 'k-means++', n_clusters = c_num, n_init = 10, max_iter = 100)
        kmeans.fit(x)
        centroids = np.reshape(kmeans.cluster_centers_, (c_num, 1, np.shape(x_train)[1]))
       
        pattern_labels = kmeans.labels_ 
        clusters = np.unique(pattern_labels)
             
        radius = np.zeros(c_num,)
       
         
        for cluster in clusters:

            indices = np.where(cluster == pattern_labels)[0]
            dsts = euclidean_distances(x[indices, :], centroids[cluster]) 
            radius[cluster] = max(dsts)
            
        
        if counter == 0:
            centroids_arr = centroids
            radius_arr = radius+eps

        else:
            centroids_arr = np.concatenate((centroids_arr, centroids), axis = 0)
            radius_arr = np.concatenate((radius_arr,radius+eps),axis = 0)

        counter += 1
    

    
    if len(classes)>2:
        for classe in classes:

            # Analyzed patterns
            pos = np.where(classe == y_train)[0]
            x = x_train[pos, :]

            # Initial Number of Clusters
            c_num = ellipses[counter]

            # Appliying KMeans to the selected class
            kmeans = KMeans(init = 'k-means++', n_clusters = c_num, n_init = 10, max_iter = 100)
            kmeans.fit(x)
            centroids = np.reshape(kmeans.cluster_centers_, (c_num, 1, np.shape(x_train)[1]))
           
            pattern_labels = kmeans.labels_ 
            clusters = np.unique(pattern_labels)
            
            radius = np.zeros(c_num)
           
            
            for cluster in clusters:

                indices = np.where(cluster == pattern_labels)[0]
                dsts = euclidean_distances(x[indices, :], centroids[cluster]) 
                radius[cluster] = max(dsts)

           

            if counter == 0:
                centroids_arr = centroids
                radius_arr = radius + eps

            else:
                centroids_arr = np.concatenate((centroids_arr, centroids), axis = 0)
                radius_arr = np.concatenate((radius_arr,radius + eps),axis = 0)

            counter += 1
          
    dendrites = centroids_arr,radius_arr        

    return dendrites
