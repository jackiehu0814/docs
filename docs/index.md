
<!-- logo -->
<img src="https://convect.ai/static/about/images/logo-color.png" 
    alt="Logo" width="400" height="100" style="display: block; margin: 0 auto" />

## Introduction

Convect AI Decision API is a collection of out-of-box APIs to support the most common decision problems in Supply Chain Optimization space. 
The goal is to let Convect manage the heavy lifting of building and tuning algorithms, allocating computing resources for your decision problems, so you can quickly add intelligence when developing supply chain decision applications.

Specifically, Convect currently provides APIs to solve two types of problems:

* [Automated forecasting](/forecast/overview)
* [Supply-demand planning](/flowopt/overview)


## Quickstart

Convect AI implements the [REST](https://blog.hubspot.com/website/what-is-rest-api) style APIs to enable users to build and trigger model runs for decision problems programmatically.
For a more comprehensive reference on the available APIs, please see [reference](https://forecast.convect.ai/api/schema/redoc/).

### Obtaining an API key

Register on [Convect Platform](https://forecast.convect.ai/), go to the account settings page to obtain an API key. Or contact [Convect support](mailto:hi@convect.ai) to obtain a demo key.

### Calling the API

Attach the API key in every header of the requests you send to a Convect API. For example, set `Authorization: Bearer {your API key}` in the header.

Convect APIs also accept and return `json` type data, so you can set `Accept: application/json` and `Content-type: application/json` in your header as well.


### Example - Automated forecasting

Here is an example of training and generating forecast by calling the automated forecasting APIs.

=== "python"
    ```python
    {!> forecast-quickstart.py !}
    ```

=== "curl"
    ```bash
    {!> forecast-quickstart.sh !}
    ```











