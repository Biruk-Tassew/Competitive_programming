class Solution(object):
   def fizzBuzz(self, n):
    outputs = []
    for i in range(1, n+1):
        if(i % 3 == 0 and i % 5 == 0):
            print
            outputs.append("FizzBuzz")
        elif(i % 3 == 0):
            outputs.append("Fizz")
        elif(i % 5 == 0):
            outputs.append("Buzz")
        else:
            outputs.append(str(i))
    return outputs
