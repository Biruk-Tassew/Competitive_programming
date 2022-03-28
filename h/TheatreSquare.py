    m, n, a = map(int, input().split())
     
    left = 0
    right = 0
    if n % a == 0:
        left = n // a
    else:
        left = n // a+1
    if m % a == 0:
        right = m // a
    else:
        right = m // a+1
             
             
    print(right*left)
