class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        toTwenty = ["One", "Two", "Three", "Four", "Five", 
                               "Six", "Seven", "Eight", "Nine","Ten",
                               "Eleven", "Twelve", "Thirteen", "Fourteen",
                               "Fifteen", "Sixteen", "Seventeen", "Eighteen", 
                               "Nineteen"]
        twentyToHundred = ["Twenty", "Thirty", "Forty", "Fifty", 
                                "Sixty", "Seventy", "Eighty", "Ninety"]
        bigNums = ["Hundred", "Thousand", "Million", "Billion"]
        bigDigits = [100, 1000, 1000000, 1000000000]
        
        def convert(num):
            if int(num)==0:
                return ''
            elif num < 20:
                return ' ' + toTwenty[int(num-1)]
            elif num<100:
                
                return ' ' + twentyToHundred[int(num/10 - 2)] + convert(num % 10)
            
            for i in range(3, -1, -1):
                if num >= bigDigits[i]:
                    return convert(num/bigDigits[i]) + " " + bigNums[i] + convert(num % bigDigits[i])
            return ''                
       
        return convert(num)[1:]
            