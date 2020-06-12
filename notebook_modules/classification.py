import pandas as pd

def split_top(tags, threshold=0.1):
	top = tags.head(int(threshold * len(tags)))
	return top

def split_top_bottom(tags, threshold=0.1):
	top = tags.head(int(threshold * len(tags)))
	bottom = tags.iloc[len(top):]
	assert len(tags) == len(top) + len(bottom), "Dataframe length mismatch!"
	return top, bottom

def classify(top_current, top_next):
	undecaying = pd.merge(top_current, top_next, how="inner", on="tag", suffixes=("", "_next"))
	decaying_left_join = pd.merge(top_current, top_next, how="left", on="tag", suffixes=("", "_next"), indicator=True)
	decaying = decaying_left_join[decaying_left_join["_merge"] == "left_only"].reset_index(drop=True)
	undecaying.drop("frequency_next", axis="columns", inplace=True)
	decaying.drop(["frequency_next", "_merge"], axis="columns", inplace=True)
	assert len(top_current) == len(undecaying) + len(decaying), "Dataframe length mismatch!"
	undecaying["class"] = 0
	decaying["class"] = 1
	result = pd.concat([undecaying, decaying], ignore_index=True)
	return result

def split_class(dataset):
	x = dataset[["frequency"]]
	y = dataset[["class"]]
	return x, y
