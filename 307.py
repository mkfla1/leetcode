###
线段树
###

class SegmentTree:
    class TreeNode:
        def __init__(self, start, end, val):
            self.start, self.end = start, end
            self.left, self.right = None, None
            self.val = val

    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, start, end):
        if start == end:
            return SegmentTree.TreeNode(start, end, nums[start])
        
        root = SegmentTree.TreeNode(start, end, 0)
        mid = (start + end) // 2
        root.left = self.build(nums, start, mid)
        root.right = self.build(nums, mid + 1, end)
        self.update_node_val(root)
        return root
    
    def update_node_val(self, root):
        root.val = 0
        if root.left:
            root.val += root.left.val
        if root.right:
            root.val += root.right.val
    
    def query(self, root, start, end):
        if root.start == start and root.end == end:
            return root.val
        
        mid = (root.start + root.end) // 2
        if mid < start:
            return self.query(root.right, start, end)
        elif mid >= end:
            return self.query(root.left, start, end)
        return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)
    
    def update(self, root, index, val):
        if not (root.start <= index <= root.end): return
        if root.start == index and root.end == index:
            root.val = val
            return
        
        mid = (root.start + root.end) // 2
        if mid < index:
            self.update(root.right, index, val)
        else:
            self.update(root.left, index, val)
        self.update_node_val(root)
        return

class NumArray:
    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(self.st.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(self.st.root, left, right)
