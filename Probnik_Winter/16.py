def f(n):
    return 2 * n * f(n - 1)


print(((f(2024) // 16) - f(2023)) // f(2022))


