img = imread('test80.jpg');
imshow(img)

%dec_int 
  reduzir = img;
  reduzirX = floor(lenght(reduzir(1,:,1))*2);
  reduzirY = floor(lenght(reduzir(:,1,1))*2);
  for i = lenght(reduzir(1,1:))
    for j = 1:reduzirX
      for k = 1:reduzirY
        Quest_1(k, j, i)=reduzir(round(k/2), round(j/2),i);
        
      endfor
    endfor
  endfor
  figure; 
  imshow(Quest_1)



\%egde_improv
  melhoramento = img;
  [A, L] = size(img);

  for i = 2:A-1
      for j = 2:L-1
          Bloco = I(i-1:i+1, j-1:j+1);
          V = sort(Bloco(:));
          Quest1_1(i,j) = V(5);
      end
  end
  figure; 
  imshow(Quest1_1)

