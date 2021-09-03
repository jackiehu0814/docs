#!/bin/env bash

export BASE_URL='https://forecast.convect.ai/api/'
export TOKEN='DEMO KEY'
export AUTH_HEADER='Authorization: Bearer ${TOKEN}'

# create a dataset group
data_group_id=$(curl --request POST $BASE_URL/data_groups/ \
    -H 'Content-Type: application/json' \
    -H $AUTH_HEADER \
    --data '{"name": "Demo data group"}' | jq '.id')

# upload a dataaset
curl --request POST $BASE_URL/datasets/ \
    -H 'Content-Type: application/json' \
    -H $AUTH_HEADER \
    --data-binary @- << EOF
    {
        "name": "target time series",
        "dataset_type": "TARGET_TIME_SERIES",
        "path": data_url,
        "file_format": "csv",
        "frequency": "W",
        "data_group": ${data_group_id},
        "schemas": [
            {"name": "sku", "col_type": "key"},
            {"name": "week", "col_type": "time"},
            {"name": "qty", "col_type": "num"},
        ],
    }
EOF


# set up a forecat config
output_path='s3://convect-data/result/demo-run'

config_id=$(curl --request POST $BASE_URL/predictor-configs/ \
    -H 'Content-Type: application/json' \
    -H $AUTH_HEADER \
    --data-binary @- << EOF
    {
        "name": "12 week forecast config",
        "result_uri": output_path,
        "horizon": 14,
        "frequency": "W",
        "data_group": data_group_id,
    }
EOF | jq '.id'
)

# trigger a forecast run
run_id=$(curl --request POST $BASE_URL/predictors/ \
    -H 'Content-Type: application/json' \
    -H $AUTH_HEADER \
    --data '{"predictor_config": "${config_id}"}' | jq '.id')


# query the run status 
curl --request GET $BASE_URL/predictors/${run_id}/ \
    -H 'Content-Type: application/json' \
    -H $AUTH_HEADER

# retrieve the result
aws s3 cp $output_path ./result.csv
