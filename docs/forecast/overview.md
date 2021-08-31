

## Background

Convect Forecast provides the tool to automate building and tuning of a forecast model. 

Forecasting serves as the prerequisite of many decision tasks. For example, when deciding the right inventory level for a product, it's critical to have some insights on the number of units it will be sold in the future, and the uncertainty about the prediction (which is commonly neglected when people are talking about building predictive models).

Another example is the need to know how soon a vendor can deliver a batch of orders to your warehouse locations (lead time), when planning for the inventory level. Longer lead times means more uncertainty and higher safety stock levels.

Therefore, having a way to quickly build a forecast model is critical when developing such decision applications, so that you can move to building the prescriptive modeling faster.


### Features

Compared to traditional time series modeling, Convect Forecast excels at handling the following problems:

* Multivariate time series
* Multiple time series

[Multivariate time series forecasting](https://towardsdatascience.com/multivariate-time-series-forecasting-653372b3db36) problems tackle the situation when there are other features besides the time series itself can provide signals in predicting the future values.
This is quite common in e.g., retailing settings, where information about the SKU being predicted, such as brand, category, can help to decide the future demands. 

Traditional methods that are widely used in ERP systems (such as SAP) and spreadsheet-style forecasting workflows, like [Exponential Smoothing](https://en.wikipedia.org/wiki/Exponential_smoothing), and [ARIMA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average) are known to be lacking in providing this feature.

Multiple time series forecasting problems tackles the situation when there are many correlated time series need to forecasted with one shot. This is also common in e.g., the retailing setting. Product demands correlate with each other, e.g., in the famous [bear and diaper](https://www.forbes.com/forbes/1998/0406/6107128a.html) case, which can lead to higher accuracy if such information is utilized when building the model.

Popular forecasting library such as [Facebook Prophet](https://facebook.github.io/prophet/) is known to lacking support for this feature.


### What does Convect Forecast do for you

Convect Forecast ease the process of building forecasting models for multivariate, multiple time series problems. Specifically, it does the following things for users:

* Preprocess data to make it ready for model building
* Generate features to be used by models
* Augment data to increase model accuracy
* Choose the right strategy and level to build models on
* Choose the strategy to evaluate model candidates against history data
* Select the best model across a large pool of candidate models
* Package the data processing and modeling process as portable bundle so it can be deployed to make predictions on unseen data

## Workflow

To build a model using Convect Forecast, we need to go through the following steps:

* [Prepare data according to the given format](data-prepare.md)
* [Gain insights about the model performance on history data](run-backtest.md) (Optional)
* [Build and generate forecast](run-forecast.md)

