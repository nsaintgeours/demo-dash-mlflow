"""
Function that sends a request to the MLflow model REST API to get a prediction from some input data.
"""
import os
from typing import List

import requests

MODEL_API = os.getenv("MODEL_API")


def post_prediction_request(x: List[float]) -> float or str:
    response = requests.post(
        url=f'http://{MODEL_API}/invocations',
        headers={'content-type': 'application/json'},
        json={"data": [x]},
    )
    try:
        response.raise_for_status()
        return response.json()[0]
    except requests.HTTPError:
        return "NO_PREDICTION"


if __name__ == '__main__':
    MODEL_API = "18.134.221.50:5001"
    y = post_prediction_request(x=[1, 2, 3])
    print(y)
