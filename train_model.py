# This file is designed based on MlFlow tutorial
# https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html


import mlflow
from utility import pipeline
from mlflow.models import infer_signature

# TODO: Set tht MLFlow tracking server uri
uri = 'http://127.0.0.1:6001'
# Use mlflow.set_tracking_uri to set the uri
mlflow.set_tracking_uri(uri)

# Set experiment name
email="yiwenz5@andrew.cmu.edu" # TODO: Use a customized experiment name
experiment_name=f"{email}-lab7"
mlflow.set_experiment(experiment_name)

# Begin the model training and evaluation process

# TODO: Generates train and test dataset using `pipeline.data_preprocessing` function
X_train,X_test,y_train,y_test= pipeline.data_preprocessing()

# Train the model:
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "multi_class": "auto",
    "random_state": 8888,
}

# TODO: Use `pipeline.train_logistic_regression` to generate trained model
trained_model= pipeline.train_logistic_regression(X_train, y_train, params)
# TODO: use `pipeline.evaluation` to evaluate the model
accuracy = pipeline.evaluation(trained_model, X_test, y_test)

# Log model and metrics to tracking serverhost>
# Start an MLflow run
run_name=None # You can specify a run name or let MLFlow choose one for you.
with mlflow.start_run(run_name=run_name):
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the accuracy metric
    mlflow.log_metric("accuracy", accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Basic LR model for iris data")

    # Infer the model signature
    signature = infer_signature(X_train, trained_model.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=trained_model,
        artifact_path="iris_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="IRIS_Model",
    )
