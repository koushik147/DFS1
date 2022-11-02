#TimeComplexity: O(n)
#SpaceComplexity: O(n)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        return self.recur(root.left,root.right) # calling recur function recursively
        
    def recur(self,root_left,root_right):
        
        if not root_left and not root_right: # if not left and right 
            return True
        if not root_left or not root_right: # if not left or right 
            return False
        if root_left.val != root_right.val: # if left value is not equal to right value 
            return False
        
        return self.recur(root_left.left,root_right.right) and self.recur(root_left.right,root_right.left) # returning recursive function with root left and root right
