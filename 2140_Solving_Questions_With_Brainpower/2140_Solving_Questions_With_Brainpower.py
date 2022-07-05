class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        len_questions = len(questions)
        solve = [0]*(len(questions)+1)
       
        for i in range(len_questions-1, -1, -1):
            points, brainpower = questions[i]
            if i + brainpower + 1 < len_questions:
                temp_sol_one = points + solve[i + brainpower + 1]
            else:
                temp_sol_one = points
            temp_sol_two = solve[i + 1]
            
            solve[i] = max(temp_sol_one, temp_sol_two)
            print(solve)
        
        return solve[0]
        
                
