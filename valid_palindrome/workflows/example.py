import typing
from flytekit import conditional, task, workflow

@task()
def isalpha(s: str) -> bool:
    if ord(s) >= ord('a') and ord(s) <= ord('z'):
        return True
    return False

@task()
def isnumeric(s: str) -> bool:
    if ord(s) >= ord('0') and ord(s) <= ord('9'):
        return True
    return False

@task
def isPalindrome(s: str = "abba") -> bool:
    result = True
    i = 0
    j = len(s) - 1
    while (i <= j):
        if s[i] != s[j]:
            result = False
            break
        i+=1
        j-=1
    return result

@task()
def filter(s: str) -> str:
    filter_s = ""
    for c in s.lower():  
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            filter_s += c
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            filter_s += c
    return filter_s

@workflow()
def isPalindrome_wf(s: str = "Hello , i am yuteng") -> bool:
    filter_s = filter(s)
    result = isPalindrome(filter_s)
    return result

if __name__ == "__main__":
    print(f"Running wf() {isPalindrome_wf(s='HellolleH')}")
