#!/bin/env python

import requests
import os.path
import pandas as pd

BASE_ENDPOINT = "https://forecast.convect.ai/api/"
DEMO_KEY = "YOUR_API_KEY"

HEADER = {
    "Accept": "application/json",
    "Content-type": "application/json",
    "Authorization": "Bearer: {}".format(DEMO_KEY),
}

# create the data group

payload = {"name": "Demo data group"}
resp = requests.post(
    os.path.join(BASE_ENDPOINT, "data_groups/"),
    json=payload,
)
data_group_id = resp.json()["id"]

# upload the dataset
data_url = "https://convect-test-data.s3.us-west-2.amazonaws.com/forecast_test_data/target_ts.csv"
payload = {
    "name": "target time series",
    "dataset_type": "TARGET_TIME_SERIES",
    "path": data_url,
    "file_format": "csv",
    "frequency": "W",
    "data_group": data_group_id,
    "schemas": [
        {"name": "sku", "col_type": "key"},
        {"name": "week", "col_type": "time"},
        {"name": "qty", "col_type": "num"},
    ],
}
resp = requests.post(
    os.path.join(BASE_ENDPOINT, "datasets/"),
    json=payload,
)
dataset_id = resp.json()["id"]


# build the forecating config
url = os.path.join(BASE_ENDPOINT, "predictor-configs/")
output_path = "s3://convect-data/result/demo-run"
payload = {
    "name": "14 week forecast config",
    "result_uri": output_path,
    "horizon": 14,
    "frequency": "W",
    "data_group": data_group_id,
}

resp = requests.post(
    os.path.join(BASE_ENDPOINT, "predictor-configs/"),
    json=payload,
)
config_id = resp.json()["id"]

# trigger the forecasting
payload = {"predictor_config": config_id}
resp = requests.post(
    os.path.join(BASE_ENDPOINT, "predictors/"), json=payload
)
predictor_id = resp.json()["id"]

# query the result
resp = requests.get(
    os.path.join(
        BASE_ENDPOINT, "predictors/", f"{predictor_id}/"
    )
)
print(resp.json())

# retrieve the result
df = pd.read_csv(output_path)
