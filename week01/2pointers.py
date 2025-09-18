# input
a = [-3, -2, 0, 1, 3, 5]
# result [0, 1, 2, 3, 3, 5]
ans = [0] * len(a)

p1 = 0
p2 = len(a) - 1
count = len(a) - 1
while True:
    if p1 == p2:
        ans[count] = a[p1]
        break
    else:
        if abs(a[p1]) > abs(a[p2]):
            ans[count] = abs(a[p1])
            p1 += 1
        else:
            ans[count] = abs(a[p2])
            p2 -= 1
        count -= 1
print(ans)
