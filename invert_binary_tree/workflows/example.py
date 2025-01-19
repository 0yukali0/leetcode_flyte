import typing
from collections import deque
from flytekit import task, workflow

class TreeNode:
    def __init__(self,
                 val:int = 0,
                 left:typing.Optional['TreeNode']=None,
                 right:typing.Optional['TreeNode']=None
                 ):
        self.val: int = val
        self.left: typing.Optional['TreeNode'] = left
        self.right: typing.Optional['TreeNode'] = right
    def invertTree(self, root:typing.Optional['TreeNode']=None) -> typing.Optional['TreeNode']:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp = self.left
        self.left = self.right
        self.right = tmp
        return root

@task()
def create_tree(nums: typing.List[typing.Optional[int]]) -> typing.Optional['TreeNode']:
    if not nums:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in nums]
    for i in range(len(nums)):
        if nodes[i] is not None:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nums) and nodes[left_index] is not None:
                nodes[i].left = nodes[left_index]
            if right_index < len(nums) and nodes[right_index] is not None:
                nodes[i].right = nodes[right_index]
    return nodes[0]

@task
def tree_to_list(root: typing.Optional['TreeNode']) -> typing.List[typing.Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


@task()
def invertTree(root:typing.Optional['TreeNode']=None) -> typing.Optional['TreeNode']:
    if not root:
        return None
    invertTree(root.left)
    invertTree(root.right)
    tmp = root.left
    root.left = root.right
    root.right = tmp
    return root

@workflow
def wf(nums: typing.List[typing.Optional[int]] = [2,3,5,None,7,1,9]) -> typing.List[typing.Optional[int]]:
    binary_tree = create_tree(nums)
    invert_binary_tree = invertTree(binary_tree)
    invert_nums = tree_to_list(invert_binary_tree)
    return invert_nums

if __name__ == "__main__":
    print(f"Running wf() {wf(nums=[1,2,3,None,4,5,6])}")
