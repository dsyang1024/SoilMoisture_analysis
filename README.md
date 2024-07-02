# Readme
You should run these two scripts for the analysis
All the detailed explanation about each function is in the .ipynb file
***
## ___00_Script_Observed Soil Moisture Analysis.ipynb (in the root directory)___
### Description
- this script runs analysis based on the observed soil moisture sensor (field observation)
- this script downloads observed soil moisture data automatically from the thingsboard server
- this script takes approx. 4 min to finish
- this script must be run everyday, if you skip, that data will not be recovered unless you change the 'TDY' variable at the top
- this script exports field capacity in csv form in [./05_fc_results]
- this script exports field capacity graph for each event in [./06_fc_graphs]
### Related directories in the root
- `[./01_Raw_data]` Automatically downloaded soil moisture data will be saved in this directory
- `[./02_Clean_data]` Cleaned data in the raw data will be saved in this directory
- `[./03_Soil_moisture_graphs]` Box plot of the soil moisture values for each station will be saved in this directory
- `[./04_fc_results]` field capacity will be saved records will be saved here in daily basis
- `[./05_fc_graphs]` field capacity graphs for each event will be saved in this directory
- `[./06_Deficit_results]` Deficit calculated will be saved in this directory for each day and as integrated, for each crop
- `[./00_Current_fieldCapacity.csv]` file for the most recent FCs for each stations


***
## ___00_Script_Checkbook Soil Moisture Analysis.ipynb (in the root directory)___
### Description
- this script runs checkbook process through the Penman Monteith equation and water balance check
- this script reads Mesonet API data (download automatically) and Mesonet manually downloaded data (30-min)
- this script takes approx. 2 min to finish
- this script exports all the variables in .csv and .xlsx format to the root directory and also exports summary file
### Related directories in the root
- `[./11_Clean_Weather_data]` Weather data converted from raw data or Mesonet data
- `[./12_API_Weather_data]` Weather data automatically downloaded from the script will be in this directory
- `[./13_Mesonet_data]` Weather data manually downloaded from the Web UI should be saved here as 'Table (30-min).csv'
- `[./14_L4_Soilmoisture_data]` this script will download soil moisture from layer 4 for upward flux calculation automatically and the data will be saved here
- `[./15_Crop_data]` Crop coefficient is needed for ET calculation and this record is in 'Crop_coefficient.xlsx'
- `[./Irrigation_log.xlsx]` irrigation record file
- `[./Penman_Irrigation_results/summary.csv/xlsx]` results file from the script
- `[./00_CheckBook_Corn_all_deficit_graph.png]` Corn deficit graph for OBS/Checkbook
- `[./00_CheckBook_Soybean_all_deficit_graph.png]` Soybean deficit graph for OBS/Checkbook


## Others
- `[./99_Data_backup]` related data not in use anymore is stored in this directory
- `[./99_Script_Backup]` scripts made in the past are stored in this directory
