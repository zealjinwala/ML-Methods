# By Zeal Jinwala
# Date: February 4, 2022
# Purpose: Principle Component Analysis application for Gene expression data analysis
# Data source: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE7307
# Data Description: The data contains samples from different human diseases and from different
#                   tissue types. For each sample, expression values of genes are given.
#                   For this assignment you are provided only with a subset of the diseases.

import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

filePath = "/Users/zsj24/GitHub/ML-Methods/diseases_subset.csv"
df = pd.read_csv(filePath,header=None)
# print(df.head())
dim = df.shape
rows = dim[0]
cols = dim[1]
data = df.iloc[1:rows,1:cols]
# print(data.head(5))
features = df.iloc[0,1:cols]
# print(features)





