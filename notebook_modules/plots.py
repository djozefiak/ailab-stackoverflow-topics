import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def setup():
	sns.set(style="whitegrid")
	plt.figure(figsize=(20,8))
	plt.xticks(rotation="vertical")

def setup_dist():
	sns.set(style="whitegrid")
	plt.figure(figsize=(8,8))
	ticks = [i / 10 for i in range(0, 11)]
	plt.xticks(ticks)
	plt.yticks(ticks)

def get_dataframe_from_csv(topic, name):
	return pd.read_csv(f"output/lists/{topic}-{name}.csv")

def make_tag_plot(topic, name, dataframe):
	setup()
	plt.title(name)
	sns.barplot(x="quarter", y=topic, data=dataframe)
	plt.savefig(f"output/plots/{topic}-{name}.png", bbox_inches="tight")

def make_frequency_plot(topic, name, dataframe):
	setup()
	plt.title(name)
	sns.barplot(x="tag", y=topic, data=dataframe)
	plt.savefig(f"output/plots/{topic}-{name}.png", bbox_inches="tight")

def make_distribution_plot(topic, name, dataframe):
	setup_dist()
	plt.title(name)
	sns.lineplot(x="percentage", y="share", data=dataframe)
	plt.savefig(f"output/plots/{topic}-{name}.png", bbox_inches="tight")
