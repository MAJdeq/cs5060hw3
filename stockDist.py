import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


def readFile(filename):
    # Read the single column data
    df = pd.read_csv(filename, header=None, names=['Daily Returns'])

    # Convert the index to a date range
    # Assuming the data is daily and starts from today
    df.index = pd.date_range(end=pd.Timestamp.today(), periods=len(df), freq='D')

    return df


def plotNormalReturns(df, filename):

    mean, std = stats.norm.fit(df)


    # Perform Kolmogorov-Smirnov test
    ks_statistic, p_value = stats.kstest(df, 'norm', args=(mean, std))

    # Plot histogram of the data
    plt.figure(figsize=(10, 6))
    plt.hist(df, bins=30, density=True, alpha=0.6, color='g', label='Empirical Data')

    # Generate x values for the fitted distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)

    # Plot the PDF of the fitted normal distribution
    pdf = stats.norm.pdf(x, mean, std)
    plt.plot(x, pdf, 'r-', linewidth=2, label=f'Fitted Normal (mean={mean:.2f}, std={std:.2f})')

    plt.title(f'Histogram and Fitted Distribution of {filename.capitalize()}')
    plt.xlabel('Daily Returns')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'assets/{filename}Normal.png')
    plt.show()
    plt.close()

def plotLogNormReturns(df, filename):

    shape, loc, scale = stats.lognorm.fit(df['Daily Returns'])


    # Perform Kolmogorov-Smirnov test
    ks_statistic, p_value = stats.kstest(df, 'lognorm', args=(shape, loc, scale))

    print(f"KS Statistic: {ks_statistic}, p-value: {p_value}")

    # Plot histogram of the data
    plt.figure(figsize=(10, 6))
    plt.hist(df, bins=30, density=True, alpha=0.6, color='g', label='Empirical Data')

    # Generate x values for the fitted distribution
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)

    # Plot the PDF of the fitted normal distribution
    pdf = stats.lognorm.pdf(x, shape, loc, scale)
    plt.plot(x, pdf, 'r-', linewidth=2, label=f'Fitted LogNorm (shape={shape:.2f}, loc={loc:.2f}, scale={scale:.2f})')
    plt.title(f'Histogram and Fitted Distribution of {filename.capitalize()}')
    plt.xlabel('Daily Returns')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'assets/{filename}LogNormal.png')
    plt.show()
    plt.close()



# Main execution
if __name__ == "__main__":
    try:
        stock1_data = readFile('stock1.csv')
        stock2_data = readFile('stock2-1.csv')
        plotNormalReturns(stock1_data, 'stock1')
        plotNormalReturns(stock2_data, 'stock2')
        plotLogNormReturns(stock1_data, 'stock1')
        plotLogNormReturns(stock2_data, 'stock2')
    except Exception as e:
        print(f"An error occurred: {e}")