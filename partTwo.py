import matplotlib.pyplot as plt
import numpy as np
import math

def payoff(strike, stock_price):
    return max(stock_price - strike, 0)

def simulate_geometric_brownian_motion(initial_price, drift, volatility, dt, T, paths):
    timesteps = int(T / dt)
    price_paths = np.zeros((paths, timesteps))
    for i in range(paths):
        current_price = initial_price
        for t in range(timesteps):
            dWt = np.random.beta(9, 10) - 0.35 # random motion
            dYt = (drift * dt) + (volatility * dWt) # Change in price
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


if __name__ == "__main__":
    price_paths = simulate_geometric_brownian_motion(100, 0.03, 17.04, 1/365, 1, 5000)
    for i in range(10):
        plt.plot(price_paths[i])
    plt.show()

    pricing = monte_carlo_option_pricing(price_paths, 100, 0.01)
    print(pricing[0].mean(), pricing[1].mean())

    print(f"Average stock price after {int(1 / (1/365)) * 1} days: ${pricing[0].mean(): .2f}")
    print(f"\nAverage payoff (option block of 100): ${pricing[1].mean() *100:.2f}")
    print(f"Cost of option: ${pricing[1].mean():.2f}")
