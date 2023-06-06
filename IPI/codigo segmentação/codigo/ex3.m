
%ler imagem inicial
M0 = double(imread('lena.tif'));
imshow(M0,[]);

%adicionar ruido gaussiano
sigma = 10; % noise level
R = sigma*randn(size(M0));
M = M0 + R;
pause;figure;imshow(M,[]);


%limiar duro vs limiar suave
%----------------------------
% valor do limiar
T = 1;
v = -linspace(-3,3,2000);
% limiar duro
v_hard = v.*(abs(v)>T);
% limiar suave
v_soft = max(1-T./abs(v), 0).*v;
pause;
clf;
hold('on');
plot(v, v_hard);
plot(v, v_soft, 'r--');
axis('equal'); axis('tight');
legend('Hard thresholding', 'Soft thresholding');
hold('off');
pause;

%hard
for N=1:3
  for i=20:20:60
    [XC,CXC,LXC,PERF0,PERFL2] = WDENCMP('gbl',M,'db1',N,i,'h',1);

    subplot(121); image(M); title('Imagem Original');
    axis square
    subplot(122); image(XC); title('Imagem Resultante');
    axis square
    pause;
  end
end

%soft
for N=1:3
  for i=20:20:60
    [XC,CXC,LXC,PERF0,PERFL2] = WDENCMP('gbl',M,'db1',N,i,'s',1);

    subplot(121); image(M); title('Imagem Original');
    axis square
    subplot(122); image(XC); title('Imagem Resultante');
    axis square
    pause;
  end
end


%utilizar o valor padrao limiar padrão
[THR,SORH,KEEPAPP] = DDENCMP('den','wv',M);
[XC,CXC,LXC,PERF0,PERFL2] = WDENCMP('gbl',M,'db1',2,THR,SORH,KEEPAPP);

subplot(121); image(M); title('Imagem Original');
axis square
subplot(122); image(XC); title('Imagem Resultante');
axis square


