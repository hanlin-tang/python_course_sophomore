def fib(n):
    a,b=1,1
    while a < n:
        a,b=b,a+b
        print(a)
    return fib(n)

        
