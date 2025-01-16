import typing
from flytekit import task, workflow

@task()
def maxProfit(prices: typing.List[int]) -> int:
    min_price: int = prices[0]
    max_profit: int = 0
    for price in prices:
        if min_price > price:
          min_price = price
        profit = price - min_price
        if profit > max_profit:
          max_profit = profit
    return max_profit



@workflow
def wf(prices: typing.List[int]) -> int:
    profit = maxProfit(prices)
    return profit


if __name__ == "__main__":
    # Execute the workflow by invoking it like a function and passing in
    # the necessary parameters
    print(f"Running wf() {wf(prices=[2,3,4,1,24,6,7])}")
