# cs5060hw3

## Collaborators:
* Ethan Ford
* Nathan Freestone

*RUNNING INSTRUCTIONS*
* This code has the following dependencies:
  - pandas
  - matplotlib
  - scipy
  - numpy

each part has a dedicated python file. To execute them, run:

```bash
python partOne.py
```

substitute your python file as needed.

*PART ONE*

* Here are the plots for both stock datasets fitted on a normal distribution:
![StockOne](https://github.com/MAJdeq/cs5060hw3/blob/main/assets/stock1Normal.png)
![StockTwo](https://github.com/MAJdeq/cs5060hw3/blob/main/assets/stock2Normal.png)
* Here are the plots for both stock datasets fitted on a beta distribution:
![StockOne](https://github.com/MAJdeq/cs5060hw3/blob/main/assets/stock1Beta.png)
![StockTwo](https://github.com/MAJdeq/cs5060hw3/blob/main/assets/stock2Beta.png)

* For future parts, we decided to use the beta distribution. Using the Kolmogorov-Smirnov test, we measured goodness of fit based on the KS test statistic and the p-value. Comparing both stocks, the beta distribution generally yielded better results.
  *   For example, the beta distribution for Stock 2 yielded a statistic of 0.0383 and a p-value of 0.642, while the normal distribution for Stock 2 yielded a statistic of 0.0389 and a p-value of 0.625. However, the beta distribution for Stock 1 yielded a statistic of 0.0237 and a p-value of 0.984, while the normal distribution for Stock 1 yielded a statistic of 0.0264 and a p-value of 0.955. In this case, the normal distribution is better because of the higher statistic, but not by much, so we'll use the beta distribution.
 

*PART TWO*
* After performing, the monte carlo simulation based on the characteristics of our asset, we calculated the payoff of the option at maturity was $761.88. The following figure is a model displaying the first 10 paths for the stock:
![image](https://github.com/user-attachments/assets/c1a6aed1-03bf-4b2e-bfcc-fc6285530685)


*PART THREE*
* Using the beta distribution for to model the stock price for both stocks, we simulated the price paths for both stocks over a year period, and simulated the future price paths and option prices.
 * Scenario 1: The option that pays off if it outperforms the average value of Stock 1 and Stock 2 at maturity was $63.27.
 * Scenario 2: The option that pays off if it outperforms the maximum value of either Stock 1 or Stock 2 at maturity was $63.27.
