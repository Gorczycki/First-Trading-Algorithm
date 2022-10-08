Seeking to use an API token to gain live market data to execute live market trades.

Algorithm will be restricted to only paper trading use to begin with.

Written in Python, list of libraries will be made soon. 

No official algorithmic strategy, just yet. Example strategies being Stat Arb, Mean Reversion, VWAP etc. https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp

Obstacles: 
Where to find the right api
Where to obtain live market data.
Interacting with JSON data uisng Python

Project outline / user stories
  Aim to simulate gains from trades using relevant trading strategies
    Strats
      VWAP (Volume-weighted average price)
      SMA (Volume-weighted average price)
        Taking an average over a set number of days
          user can simulate gaines/losses
            User enters the stock 
              User enters investment start date
                  Investment end date
              Calc if investment is positive of neg over the given period of days