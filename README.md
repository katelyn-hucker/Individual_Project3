# Individual Project #3: Databricks ETL (Extract Transform Load) Pipeline
### Katelyn Hucker (kh509) [![CICD](https://github.com/katelyn-hucker/Individual_Project3/actions/workflows/cicd.yml/badge.svg)](https://github.com/katelyn-hucker/Individual_Project3/actions/workflows/cicd.yml)

#### Project Overview:
Three databricks notebooks which each perform ETL (Extract, Transform, Load) operations, and are then pushed to this github repo. I use of Delta Lake for data storage. This takes advantage of delta lake's capabilities of selective overwriting based on filters and partitions. We can also manually or automatically update your table schema without rewriting data with the data in a delta lake. I use Spark SQL for data transformations, like dropping unnecessary columns and removing null values. I have proper error handling and data validation, by having my code run through github actions. The data is also checked for table existance in every stage. This pipeline is triggered every Monday morning at 8AM EST. 
	

 #### ETL in Databricks Notebooks:
 ##### Extract:
 In these two images you see the 'ingest' notebook in the databricks workflow screen loading in data about the game, Phasmophobia. The notebook saves this as a "raw_phasmophobia_table." The two images below show the start and end of the notebook, respectively.

 ![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/506dadcc-1448-41e7-8f87-906116941fb9)


![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/6bfcc3a6-190f-452d-b9cf-be48d93062d5)

 ##### Transform:
 In this notebook I use spark SQL to select certain columns, drop nulls, and calculate two new columns to account for minutes to hours conversion. This is than saved as "clean_phasmophobia_table."This is also where it is saved into a Delta Lake as a Delta Table.
 ![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/e2999922-2403-4ab1-9123-05da51d4be1d)

![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/b6f33726-64ea-49f2-8494-264fcf8ad743)

 ##### Load:
 In this notebook I load the data. I plot some graphs of whether a user recommends a game or not (voted up = True) vs hours played.

 ![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/f55d3b33-a6f2-4150-a7cc-929947efa399)

![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/a8209dcf-3fcc-42d1-9f37-72cf66dd14f9)

##### Visualization:
![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/4e9d23b7-a9c1-45c9-ad40-0c41b4b0b97c)


##### The workflow run has passed:

![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/ed000911-0417-48f4-8f2c-b489645a47e9)

##### The workflow snapshot with trigger schedule:
 
![image](https://github.com/katelyn-hucker/Individual_Project3/assets/143521756/86c150e9-6cf7-4561-99bb-fd6e22a6cf21)

	
	
	
Video Demo: A YouTube link in README.md showing a clear, concise walkthrough and demonstration of your ETL pipeline, including the automated trigger and recommendations to the management team.
