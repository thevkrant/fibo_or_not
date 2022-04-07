def isfibo(n):
    fib_a = 0
    fib_b = 1
    while fib_a < n:
        fib_a, fib_b = fib_b, fib_a + fib_b
    if (fib_a == n):
        return("IsFibo")
    else:
        return("IsNotFibo")
