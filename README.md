# cs5060hw3

## Collaborators:
* Ethan Ford
* Nathan Freestone

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
![StockTwo](https://github.com/MAJdeq/cs5060hw3/blob/main/assets/stock2Beta.png)
