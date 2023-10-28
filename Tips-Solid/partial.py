import statistics
from dataclasses import dataclass
from functools import partial
from typing import Callable

TradingStrategyFunction = Callable[[list[int]], bool]


def should_buy_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] < statistics.mean(list_window)


def should_sell_avg(prices: list[int], window_size: int) -> bool:
    list_window = prices[-window_size:]
    return prices[-1] > statistics.mean(list_window)


def should_buy_minmax(prices: list[int], max_price: int) -> bool:
    # buy if it's below the max price
    return prices[-1] < max_price


def should_sell_minmax(prices: list[int], min_price: int) -> bool:
    # sell if it's above the min price
    return prices[-1] > min_price


@dataclass
class TradingBot:
    """Trading bot that connects to a crypto exchange and performs trades."""

    buy_strategy: TradingStrategyFunction
    sell_strategy: TradingStrategyFunction

    def run(self, symbol: str) -> None:
        prices = 200
        if self.buy_strategy(prices):
            print('bought')
        elif self.sell_strategy(prices):
            print('sold')
        else:
            print(f"No action needed for {symbol}.")


def main() -> None:

    # create the trading bot and run the bot once
    buy_strategy = partial(should_buy_minmax, max_price=32_000_00)
    sell_strategy = partial(should_sell_minmax, min_price=38_000_00)
    bot = TradingBot(buy_strategy, sell_strategy)
    bot.run("BTC/USD")


if __name__ == "__main__":
    main()