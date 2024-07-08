import mlflow as mlflow
import pandas as pd


def main():
    print("akash")
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("cancer dataset pipeline experiment")
    mlflow.log_metric("zero_count_columns", 100)
    mlflow.log_param("first", "sample param")
    print("roshani")


if __name__ == '__main__':
    main()