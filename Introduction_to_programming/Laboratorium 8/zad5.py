def newtons_binomial(n, k):
    if k == 0 or k == n:
        return 1
    elif k == 1:
        return n
    else:
        return newtons_binomial(n - 1, k - 1) + newtons_binomial(n - 1, k)


print(newtons_binomial(5, 1))
