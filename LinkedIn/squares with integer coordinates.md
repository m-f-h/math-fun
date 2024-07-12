# squares with integer coordinates

Ref: https://www.linkedin.com/feed/update/urn:li:activity:7217182867599093761?
```
                  (x+2, y-1)
   (x,y)
                    (x+1+2, y+2-1)
    (x+1, y+2)
```
Solution : this is https://oeis.org/A002415 :
#### 4-dimensional pyramidal numbers: a(n) = n^2*(n^2-1)/12.
0, 0, 1, 6, 20, 50, 105, 196, 336, 540, 825, 1210, 1716, 2366, 3185, 4200, 5440, 6936, 8721, 
10830, 13300, 16170, 19481, 23276, 27600, 32500, 38025, 44226, 51156, 58870, 67425, 76880, 87296, 98736, 
111265, 124950, 139860, 156066, 173641, 192660, 213200, 235340, ...

In PARI/GP:
```PARI/GP
cnt(N,show=0)={ my(m,M);
   sum(x=0, N-1, sum(y=0, N-1, /* (x,y) = upper left corner of the square,
         the other 4 points will be :   (x+dx, y+dy) = lower left
                                        (x+dy, y-dx) = upper right
                                        (x+dx+dy, y+dy-dx) = lower right */
      sum(dx =  /* delta x for lower-left corner: 
                   constraints are  0 <= x+dx <= N,  0 <= y-dx <= N
                   <=>  -x <= dx <= N-x  and  y-N <= dx <= y  */
               max(y-N, -x),  /* can't be less than -x_ul (left border), nor N-y because "dx" is added to y and dy*/
               min(y, N-x), /* can't be more than N-x_ul (right border) nor y because dx is subtracted from y for upper-right */
      /* how many dy's are possible ? we have the constraints:
         0 <= y+dy <= N     <=>     -y <= dy <= N-y
         0 <= x+dy <= N     <=>     -x <= dy <= N-x
         0 <= x+dx+dy <= N  <=>  -x-dx <= dy <= N-x-dx
         0 <= y-dx+dy <= N  <=>  -y+dx <= dy <= N+dx-y
         Finally, to avoid double counting, we will restrict dy >= -dx ("left side" at least 45° w.r.t. horizontal,
            and less than 135°:) dy > dx
         */
         my(m = -vecmin([y,x,x+dx,y-dx,if(dx<0,dx,-dx-1)]), M = N-vecmax([y,x,x+dx,y-dx]));
         show && printf("x=%d, y=%d, dx=%d, dy=%d .. %d => %d, \n", x,y,dx,m,M, 1+M-m);
                      max(1+M-m, 0))/*sum dx*/
   ))}
```
