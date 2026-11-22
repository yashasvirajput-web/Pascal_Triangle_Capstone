import time

def make_row_iterative(n):
    row = [1]
    for i in range(n):
        new_row = [1]
        for j in range(len(row) - 1):
            new_row.append(row[j] + row[j+1])
        new_row.append(1)
        row = new_row
    return row

def binom(n, k):
    if k == 0 or k == n:
        return 1
    return binom(n-1, k-1) + binom(n-1, k)

def make_row_recursive(n):
    row = []
    for k in range(n+1):
        row.append(binom(n, k))
    return row

N = 10

print("Pascal Triangle - Iterative Method")
print("-" * 40)

start = time.time()
triangle = []
for i in range(N):
    triangle.append(make_row_iterative(i))
end = time.time()
print("Iterative time:", round(end - start, 4), "seconds\n")

for row in triangle:
    line = ""
    for num in row:
        line += str(num) + " "
    print(line.center(50))

print("\n" + "="*50)
print("Pascal Triangle - Recursive Method")
print("-" * 40)

start = time.time()
triangle_rec = []
for i in range(N):
    triangle_rec.append(make_row_recursive(i))
end = time.time()
print("Recursive time:", round(end - start, 4), "seconds")
print("(Recursive is much slower, so keep N small)\n")

print("Binomial Expansion of (a + b)^" + str(N-1))
print("-" * 40)
row = make_row_iterative(N-1)
expansion = ""
for i in range(len(row)):
    coeff = row[i]
    a_power = N-1 - i
    b_power = i
    
    term = ""
    if coeff != 1:
        term += str(coeff)
    if a_power > 0:
        term += "a"
        if a_power > 1:
            term += "^" + str(a_power)
    if b_power > 0:
        term += "b"
        if b_power > 1:
            term += "^" + str(b_power)
    if term == "":
        term = "1"
    
    if i > 0:
        expansion += " + "
    expansion += term

print(expansion)

print("\n" + "="*50)
print("Row Sum Check (should be 2^n) and Odd Numbers Pattern")
print("-" * 50)

for i in range(N):
    row = triangle[i]
    total = 0
    for num in row:
        total += num
    
    print("Row", i, "sum =", total, "  (2^" + str(i) + " =", 2**i, ")")
    
    pattern = ""
    for num in row:
        if num % 2 == 1:
            pattern += "* "
        else:
            pattern += "  "
    print("Pattern:", pattern)