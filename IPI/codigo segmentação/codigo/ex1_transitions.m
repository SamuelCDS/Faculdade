%rodar cada exemplo na linha de comandos


%detetor de transi��es
edgedetect('im1.jpg');

%detetor de transci��es (ver a importancia do limiar, e diferentes
%dire��es)
sobeledge('im1.jpg');

%transformada de hough
houghtr('im1.jpg');
houghtr('pentagon.tif');

%segmenta��o por limiares
thresh('im2.jpg');