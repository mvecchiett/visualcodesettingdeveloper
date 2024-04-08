def fib(n): # escribe la serie de Fibonacci hasta n
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    



#fib(n) = fib(n-1) + fib(n-2)

print(fib(0))
print(fib(1))
