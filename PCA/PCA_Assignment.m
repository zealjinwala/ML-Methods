%% PCA
% by Felix Agbavor, Zeal Jinwala
clc
clear
close all
% In this assignment you will analyze gene expression data available at:
% https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE7307
% The data contains samples from different human diseases and from different
% tissue types. For each sample, expression values of genes are given.
% For this assignment you are provided only with a subset of the diseases.

%%
% download the data file. Nothing for you to change here.
file = bmes.downloadurl('http://sacan.biomed.drexel.edu/lib/exe/fetch.php?media=course:ml:data:diseases_subset.xlsx');

%% Load the data
% Read the data from the file and convert it into a usable format.
df = readcell(file);

%% PCA Visualization
% Visualize (in 2D) the provided dataset.
% Use a scatter-plot where each point represents a sample. Use a different
% color and/or marker for each disease. Samples from the same disease should
% have the same color and/or marker.

df_no_gene = df(2:end,2:end);
[PC,Y,variance] = pca(cell2mat(df_no_gene)');
x = Y(:,1);
y = Y(:,2);
groups = df(1,2:end)';
gscatter(x,y,groups,['r','g','m','b','k'],['o','+','<','h','v']);

var_pc1 = num2str(round((variance(1)/sum(variance))*100,2));
var_pc2 = num2str(round((variance(2)/sum(variance))*100,2));

xlabel(strcat('PC1(',var_pc1,'%)'))
ylabel(strcat('PC2(',var_pc2,'%)'))
%% Interpret
% Answer these questions below each question, using comments and/or
% any supporting programming code. 



%%
% Samples from which disease are the most tightly clustered in the 2D PCA plot?
% Support your observation with quantitative analysis.

% From the graph, Parkinson's Disease is the disease most tightly clustered
% together. 

groups_str = string(groups);
dist_rh = cluster_val(x,y,'Rheumatoid arthritis', groups_str);
fprintf('Cluster distance value Rheumatoid arthritis: %f\n',dist_rh);

dist_endo = cluster_val(x,y,'Endometriosis', groups_str);
fprintf('Cluster distance value Endometriosis: %f\n',dist_endo);

dist_park = cluster_val(x,y,"Parkinson's disease", groups_str);
fprintf("Cluster distance value Parkinson's disease: %f\n",dist_park);

dist_neuro = cluster_val(x,y,"Neuromuscular pain", groups_str);
fprintf("Cluster distance value Neuromuscular pain: %f\n",dist_neuro);

dist_cancer = cluster_val(x,y,"Breast cancer", groups_str);
fprintf("Cluster distance value Breast cancer: %f\n\n",dist_cancer);

%%
% How many dimensions should one keep (and not necessarily visualize) in
% order to capture at least a total of 75% of the variance in the original dataset ?
dim = 0;
vari = 0;
for i=1:size(variance,1)
    if vari >= 75
        break
    else 
        curvar = variance(i)/sum(variance) * 100;
        vari = vari + curvar;
        dim = dim + 1;
    end
end
disp("dimensions needed to capture atleast 75% variance: "+num2str(dim));
%%
% What is the reconstruction error if we used the first 3 principal
% components to represent the dataset ?
% Remember to compare the reconstructed data, not with the "original data",
% but with the "mean-shifted original data".
X = cell2mat(df_no_gene)' - mean(cell2mat(df_no_gene)');  % "mean-shifted original data"
i = 3;
X2=Y(:,1:i)*PC(:,1:i)';
figure(i+2);
plot(X(:,1),X(:,2),'sb');
hold on;
plot(X2(:,1),X2(:,2),'xr','LineWidth',2);
title(sprintf('reconstruction with %d components',i));
grid on; axis square;
fprintf('Reconstruction error using %d components: %f\n',i,sqrt(mean(sum((X-X2).^2,2))));



