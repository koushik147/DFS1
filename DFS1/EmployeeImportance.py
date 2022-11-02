#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution:
    total_importance = 0 # declaring total importance to 0
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        d_dict = dict() # declaring dictionary
        for i in employees: # for iterating in employees
            d_dict[i.id] = i # storing employee in dictionary of id
            
        def dfs(d):
            self.total_importance += d.importance # storing the importance in total importance
            for i in d.subordinates:
                dfs(d_dict[i]) # calling recursive function with dictionary of i
                
        dfs(d_dict[id]) # calling dfs fucntion recursively with dictionary of id
        return self.total_importance # returning total importance
