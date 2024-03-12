import mlflow
import pandas as pd
import numpy as np

# TODO: Set tht MLFlow server uri
uri = ___________________
mlflow.set_tracking_uri(uri=uri)

# TODO: Provide model path/url
logged_model = ___________________

# Load model as a PyFuncModel.
loaded_model = mlflow.sklearn.load_model(logged_model)

# Input a random datapoint
data=np.array([[1.0,2.0,3.0,4.0]])

# TODO: Predict on a Pandas DataFrame. Due to the MLFlow functionality constrain.
#       The loaded model's predict function only accept dataframe as input instead of numpy array.
prediction=loaded_model.predict(___________)

# Print out prediction result
print(prediction)