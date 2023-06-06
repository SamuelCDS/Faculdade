close all
clear all
clc
pkg load image

img = imread('morf_test.png');
figure, imshow(img), title('Original');

#Segmentação.
min = min(img(:));
max = max(img(:));
a = max - min;
M = mean2(img(:));
d = std2(img(:));
printf('Min: %f\n', min);
printf('Max: %f\n', max);
printf('Med: %f\n', M);
printf('apmpli: %f\n', a);
printf('desvio: %f\n', d);
x = double(img);
y = 255 * (x-(160-150)) / ((160+150) - (160-150));
img = uint8(y);
img = img - graythresh(img, 'otsu');
[junk threshold] = edge(img, 'prewitt');
fudgeFactor = .5;
img = edge(img,'prewitt', threshold * fudgeFactor);
figure, imshow(img), title('Segmentada.');

#Alargamento.
img = imdilate(img, [1 1]);
figure, imshow(img), title('dilated gradient mask');

