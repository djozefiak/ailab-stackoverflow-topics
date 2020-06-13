import pandas as pd

def aggregate_features(collection, timespan):
	cursor = collection.aggregate([
		{"$match": {
			"PostTypeId": 1,
			"CreationDate": {
				"$gte": timespan.start,
				"$lt": timespan.end
			}
		}},
		{"$unwind": "$Tags"},
		{"$group": {
			"_id": "$Tags",
			"frequency": {"$sum": 1},
			"score": {"$sum": "$Score"},
			"answers": {"$sum": "$AnswerCount"},
			"comments": {"$sum": "$CommentCount"},
			"favorites": {"$sum": "$FavoriteCount"},
			"views": {"$sum": "$ViewCount"}
		}},
		{"$sort": {
			"frequency": -1
		}}
	])
	result = list(cursor)
	if len(result) == 0:
		return pd.DataFrame()
	else:
		df = pd.DataFrame(result)
		df.rename({"_id": "tag"}, axis="columns", inplace=True)
		return df

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
	drop_list = [col for col in list(undecaying.columns) if col.endswith("_next")]
	undecaying.drop(drop_list, axis="columns", inplace=True)
	decaying.drop([*drop_list, "_merge"], axis="columns", inplace=True)
	assert len(top_current) == len(undecaying) + len(decaying), "Dataframe length mismatch!"
	undecaying["class"] = 0
	decaying["class"] = 1
	result = pd.concat([undecaying, decaying], ignore_index=True)
	return result

def split_class(dataset):
	x = dataset.drop(["tag", "class"], axis="columns")
	y = dataset[["class"]]
	return x, y
