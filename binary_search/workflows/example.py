import typing
from flytekit import task, workflow

@task()
def binary_search(nums: typing.List[int], target: int) -> int:
    i = 0
    j = len(nums)
    result = 0
    while i < j:
      index = int((i + j) / 2)
      val = nums[index]
      if val == target:
        result = index
        break
      if val > target:
        j = index - 1
      else:
        i = index + 1
    return result

@workflow
def wf(nums: typing.List[int], target: int) -> int:
  result = binary_search(nums, target)
  return result

if __name__ == "__main__":
    print(f"Running wf() {wf(nums='[1,2,3,4]', target='3')}")
