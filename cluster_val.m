function out = cluster_val(x,y,disease_group, groups)
    
    rhematiod_idx = groups == disease_group;
    x_disease = x(rhematiod_idx);
    y_disease = y(rhematiod_idx);
    
    % centroid
    mean_xdisease = mean(x_disease);
    mean_ydisease = mean(y_disease);
    
    dist_disease = sqrt((x_disease - mean_xdisease).^2 + (y_disease - mean_ydisease).^2);
    
    % remove outliers
    [~,TF] = rmoutliers(dist_disease,'percentiles',[10, 90]);
    if(any(TF))
        dist_disease = dist_disease(~TF);
    end
    
    out = sum(dist_disease)/numel(dist_disease);
end