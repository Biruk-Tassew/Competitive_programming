class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def compDist(pt):
            return pt[0] ** 2 + pt[1] ** 2
        def mainLogic(lst, K):
            if len(lst) == K:
                return [i[0] for i in lst]
            maxL = lst[0][1]
            minL = lst[0][1]
            for i in lst:
                if maxL < i[1]:
                    maxL = i[1]
                if minL > i[1]:
                    minL = i[1]

            if maxL == minL:
                outPut = [lst[1][0]] * K
                return outPut
            rand_tup = random.choice(lst)
            pivot = rand_tup[1]
            
            i = 0
            lowest = []
            highest = []
            middle = []
            
            for i in lst:
                if i[1] < pivot:
                    lowest.append(i)
                elif i[1] > pivot:
                    highest.append(i)
                else:
                    middle.append(i)
                    
            len_lowest = len(lowest)
            if len_lowest == K:
                return [i[0] for i in lowest]
            elif len_lowest + len(middle) == K:
                return [i[0] for i in lowest] + [i[0] for i in middle]
            elif K > len(lowest) and (K < len(lowest) + len(middle)):
                return [i[0] for i in lowest] + mainLogic(middle,K-len(lowest)
                                                          -len(highest))
            elif K < len_lowest:
                return mainLogic(lowest, K)
            else:
                return [i[0] for i in lowest] + [i[0] for i in middle] +mainLogic(highest, K - len_lowest - len(middle)) 

        lst = [(i, compDist(i)) for i in points]
        return mainLogic(lst, k)


