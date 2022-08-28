t = int(input())

while t:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    left = 1
    right = len(a)-1
    blue = 0
    red = 0
    blue += a[left-1] + a[left]
    red += a[right]
    res = "NO"
    while left < right:
        if blue < red:
            res = "YES"
            break
        else:
            right -= 1
            left += 1
            blue += a[left]
            red += a[right]
    print(res)
    t -= 1
