def make_tag_list(topic, name, dataframe):
	dataframe.to_csv(f"output/lists/{topic}-{name}.csv", index=False)
