close all
clear all
clc
pkg load image

#Leitura da imagem.
img = imread('pcb.tif');
figure, imshow(img), title('Imagem Original.');

#Segmentação.
[junk threshold] = edge(img, 'canny');
fudgeFactor = 0.5;
Segmentada = edge(img, 'canny', 0.0001);
#h = [0 -1 0; -1 5 -1; 0 -1 0]
#L = filter2(h, img, 'same');
#L = abs(L);
#Segmentada = L, [];
figure, imshow(Segmentada), title('Máscara de Gradiente.');

#Dilatação da imagem.
Seg_dil = imdilate(Segmentada, [1 1 1 1]);
figure, imshow(Seg_dil), title('Máscara de Greadiente Dilatada.');

#Prencher buracos.
Seg_pre = imfill(Seg_dil, 'holes');
figure, imshow(Seg_pre), title('Imagem Binarizada com buracos preenchidos.');

#Remover objetos conectados na borda.
Seg_SB= imclearborder(Seg_pre, 26);
figure, imshow(Seg_SB), title('Imagem Bordas Limpas.');

#Aplicando Erosão.
seD = strel('diamond',1);
I_F = imerode(Seg_SB,seD);
I_F = imerode(I_F,seD);
figure, imshow(I_F), title('segmented image');

#Achando perimetro.
BWoutline = bwperim(I_F);
Segout = img;
Segout(BWoutline) = 255;
figure, imshow(Segout), title('outlined original image');
