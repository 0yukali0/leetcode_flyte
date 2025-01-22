import typing
from flytekit import task, workflow

class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: typing.Optional['ListNode'] = None

@task()
def createNodeList(nums: typing.List[int], cycle: bool) -> typing.Optional['ListNode']:
    if len(nums) == 0:
        return None
    head = ListNode(-1)
    tmp = head
    for num in nums:
        instance = ListNode(num)
        tmp.next = instance
        tmp = tmp.next
    if cycle:
        tmp.next = head
    else:
      tmp = head
      head = head.next
      tmp.next = None
    return head


@task()
def has_cycle(head: typing.Optional['ListNode']) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


@workflow
def wf(nums: typing.List[int] = [1,2,3]):
    head = createNodeList(nums, True)
    result = has_cycle(head)
    print(result)
    head = createNodeList(nums, False)
    result = has_cycle(head)
    print(result)


if __name__ == "__main__":
    print(f"Running wf() {wf(nums='[1,2,3]')}")
