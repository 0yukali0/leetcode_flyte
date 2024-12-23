import typing
from flytekit import task, workflow

@task()
def two_sum(nums: list[int], target: int) -> list[int]:
  data = []
  num: dict[int, int] = {}
  for idx, value in enumerate(nums):
    num[value] = idx

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
def wf(nums: list[int] = [1, 2, 3], target: int = 4) -> typing.Tuple[str, int]:
    result = two_sum(nums=nums, target=target)
    greeting_len = greeting_length(greeting=greeting)
    return greeting, greeting_len


if __name__ == "__main__":
    # Execute the workflow by invoking it like a function and passing in
    # the necessary parameters
    print(f"Running wf() {wf(nums=[1, 2, 3, 4], target=6)}")
