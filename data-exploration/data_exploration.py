import pandas as pd
from configuration import config

data_set = config.DATASET_PATH
class DataExploration:

    def get_customer_churn_dataset():
        df = pd.read_csv(data_set)
