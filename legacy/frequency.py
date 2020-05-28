for quarter in quarters:
    pbar = tqdm(total=LIMIT, unit="query", desc=str(quarter), ascii=True)
    df = pd.DataFrame(columns=["tag", "frequency"])
    for tag in topTags:
        result = posts.count_documents({
            "PostTypeId": 1,
            "CreationDate": {
                "$gte": quarter.start,
                "$lt": quarter.end
            },
            "Tags": tag["TagName"]
        })
        index = len(df.index)
        df.loc[index] = [tag["TagName"], result]
        pbar.update()
    topTags.rewind()
    pbar.close()
    df = df.sort_values("frequency", ascending=False)
    df.reset_index(drop=True)
    df.frequency = df.frequency.astype("int")
    make_list("frequency", str(quarter), df)
    make_frequency_plot("frequency", str(quarter), df)
