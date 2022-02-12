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
from sklearn.decomposition import PCA

def extractData(filePath):
    #...... Purpose: data wranging
    df = pd.read_csv(filePath,header=None)
    print(df.head())
    dim = df.shape
    rows = dim[0]
    cols = dim[1]
    data = df.iloc[1:rows,1:cols]
    tdata = data.transpose()
    return tdata

def PCAfunc(tdata): 
    #..... calculates variance ratios for all components and determines no of dimensions needed to capture 75% var
    covarMatrix = PCA(n_components=5) # because 5 features in the dataset
    covarMatrix.fit(tdata)
    varianceRatios = covarMatrix.explained_variance_ratio_ #get variance ratios
    variance = covarMatrix.get_covariance() # Compute data covariance with the generative model
    var = np.cumsum(np.round(covarMatrix.explained_variance_ratio_,decimals=3)*100) #calculate variance ratio percent
    # plot all variance ratios
    plt.ylabel('% Variance Explained')
    plt.xlabel('# of Features')
    plt.title('PCA Analysis')
    plt.ylim(30,100.5)
    plt.style.context('seaborn-whitegrid')
    plt.plot(var)
    # components needed to capture 75% variance
    dim = 0
    targetVar = 0
    for i in var:
        if i>=75:
            break
        else:
            targetVar = targetVar + i 
            dim = dim + 1
    return dim

# def plotbygroup: 
# def plotRE(tdata,dim):
#     X = tdata - tdata.mean()
#     print(X)


if __name__ == "__main__":
    filePath = "/Users/zsj24/GitHub/ML-Methods/PCA/diseases_subset.csv"
    data = extractData(filePath)
    noOfDimensions = PCAfunc(data)
    print("Number of dimensions needed to captute 75% variance: ", noOfDimensions)


