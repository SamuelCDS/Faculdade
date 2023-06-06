I = imread('im3.jpg');
imshow(I);
title('original');
pause;

I_eq = adapthisteq(I);
figure;
imshow(I_eq);
title('adaptar histograma');
pause;

%binarizar por limiar
bw = im2bw(I_eq, graythresh(I_eq));
figure;
imshow(bw);
title('binarizar por limiar');
pause;

%limpar a imagem, e achar os perimetros (seria um segmentação possivel)
bw2 = imfill(bw,'holes');
bw3 = imopen(bw2, ones(5,5));
bw4 = bwareaopen(bw3, 40);
bw4_perim = bwperim(bw4);
overlay1 = imoverlay(I_eq, bw4_perim, [.3 1 .3]);
figure;
imshow(overlay1);
title('limpar e achar perimetros');
pause;



%identificar os pixels de maior intensidade
mask_em = imextendedmax(I_eq, 30);
figure;
imshow(mask_em);
title('pix maior intensidade');
pause;

%limpar e mostrar o resultado
mask_em = imclose(mask_em, ones(5,5));
mask_em = imfill(mask_em, 'holes');
mask_em = bwareaopen(mask_em, 40);
overlay2 = imoverlay(I_eq, bw4_perim | mask_em, [.3 1 .3]);
figure;
imshow(overlay2);
title('limpar maiores intensidades');
pause;

%fazer o compelemento (watershed precisa que os pontos sejam minimos nao
%maximos)
I_eq_c = imcomplement(I_eq);


%forçar com que os pontos encontrados sejam os minimos locais
I_mod = imimposemin(I_eq_c, ~bw4 | mask_em);
figure;
imshow(I_mod);
title('complemento, localizar minimos');
pause;

%fazer a transformada watershed (notar que segmento elementos que na
%segmentação por perimetro estão unidos
L = watershed(I_mod);
figure;
title('resultado watershed');
imshow(label2rgb(L))
