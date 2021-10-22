"""
Function that sends a request to the MLflow model REST API to get a prediction from some input data.
"""
import os
from typing import List

import requests


def predict(x: List[float]) -> float or str:
    try:
        response = requests.post(
            url=os.getenv("MODEL_API"),
            headers={'content-type': 'application/json'},
            json={"data": [x]},
        )
        response.raise_for_status()
        output = str(response.json()[0])
    except (requests.HTTPError, IOError) as err:
        output = str(err)
    return output
