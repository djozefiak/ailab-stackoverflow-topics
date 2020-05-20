import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def make_tag_plot(topic, name, dataframe):
	plt.figure(figsize=(20,8))
	plt.title(name)
	plt.xticks(rotation="vertical")
	sns.set(style="whitegrid")
	sns.barplot(x="quarter", y=topic, data=dataframe)
	plt.savefig(f"output/plots/{topic}-{name}.png")

def make_tag_plot_from_csv(topic, name):
	dataframe = pd.read_csv(f"output/lists/{topic}-{name}.csv")
	plt.figure(figsize=(20,8))
	plt.title(name)
	plt.xticks(rotation="vertical")
	sns.set(style="whitegrid")
	sns.barplot(x="quarter", y=topic, data=dataframe)
	plt.savefig(f"output/plots/{topic}-{name}.png")
