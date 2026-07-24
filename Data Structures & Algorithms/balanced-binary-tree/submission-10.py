# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#


def tolist(tree):
    if not tree:
        return [None]
    # elif not tree.left and not tree.right:return [tree.val]
    return tolist(tree.left) + [tree.val] + tolist(tree.right)


def height(node) -> int:
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        Unbalanced = None
        def height(t)->int|Unbalanced:#none is failure case
            if not t:return 0
            hl,hr=height(t.left),height(t.right)
            # the bal cond, already using itself
            if hl == Unbalanced or hr == Unbalanced or abs(hl-hr)>1:return Unbalanced
            return 1+(max(hl,hr))
        return height(root) != Unbalanced
        # print(height(root), tolist(root))
        # isbal = True

        # descend into subtrees and check their heights and balance
        # curr = root
        # while curr:
        #     l, r = curr.left, curr.right
        #     hl, hr = height(l), height(r)

        # if root is None:
        #     return True  # empty or single
        # elif (root.left is None and root.right and (root.right.right or root.right.left)) or (
        #     root.right is None and root.left and (root.left.left or root.left.right)
        # ):
        #     return False
        # # elif root.left is not None and root.right
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        # # lh,rh = height(root.left),height(root.right)
        # # return abs(lh-rh)<=1


# track depth explicitly?
