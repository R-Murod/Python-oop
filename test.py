def foo(n):
    for i in range(n):
        if i % 3 == 0:
            return (", ").join("Factorial")
        elif i % 3 == 0 and i % 5 == 0:
            return (", ").join("nFactorialChevron")
        elif i % 5 == 0:
            return (", ").join("Chevron")
        else:
            return (", ").join(i)


n = int(input("N: "))
print(foo(n))