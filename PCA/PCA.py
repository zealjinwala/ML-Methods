# By Zeal Jinwala
# Date: February 4, 2022
# Purpose: Principle Component Analysis application for Gene expression data analysis
# Data source: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE7307
# Data Description: The data contains samples from different human diseases and from different
#                   tissue types. For each sample, expression values of genes are given.
#                   For this assignment you are provided only with a subset of the diseases.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def extractData(filePath):
    df = pd.read_csv(filePath,header=None)
    print(df.head())
    dim = df.shape
    rows = dim[0]
    cols = dim[1]
    data = df.iloc[1:rows,1:cols]
    features = df.iloc[0,1:cols]
    return data, features 

def PCAfunc(data): 
    covarMatrix = PCA(n_components=6)# we have 5 features
    covarMatrix.fit(data)
    var = np.cumsum(np.round(covarMatrix.explained_variance_ratio_,decimals=3)*100) #calculate variance ratios
    plt.ylabel('% Variance Explained')
    plt.xlabel('# of Features')
    plt.title('PCA Analysis')
    plt.ylim(30,100.5)
    plt.style.context('seaborn-whitegrid')
    plt.plot(var)
    return var

# def plotbygroup: 



# see how much variance is captured with 2 components
# how many components will gcapture 75% variance? Ans: x components
# what is the reconstruction error with X components

if __name__ == "__main__":
    filePath = "/Users/zsj24/GitHub/ML-Methods/PCA/diseases_subset.csv"
    [data, features] = extractData(filePath)
    tvalues = PCAfunc(data)
