clear all
close all
clc
pkg load image

rgb = imread('pcb.jpg');
figure, imshow(rgb), title('Original');

d = drawLine(LINE);
pos = d.Position;
diffPos = diff(pos);
diameter = hypot(diffPos(1),diffPos(2))

[centers,radii] = imfindcircles(rgb,[20 25],'ObjectPolarity','dark');

[centers,radii] = imfindcircles(rgb,[20 25],'ObjectPolarity','dark', 'Sensitivity',0.9);

figure, imshow(rgb);
h = viscircles(centers,radii);
length(centers);
[centers,radii] = imfindcircles(rgb,[20 25],'ObjectPolarity','dark', ...
          'Sensitivity',0.92,'Method','twostage');

delete(h)
h = viscircles(centers,radii);

[centers,radii] = imfindcircles(rgb,[20 25],'ObjectPolarity','dark', ...
          'Sensitivity',0.95);

delete(h)
viscircles(centers,radii);

