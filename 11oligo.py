def oligomt(a,c,g,t):
    nt = a + c + g + t
    if nt <= 13:
        return (a + t) * 2 + (g + c) * 4
    elif nt > 13:
        return 64.9 + 41 * (g + c - 16.4) / (a + c + g + t)
    return None
print(oligomt(5, 7, 3, 4))