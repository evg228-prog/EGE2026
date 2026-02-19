def f(start, end, cnt):
    if start == end and cnt <= 15: return 1
    if start > end or cnt > 15: return 0
    return f(start + 2, end, cnt + (1 if (start + 2) % 2 == 0 else 0)) + \
        f(start + 3, end, cnt + (1 if (start + 3) % 2 == 0 else 0)) + \
        f(start * 2 + 1, end, cnt + (1 if (start * 2 + 1) % 2 == 0 else 0))

print(f(1, 55, 0))

# 4197234