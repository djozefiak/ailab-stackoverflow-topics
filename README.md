## Artificial Intelligence Lab 2020 @ Leibniz Universität Hannover

### Analysis and Prediction of Decaying Topics in Stack Overflow

### Introduction

* question answering sites, such as Stack Overflow, have become a major source for users
  * to share knowledge
  * to learn through the contributions of the community
* these sites rely on tags to organize and maintain its content
* choosing appropriate tags has a huge impact on the response time of questions
* the wide variety and high overlap of topics makes it difficult for inexperienced users to choose accurate tags
* many topics are becoming outdated and loosing the attractiveness as technology evolves

### Task

* in this work, we study and identify decaying tags
  * that are fading away from user interest
  * that have no or less potential to get answers for its questions
* this can be a good guideline for question askers
  * to choose accurate tags
  * to be aware of outdated topics to improve their questions
* in addition, the detection of decaying tags is important for site moderators
  * to manage the website content
  * to increase the user engagement

### Importing the data set

To import the data set and run the analysis scripts afterwards, [Python 3.7.8](https://www.python.org/downloads/release/python-378/) or newer is required. Used packages and libraries are defined in the `Pipfile`. A portable installation (zip-package) of [MongoDB 4.2.8](https://www.mongodb.com/try/download/community) or newer is recommended, but any kind of installation should work. The scripts for importing the data set expect the database to be running without authentication enabled. If you decide to use any other form of installation, you need to adjust the connection parameters accordingly.

The data set can be downloaded from [Stack Exchange Data Dump](https://archive.org/details/stackexchange), the archives `stackoverflow.com-Posts.7z` and `stackoverflow.com-Tags.7z` are required.

After downloading, the extracted files need to be placed in the `stack_exchange_data_dump/` directory inside the project root.

```
project_root/stack_exchange_data_dump/
  - Posts.xml
  - Tags.xml
```

Finally the scripts `posts_to_mongodb.py` and `tags_to_mongodb.py` start the import process. Importing `Tags.xml` should take a few seconds up to some minutes, while importing `Posts.xml` will take about an hour or longer. A progress bar will indicate the remaining time.

I strongly recommend generating [database indexes](https://docs.mongodb.com/manual/indexes/) using `database_management.ipynb` before doing any analysis. Doing so will increase the speed of an database query by a lot.

### Analysis

Different Jupyter Notebooks in the form of `some_analysis.ipynb` are placed in the project root for their respective topic. While some may show plots and figures directly in the Notebook, all output files are also placed in `project_root/output/` inside a subdirectory.

### References
1. [Min(e)d your tags: analysis of question response time in Stack Overflow](https://dl.acm.org/ft_gateway.cfm?id=3191901&type=pdf)
2. [Topic Shifts in Stack Overflow: Ask it Like Socrates](https://link.springer.com/chapter/10.1007/978-3-319-41754-7_18)
3. [What are developers talking about? An analysis of topics and trends in Stack Overflow](https://dl.acm.org/doi/10.1007/s10664-012-9231-y)
