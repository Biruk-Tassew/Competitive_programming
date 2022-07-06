class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        street_list = list(street)
        
        for i in range(len(street_list)):
            if street_list[i] == 'H':
                if i > 0 and street_list[i-1] =='B':
                    continue
                if i < len(street_list)-1 and street_list[i+1]  == '.':
                    street_list[i+1] = 'B'   
                elif i > 0 and street_list[i-1] == '.':
                    street_list[i-1] = 'B' 
                else:
                    return -1
                
        return street_list.count('B')
