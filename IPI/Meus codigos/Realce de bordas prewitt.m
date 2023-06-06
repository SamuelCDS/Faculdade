close all
clear all
clc
pkg load image

img = imread("img.jpeg");

pH = fspecial('prewitt');
P_H = filter2(pH, img, 'same');

P_H = abs(P_H);

pV = pH;
P_V = filter2(pV, img, 'same');
P_V = abs(P_V);
P_H_V = P_H + P_V
figure, imshow(P_H, []);
figure, imshow(P_V, []);
figure, imshow(P_H_V, []);

