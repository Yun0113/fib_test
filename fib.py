def fib(n):
    fib = []
    for i in range(0, n):
        if len(fib) < 2:
            fib.append(1)
            continue
        fib.append(fib[-1]+fib[-2])
    return fib