close all
clear all
clc
pkg load image

img = imread('img.jpeg');

sH = fspecial('sobel');
S_H = filter2(sH, img, 'same');
S_H = abs(S_H);

sV = sH';
S_V = filter2(sV, img, 'same');
S_V = abs(S_V);

S_H_V = S_H + S_V;

figure, imshow(S_H,[]);
figure, imshow(S_V,[]);
figure, imshow(S_H_V,[]);
