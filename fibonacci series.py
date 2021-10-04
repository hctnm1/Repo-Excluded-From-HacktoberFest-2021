n = int(input("enter the values of n :"))
fib1 = 0
fib2 = 1
print(fib1,fib2)
i=1
while i<=n-2:
    fib = fib1+fib2
    print(fib)
    i = i + 1
    fib1 = fib2
    fib2 = fib

