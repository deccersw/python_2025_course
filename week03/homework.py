nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
p1 = 0
p2 = len(nums) - 1
ans = 0
while p1 != p2:
    ans = max(ans, min(nums[p1], nums[p2]) * (p2 - p1))
    if nums[p1] <= nums[p2]:
        p1 += 1
    else:
        p2 -= 1
print(ans)
