
n, k = 6, 0
numbers = "0 0 0 0 1 1".split(" ")
print(numbers)
for i in range(n):
    el = int(numbers[i])

    if el == 0:
        k += 1
if k < n/2:
    print(k)
else:
    print(n-k)
