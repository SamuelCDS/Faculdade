close all
clear all
clc
pkg load image

img = imread('img.jpeg');

h = [0 -1 0; -1 4 -1; 0 -1 0]
L = filter2(h, img, 'same');
L = abs(L);

figure, imshow(L, []);
