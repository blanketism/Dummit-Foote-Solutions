start = 2
end = 1000
step = 2
filepath = "sylow-even.txt"

def primeFactorization(n):
    primeFactors = []
    if n % 2 == 0:
        c = 0
        while n % 2 == 0:
            n //= 2
            c += 1
        primeFactors.append([2, c])
    p = 3
    while p * p <= n:
        if n % p == 0:
            c = 0
            while n % p == 0:
                n //= p
                c += 1
            primeFactors.append([p, c])
        p += 2
    if n > 1:
        primeFactors.append([n, 1])
    return primeFactors

def npval(primeFactors, p):
    cp = 1
    for pf in primeFactors:
        if pf[0] != p:
            cp *= pf[0] ** pf[1]
    count = 0
    nptest = 1
    while nptest <= cp:
        if cp % nptest == 0:
            count += 1
            if count > 1:
                return False
        nptest += p
    return True

count = 0
output = ""
n = start
while n <= end:
    primeFactors = primeFactorization(n)
    if len(primeFactors) > 1:
        if not all(npval(primeFactors, pf[0]) for pf in primeFactors):
            count += 1
            primefac = " * ".join(f"{pf[0]}^{pf[1]}" for pf in primeFactors)
            output += f"{n} = {primefac}\n"
            for pf in primeFactors:
                # recompute full list only for output purposes
                cp = 1
                for other in primeFactors:
                    if other[0] != pf[0]:
                        cp *= other[0] ** other[1]
                vals = [t for t in range(1, cp + 1, pf[0]) if cp % t == 0]
                output += f"{pf[0]}: {vals}\n"
            output += "===============\n"
    n += step

with open(filepath, "w") as f:
    f.write(f"Count: {count}\n")
    f.write(output)