# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# could cache
def issame(t, r):
    if t is None and r is None:
        return True
    elif (t and not r) or (r and not t):
        return False
    return t.val == r.val and issame(t.left, r.left) and issame(t.right, r.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return False
        elif root is None and subRoot:
            return False
        elif root and subRoot is None:
            return True
        # match val, candidate
        if root.val == subRoot.val:
            if issame(root, subRoot):return True# or issame(root.left,subRoot) or issame(root.right,subRoot)
            # return (
            # (issame(root, subRoot) or issame(root.right,subRoot))
            # or self.isSubtree(root.left, subRoot.left)
            # and self.isSubtree(root.right, subRoot.right)
            # )
        # else:  # descend
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
