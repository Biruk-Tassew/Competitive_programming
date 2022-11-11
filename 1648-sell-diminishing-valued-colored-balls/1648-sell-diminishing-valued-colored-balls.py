class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True) 
        inventory += [0]
        ans = 0
        level = 1
        for i in range(len(inventory)-1): 
            if inventory[i] > inventory[i+1]: 
                if level*(inventory[i] - inventory[i+1]) < orders: 
                    ans += level*(inventory[i] + inventory[i+1] + 1)*(inventory[i] - inventory[i+1])//2 
                    orders -= level*(inventory[i] - inventory[i+1])
                else: 
                    q, r = orders//level, orders%level
                    ans += level*(2*inventory[i] - q + 1) * q//2 + r*(inventory[i] - q)
                    return ans % (10**9 + 7)
            level += 1