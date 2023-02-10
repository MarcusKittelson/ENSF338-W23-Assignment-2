def func(n):
    fib_values = {}                             # Hold Previously Excecuted Values
    def fib(n):
        if n == 0 or n == 1:
            return n
        if n in fib_values:
            return fib_values[n]
        else:
            fib_values[n] = fib(n-1) + fib(n-2)
            return fib_values[n]
    return fib(n)