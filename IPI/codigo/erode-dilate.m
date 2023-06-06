im = imread('shapes.tif');
imshow(im); pause;

figure;

%erosao
for i=3:2:11
 SE = strel('disk',i)
 im_e = imerode(im,SE);
 imshow(im_e); pause;
end

for i=3:2:11
 SE = strel('square',i)
 im_e = imerode(im,SE);
 imshow(im_e); pause;
end

 SE = strel('line',10,45)
 im_e = imerode(im,SE);
 imshow(im_e); pause;

 
 SE2 = zeros(7,7)
 SE2(2:7,5:7) = 1;
 SE2(2:3,:) = 1;
 im_e = imerode(im,SE2);
 imshow(im_e); pause;
 
%dilatacao 
 for i=3:2:11
 SE = strel('disk',i)
 im_e = imdilate(im,SE);
 imshow(im_e); pause;
end

for i=3:2:11
 SE = strel('square',i)
 im_e = imdilate(im,SE);
 imshow(im_e); pause;
end

 SE = strel('line',10,45)
 im_e = imdilate(im,SE);
 imshow(im_e); pause;

 
 
 %Abertura e Fechamento
 SE = strel('disk',7);
 im_o = imopen(im, SE);
 imshow(im_o); pause;

  SE = strel('disk',7);
 im_c = imclose(im, SE);
 imshow(im_c); pause;
