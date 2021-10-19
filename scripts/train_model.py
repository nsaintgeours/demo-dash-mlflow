import mlflow
import numpy as np
from sklearn.dummy import DummyRegressor

model = DummyRegressor()
model.fit(
    X=np.random.rand(1000, 3),
    y=np.random.rand(1000, 1)
)
mlflow.sklearn.save_model(sk_model=model, path='../mlflow_model')
