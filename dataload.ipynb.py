# Databricks notebook source
spark.sql("CREATE TABLE IF NOT EXISTS Clean_Phasmophobia_Table")

# Query the table
loaded_data = spark.sql("SELECT * FROM Clean_Phasmophobia_Table")

# Show the loaded data
loaded_data.show()

# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# COMMAND ----------


df_pd = loaded_data.toPandas()
x_limit = (0, 10000)  # Adjust the range as needed
y_limit = (-.05, 1.05)
# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='playtime_forever_hours', y='voted_up', data=df_pd)
plt.title('Scatter Plot of Playtime vs Voted Up')
plt.xlabel('Playtime Forever')
plt.ylabel('Voted Up (True/False)')
plt.xlim(x_limit)
plt.ylim(y_limit)
plt.show()



# COMMAND ----------


x_limit = (0, 4000)  # Adjust the range as needed
y_limit = (-.05, 1.05)
# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='playtime_at_review_hours', y='voted_up', data=df_pd)
plt.title('Scatter Plot of Playtime vs Voted Up')
plt.xlabel('Playtime at Reivew')
plt.ylabel('Voted Up (True/False)')
plt.xlim(x_limit)
plt.ylim(y_limit)
plt.show()

