% Demo 3: kmeans-based clustering for color image segmentation
close all;
x=imresize(imread('basketball2.jpg'),.5);
imshow(x); 
[M,N,K]=size(x);

% criar os vetores de dados (R,G,B) 
y=double(reshape(x,M*N,K));

% chamar a função kmeans
num_cluster=3;
Idx=kmeans(y,num_cluster);
for i=1:num_cluster
    imshow(reshape(Idx==i,M,N));
    pause;
end

