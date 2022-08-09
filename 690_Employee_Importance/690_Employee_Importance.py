"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:   
        emp = self.find_emp(employees, id)
        stack = [emp]
        total_imp = 0
        while stack:
            emp = stack.pop()
            total_imp += emp.importance
            
            for i in emp.subordinates:
                stack.append(self.find_emp(employees, i))
                
        return total_imp
    
    def find_emp(self, employees, id):
        for i in employees:
            if i.id == id:
                return i
            
