fib = [0,1]
y = 0
x = 1

for i in range(60):
  t=x+y
  fib.append(t)
  y=x
  x=t

T= int(input())
for i in range(T):
    N=int(input())
    print('Fib(%d) = %d' %(N, fib[N]))
