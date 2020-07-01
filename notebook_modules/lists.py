import pandas as pd

# keep old function to avoid breaking notebooks
def make_list(topic, name, dataframe):
	dataframe.to_csv(f"output/lists/{topic}-{name}.csv", index=False)

def save_db(dataframe, topic, name, sep=";"):
	dataframe.to_csv(f"output/db/{topic}-{name}.csv", index=False, sep=sep)

def load_db(topic, name, sep=";"):
	return pd.read_csv(f"output/db/{topic}-{name}.csv", sep=sep)
