    i, j, k = map(int, input().split())
    def compute(num, left, right):
        if right < j or left > k:
            return 0
        
        if num < 2:
            if left >= j and right <= k:
                return num
            return 0
            
        mid = (left + right) >> 1
        return compute(num//2, left, mid-1) + compute(num % 2, mid, mid) + compute(num//2, mid + 1, right);
     
           
        
     
    comp = 1
    while comp < i:
        comp = (comp * 2) + 1
    print(compute(i, 1, comp))
