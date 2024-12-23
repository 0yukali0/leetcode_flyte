import typing
from flytekit import task, workflow

@task()
def two_sum(nums: list[int], target: int) -> list[int]:
  num: dict[int, int] = {}
  for idx, value in enumerate(nums):
    num[value] = idx
  data = []
  for idx, value in enumerate(nums):
    want = target - value
    if want in num.keys():
      want_idx = num[want]
      if want_idx == idx:
        continue
      else:
        data.append(idx)
        data.append(want_idx)
        break
  return data

@workflow
def wf(nums: list[int] = [1, 2, 3], target: int = 4) -> list[int]:
    result = two_sum(nums=nums, target=target)
    return result


if __name__ == "__main__":
    print(f"Running wf() {wf(nums=[2,7,11,15], target=9)}")
    print(f"Running wf() {wf(nums=[3,2,4], target=6)}")
    print(f"Running wf() {wf(nums=[3,3], target=6)}")
