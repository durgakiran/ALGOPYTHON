# compute gcd(14,63)

# naive gcd


def naiveGcd(a, b):
    fa = []
    fb = []
    for i in range(1, a+1):
        if(a % i == 0):
            fa.append(i)

    for j in range(1, b + 1):
        if(b % j == 0):
            fb.append(j)

    cf = []
    for f in fa:
        if f in fb:
            cf.append(f)
    print(cf)
    return cf[-1]


gcd = naiveGcd(14, 63)

print(gcd)