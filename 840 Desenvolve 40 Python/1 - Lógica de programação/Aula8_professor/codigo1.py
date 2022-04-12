# Fatorial
# 4! = 4 * 3 * 2 * 1 = 24
# 3! = 3 * 2 * 1 = 6
# 2! = 2 * 1 = 2
# 1! = 1
# 0! = 1

# n! = n * (n-1) * (n - 2) * ... * 2 * 1
# (n-1)! = (n-1) * (n - 2) * ... * 2 * 1

# n! = n * (n-1)!
# 5! = 5 * 4! = 5 * 24 = 120
# 4! = 4 * 3! = 4 * 6 = 24
# 3! = 3 * 2! = 3 * 2 = 6
# 2! = 2 * 1! = 2
# 1! = 1 * 0! = 1
# 0! = 1 # Caso base

# fatorial(n) = n * fatorial(n-1)
# fatorial(0) = 1

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
