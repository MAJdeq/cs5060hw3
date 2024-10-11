import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
from scipy import stats
import numpy as np

# PART ONE
def readFile(filename):
    # Read the single column data
    df = pd.read_csv(filename, header=None, names=['Daily Returns'])
    l = list(df['Daily Returns'])
    return [0 if i == 0 else l[i] - l[i-1] for i in range(len(l))], l[-1]


def betaFit(df):
    # Unpack four parameters from beta distribution fit
    return stats.beta.fit(df)


# PART TWO
def payoff(strike, stock_price):
    return max(stock_price - strike, 0)


def simulate_paths(initial_price, drift, a, b, loc, scale, paths):
    T = 1
    dt = 1/365
    timesteps = int(T / dt)
    price_paths = np.zeros((paths, timesteps))
    for i in range(paths):
        current_price = initial_price
        for t in range(timesteps):
            dWt = (np.random.beta(a, b) * scale) + loc # random motion
            dYt = (drift * dt) + dWt # Change in price
            current_price += dYt # Update the current price
            price_paths[i, t] = current_price # Store price in path
    return price_paths


def monte_carlo_option_pricing(price_paths, strike, risk_free_rate):
    call_payoffs = np.zeros(price_paths.shape[0])
    final_prices = np.zeros(price_paths.shape[0])
    for i in range(price_paths.shape[0]):
        final_price = price_paths[i, -1] # Last price in the path
        final_prices[i] = final_price
        call_payoffs[i] = payoff(strike, final_price) / (1 + risk_free_rate)
    return final_prices, call_payoffs

def scenario1_pricing(paths1, paths2):
    finals1, payoffs1  = monte_carlo_option_pricing(paths1, paths1[0, 0], 0.01)
    finals2, payoffs2 = monte_carlo_option_pricing(paths2, paths2[0, 0], 0.01)

    pricing1 = payoffs1.mean()
    pricing2 = payoffs2.mean()

    return (pricing1 + pricing2) / 2


def scenario2_pricing(paths1, paths2):
    finals1, payoffs1  = monte_carlo_option_pricing(paths1, paths1[0, 0], 0.01)
    finals2, payoffs2 = monte_carlo_option_pricing(paths2, paths2[0, 0], 0.01)

    pricing1 = payoffs1.mean()
    pricing2 = payoffs2.mean()

    return max(pricing1, pricing2)


if __name__ == "__main__":
    stock1, close1 = readFile('stock1.csv')
    stock2, close2 = readFile('stock2.csv')

    a1, b1, loc1, scale1 = betaFit(stock1)
    a2, b2, loc2, scale2 = betaFit(stock2)

    # assume drift is 3%
    paths1 = simulate_paths(close1, 0.03, a1, b1, loc1, scale1, 5000)
    paths2 = simulate_paths(close2, 0.03, a2, b2, loc2, scale2, 5000)

    print(f"Scenario 1 price: ${scenario1_pricing(paths1, paths2):.2f}")
    print(f"Scenario 2 price: ${scenario2_pricing(paths1, paths2):.2f}")