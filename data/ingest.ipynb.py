# Databricks notebook source
import pandas as pd

# COMMAND ----------

file1 = pd.read_csv("phas.csv")
spark_df = spark.createDataFrame(file1)

# COMMAND ----------

file_path = f'/FileStore/tables/{"phas"}.csv'

# COMMAND ----------

spark_df.write.mode('overwrite').csv(file_path)

# COMMAND ----------

from pyspark.sql import SparkSession

# COMMAND ----------

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType, StringType, BooleanType, DoubleType

# Define the schema for your CSV file
schema = StructType([
    StructField("recommendationid", LongType(), True),
    StructField("language", StringType(), True),
    StructField("review", StringType(), True),
    StructField("timestamp_created", LongType(), True),
    StructField("timestamp_updated", LongType(), True),
    StructField("voted_up", BooleanType(), True),
    StructField("votes_up", LongType(), True),
    StructField("votes_funny", LongType(), True),
    StructField("weighted_vote_score", DoubleType(), True),
    StructField("comment_count", LongType(), True),
    StructField("steam_purchase", BooleanType(), True),
    StructField("received_for_free", BooleanType(), True),
    StructField("written_during_early_access", BooleanType(), True),
    StructField("hidden_in_steam_china", BooleanType(), True),
    StructField("steam_china_location", DoubleType(), True),
    StructField("timestamp_dev_responded", DoubleType(), True),
    StructField("developer_response", StringType(), True),
    StructField("steamid", LongType(), True),
    StructField("num_games_owned", DoubleType(), True),
    StructField("num_reviews", DoubleType(), True),
    StructField("playtime_forever", DoubleType(), True),
    StructField("playtime_last_two_weeks", DoubleType(), True),
    StructField("playtime_at_review", DoubleType(), True),
    StructField("last_played", DoubleType(), True)
    # Add more fields as needed
])

# Read the CSV file with the specified schema
csv_file_path = "dbfs:/FileStore/tables/phas.csv"
game_data = spark.read.csv(csv_file_path, header=True, schema=schema)

# Show the DataFrame with column names
game_data.show()


# COMMAND ----------

game_data.head(10)

# COMMAND ----------

game_data.write.saveAsTable("Raw_Phasmophobia_Table")
