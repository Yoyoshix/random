def convert(n, from_base=2, to_base=10, char_list="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"):
    new = 0
    if from_base != 10:
        for idx, i in enumerate(str(n)[::-1]):
            new += char_list.index(i) * (from_base ** idx)
    n = int(new)
    res = ""
    while n > 0:
        res += char_list[n % to_base]
        n = n // to_base
    return res[::-1]
