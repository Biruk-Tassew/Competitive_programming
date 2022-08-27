t = int(input())

while t:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split())) 
    a_b = []
    for i in range(n):
        a_b.append((a[i], b[i]))
    a_b.sort(reverse=True)
   
    size = k
    while a_b and a_b[-1][0] <= size:
        size += a_b.pop()[1]
        
    print(size)
    t -= 1
