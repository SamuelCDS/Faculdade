
%ler imagem inicial
M0 = double(imread('bab512.tif'));
imshow(M0,[]);pause;



%utilizar o valor padrao limiar padrão
[THR,SORH,KEEPAPP] = DDENCMP('cmp','wv',M0);


for N=1:2
   for THR=5:5:25
   [XC,CXC,LXC,PERF0,PERFL2] = WDENCMP('gbl',M0,'db1',N,THR,SORH,KEEPAPP);
   PERF0
   PERFL2
   subplot(121); image(M0); title('Imagem Original');
   axis square
   subplot(122); image(XC); title('Imagem Resultante');
   axis square
   pause;
   end
end

%utilizando o valor padrao
[THR,SORH,KEEPAPP] = DDENCMP('cmp','wv',M0);
[XC,CXC,LXC,PERF0,PERFL2] = WDENCMP('gbl',M0,'db1',2,THR,SORH,KEEPAPP);
PERF0
PERFL2

subplot(121); image(M0); title('Imagem Original');
axis square
subplot(122); image(XC); title('Imagem Resultante');
axis square


%compressão exagerada

[XC,CXC,LXC,PERF0,PERFL2] = WDENCMP('gbl',M0,'db1',4,80,SORH,KEEPAPP);
PERF0
PERFL2

subplot(121); image(M0); title('Imagem Original');
axis square
subplot(122); image(XC); title('Imagem Resultante');
axis square