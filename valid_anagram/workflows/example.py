import typing
from flytekit import task, workflow

@task()
def isAnagram(s: str, t: str) -> bool:
    count: typing.Dict[str, int] = {}
    for letter in range (ord('a'), ord('z')+1):
      count[chr(letter)] = 0
    for letter in s:
      count[letter] += 1
    for letter in t:
      count[letter] -= 1
    for num in count.values():
      if num < 0 or num > 0:
        return False
    return True



@workflow
def wf(s: str = "world", t: str = "wlord") -> bool:
  result = isAnagram(s, t)
  return result


if __name__ == "__main__":
    result = wf(s="a")
    print(f"Running wf() {result}")
