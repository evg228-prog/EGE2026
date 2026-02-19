def f(start, end, digits):
    if start == end and len(digits) - 1 > 50: return 1
    if start > end: return 0
    return f(start + 2, end, digits | {start + 2}) + \
        f(start * 3, end, digits | {start * 3}) + \
        f(start * 4, end, digits | {start * 4})

print(f(2, 400, set()))

# 6142