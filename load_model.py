import mlflow
import pandas as pd
import numpy as np

# Set tht MLFlow server url
mlflow.set_tracking_uri(uri="http://127.0.0.1:6363")

# Provide model path/url
logged_model = r'runs:/13356b3e8e3b42e9b99a3d53565d1640/iris_model'

# Load model as a PyFuncModel.
loaded_model = mlflow.sklearn.load_model(logged_model)

# Input a random datapoint
data=np.array([[1.0,2.0,3.0,4.0]])

# Predict on a Pandas DataFrame.
prediction=loaded_model.predict(pd.DataFrame(data))

# Print out prediction result
print(prediction)