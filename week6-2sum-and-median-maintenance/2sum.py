container = set()

with open('algo1-programming_prob-2sum.txt') as inf:
    for line in inf:
        container.add(int(line))

count = 0

container = sorted(container)
for k, i in enumerate(container):
    if i > 0:
        break


t0 = -10000
t1 = 10000
k0 = k - 1
k1 = k


res = set()
L = len(container)
while True:
    s = container[k0] + container[k1]
    if s < t0:
        k1 = min(k1 + 1, L - 1)
    elif s > t1:
        k0 = max(k0 - 1, 0)
    else:
        res.add(s)
        # updating k0 or k1 will results in equivalent results
        k0 = max(k0 - 1, 0)
        # k1 = min(k1 + 1, L - 1)
        
    # print(k0, k1, len(res), s)
    if k0 == 0 or k1 == L - 1:
        break

print('final: ', len(res))
