a = im2double(rgb2gray(imread('lincon.jpg')));
imshow(a,[]); pause;

b = a > 0.83;
imshow(b,[]); pause;


SE = strel('disk', 4);
b = imopen(b, SE);
imshow(b,[]); pause;

SE = strel('disk', 9);
b = imclose(b, SE);
imshow(b,[]); pause;


b = ~b;
imshow(b,[]); pause;


%borda externa
SE = strel('disk', 3);
b_d = imdilate(b, SE);
borda = b_d - b;
imshow(borda,[]); pause;

c =a ;
c(borda==1) = 1;
figure;imshow(c,[]); pause;



%borda interna
SE = strel('disk', 3);
b_e = imerode(b, SE);
borda2 = b - b_e;
figure;imshow(borda2,[]); pause;


c =a ;
c(borda2==1) = 1;
figure;imshow(c,[]); pause;


