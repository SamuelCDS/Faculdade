close all
clear all
clc
pkg load image

img = imread('img.jpeg');
n = 3;
h = fspecial('average', [n n]);

img1 = imnoise(img, 'salt & pepper');
s = imfilter(img, h, 'replicate','same');
me = medfilt2(img1, [n n]);
figure, imshow(img);
#figure, imshow(s);
figure, imshow(me);
