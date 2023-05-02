import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
dbs = DBSCAN(eps=0.26, min_samples=10);
#dbs.fit(pca_raisin);

#plt.scatter(pca_raisin[:,0],pca_raisin[:,1], c=dbs.labels_)