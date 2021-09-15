
## What is backtesting

![](https://facebook.github.io/prophet/static/diagnostics_files/diagnostics_4_0.png)

Backtesting is a technique to go back to the past and generate a forecast result at a *cutoff* date, then compare the result with the actual observations to compute the accuracy metrics of a model.

For example, if I would like to generate the sales forecast for a store during the coming Thanksgiving season, a good backtesting strategy is to go back 1 year, to a date prior to Thanksgiving, and to generate a forecast result. Then compare the result with last year's Thanksgiving sales to gain an understanding how my model is likely to perform for this year based on last year's performance.

## Set up a backtesting

Before setting up a backtesting experiment, we will go through the same process of [preparing data](data-prepare.md) and [constructing](run-forecast.md) a `predictor-config`.

Once you have the `predictor-config`, we first create a `backtest-config` by

```python
import requests
import os.path

BASE_ENDPOINT = "https://forecast.convect.ai/api/"
DEMO_KEY = "YOUR_API_KEY"

HEADER = {
    "Accept": "application/json",
    "Content-type": "application/json",
    "Authorization": "Bearer {}".format(DEMO_KEY),
}

payload = {
    backtest_dates: ["2019-11-10", "2019-12-20"],
    name: "holiday sales backtest",
    result_uri: "s3://convect-data/result/backtest-results/",
    predictor: YOUR_PREDICTOR_ID
}

resp = requests.post(
    os.path.join(BASE_ENDPOINT, "backtest-configs/"),
    json=payload,
    headers=HEADER
)

config_id = resp.json()["id]
```

Then we trigger the actual runs based on the config by

```python
payload = {"backtest_config": config_id}
resp = requests.post(
    os.path.join(BASE_ENDPOINT, "backtesters/"),
    json=payload,
    headers=HEADER
)
job_id = resp.json()["id]
```

And you can query the status of the run similarly to the normal forecast runs by 

```python
resp = requests.get(
    os.path.join(BASE_ENDPOINT, "backtesters", f"{job_id}/"),
    headers=HEADER
)
print(resp.json())
```
