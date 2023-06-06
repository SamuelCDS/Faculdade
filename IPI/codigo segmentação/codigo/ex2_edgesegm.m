% Demo II: edge-based segmentation
% Passo 1: Ler a Imagem
I = imread('lena.tif');
figure, imshow(I), title('original image');

pause;
% Step 2: Detect Entire Cell
% Duas celulas aparecem na imagem, mas somente uma esta inteira
% Queremos segmentar a celula inteira
[junk threshold] = edge(I, 'sobel');
fudgeFactor = .5;
BWs = edge(I,'sobel', threshold * fudgeFactor);
figure, imshow(BWs), title('binary gradient mask');

pause;
% Step 3: Dilate the Image
% Dilatar a imagem para conectar as linhas

se90 = strel('line', 3, 90);
se0 = strel('line', 3, 0);

BWsdil = imdilate(BWs, [se90 se0]);
figure, imshow(BWsdil), title('dilated gradient mask');

pause;
% Step 4: Fill Interior Gaps
% Vamos prencher os buracos com a fun��o imfill

BWdfill = imfill(BWsdil, 'holes');
figure, imshow(BWdfill);
title('binary image with filled holes');

pause;
% Step 5: Remove Connected Objects on Border
% Remover objetos que tocam as bordas: imclearborder

BWnobord = imclearborder(BWdfill, 4);
figure, imshow(BWnobord), title('cleared border image');

pause;
% Step 6: Smoothen the Object
% Para refinar vamos fazer uma eros�o

seD = strel('diamond',1);
BWfinal = imerode(BWnobord,seD);
BWfinal = imerode(BWfinal,seD);
figure, imshow(BWfinal), title('segmented image');

%podemos utilizar a fun��o bwperim para achar o perimetro
BWoutline = bwperim(BWfinal);
Segout = I;
Segout(BWoutline) = 255;
figure, imshow(Segout), title('outlined original image');


