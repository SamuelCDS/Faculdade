%rodar cada exemplo na linha de comandos


%detetor de transições
edgedetect('im1.jpg');

%detetor de transcições (ver a importancia do limiar, e diferentes
%direções)
sobeledge('im1.jpg');

%transformada de hough
houghtr('im1.jpg');
houghtr('pentagon.tif');

%segmentação por limiares
thresh('im2.jpg');