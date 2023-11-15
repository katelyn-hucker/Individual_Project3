# Databricks notebook source
# Register the table
spark.sql("CREATE TABLE IF NOT EXISTS Raw_Phasmophobia_Table")

# Query the table
loaded_data = spark.sql("SELECT * FROM Raw_Phasmophobia_Table")

# Show the loaded data
loaded_data.show()

# COMMAND ----------

needed_game_data = loaded_data.select("recommendationid","review", "playtime_at_review","voted_up","playtime_forever")

# COMMAND ----------

needed_game_data.show()

# COMMAND ----------

null_values = needed_game_data.filter(needed_game_data["recommendationid"].isNull() |
                                      needed_game_data["review"].isNull() |
                                      needed_game_data["playtime_at_review"].isNull() |
                                      needed_game_data["voted_up"].isNull() |
                                      needed_game_data["playtime_forever"].isNull())

# Show null values
#null_values.show()

# Remove rows with null values
needed_game_data_no_nulls = needed_game_data.dropna()

# Show the DataFrame without null values
needed_game_data_no_nulls.show()


# COMMAND ----------

from pyspark.sql.functions import col
needed_game_data_no_nulls = needed_game_data_no_nulls.withColumn("playtime_at_review_hours", col("playtime_at_review") / 60)
needed_game_data_no_nulls = needed_game_data_no_nulls.withColumn("playtime_forever_hours", col("playtime_forever") / 60)

# COMMAND ----------

# Save the DataFrame as a Delta table, overwriting the existing table
needed_game_data_no_nulls.write.format("delta").mode('overwrite').option("overwriteSchema", "true").saveAsTable("Clean_Phasmophobia_Table")

