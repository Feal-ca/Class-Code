nums = input().split(" ")
sum = 0.0
for n in nums:
    n = float(n)
    sum = sum + n
print("{:.2f}".format((sum/len(nums))))