
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

def ekmeans(x_train, y_train, ellipses):

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
        print("centroid:",centroids)
        pattern_labels = kmeans.labels_ 
        clusters = np.unique(pattern_labels)
        covariances = np.zeros((c_num, np.shape(x_train)[1], np.shape(x_train)[1]))
        
        for cluster in clusters:

            indices = np.where(cluster == pattern_labels)[0]
            covariances[cluster] = np.cov(x[indices, :].T)

        print("Covariances:",covariances)

        if counter == 0:
            covariances_arr = covariances
            centroids_arr = centroids

        else:
            covariances_arr = np.concatenate((covariances_arr, covariances), axis = 0)
            centroids_arr = np.concatenate((centroids_arr, centroids), axis = 0)

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
            covariances = np.zeros((c_num, np.shape(x_train)[1], np.shape(x_train)[1]))
            
            for cluster in clusters:

                indices = np.where(cluster == pattern_labels)[0]
                covariances[cluster] = np.cov(x[indices, :].T,bias=True)

            

            if counter == 0:
                covariances_arr = covariances
                centroids_arr = centroids

            else:
                covariances_arr = np.concatenate((covariances_arr, covariances), axis = 0)
                centroids_arr = np.concatenate((centroids_arr, centroids), axis = 0)

            counter += 1
            
    dendrite = covariances_arr, centroids_arr
    return dendrite

