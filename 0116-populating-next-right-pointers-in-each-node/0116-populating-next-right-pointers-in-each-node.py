"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def find_next(self, root, next_node):
        if root == None:
            return
        root.next = next_node
        self.find_next(root.left, root.right)
        nxt = None
        if root.next != None:
            nxt = root.next.left
        self.find_next(root.right, nxt)
        
    
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.find_next(root, None)
        return root
        
    
            
            
        