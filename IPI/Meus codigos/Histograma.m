close all
clear all
clc
pkg load image

img = imread('foto.jpg');
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
y = 255 * (x-(132-130)) / ((132+130) - (132-130));
y = uint8(y);

figure, imshow(img);
figure, imhist(img);
figure, imshow(y);
figure, imhist(y);
