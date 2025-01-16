"""A basic Flyte project template that uses ImageSpec"""

import typing
from flytekit import task, workflow

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

@task()
def mergeTwoLists(list1: typing.Optional[ListNode], list2: typing.Optional[ListNode]) -> typing.Optional[ListNode]:
    result = ListNode()
    cur = result
    while list1 and list2:
      if list1.val > list2.val:
        cur.next = list2
        list2 = list2.next
      else:
        cur.next = list1
        list1 = list1.next
      cur = cur.next
    if list1:
      cur.next = list1
    if list2:
      cur.next = list2
    tmp = result.next
    result.next = None
    result = tmp
    return result

@task()
def createListNode(nums: typing.List[int]) -> typing.Optional[ListNode]:
    result = ListNode()
    cur = result
    for num in nums:
      cur.next = ListNode(val=num)
      cur = cur.next
    tmp = result.next
    result.next = None
    result = tmp
    return result

@task()
def PrintListNode(result: typing.Optional[ListNode]):
  print(f"{result.val}")
  tmp = result
  while tmp:
    print(f"{tmp.val}")
    tmp = tmp.next

@workflow
def wf(nums1: typing.List[int], nums2: typing.List[int]) -> typing.Optional[ListNode]:
  listnode1 = createListNode(nums1)
  listnode2 = createListNode(nums2)
  node = mergeTwoLists(listnode1, listnode2)
  PrintListNode(node)
  return node


if __name__ == "__main__":
  result = wf(nums1=[1,2,3,4], nums2=[3,4,5,7])
