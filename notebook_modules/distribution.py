import pandas as pd

def aggregate(collection, timespan, full=False):
	if full:
		datefilter = {
			"$lt": timespan.end
		}
	else:
		datefilter = {
			"$gte": timespan.start,
			"$lt": timespan.end
		}

	cursor = collection.aggregate([
		{"$match": {
			"PostTypeId": 1,
			"CreationDate": datefilter
		}},
		{"$unwind": "$Tags"},
		{"$group": {
			"_id": "$Tags",
			"frequency": {"$sum": 1}
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

def distribute(aggr):
	dist = []
	unique_tags = len(aggr.index)
	total_tags = aggr.frequency.sum()
	resolution = 100
	for p in range(0, resolution + 1):
		percentage = p / resolution
		index = int(unique_tags * percentage)
		part = aggr.head(index)
		share = part.frequency.sum() / total_tags
		dist.append([percentage, share, len(part.index)])
	return pd.DataFrame(dist, columns=["percentage", "share", "count"])
