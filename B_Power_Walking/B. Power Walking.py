from collections import defaultdict
t = int(input())

while t:
    n = int(input())
    store = defaultdict(lambda: 0)
    a = list(map(int, input().split()))
    
    for i in range(n):
        store[a[i]] += 1

    for i in range(1, n+1):
        print(max(i, len(store)), end=" ")
    print("\n")
        
    t -= 1
