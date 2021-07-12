import pandas as pd
import random
import numpy
import sqlalchemy as sqla
from datetime import datetime

print("Preparing Data...")

plant_1 = pd.read_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_1_Generation_Data.csv")
plant_2 = pd.read_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_2_Generation_Data.csv")
weather_sensor_1 = pd.read_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_1_Weather_Sensor_Data.csv")
weather_sensor_2 = pd.read_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_2_Weather_Sensor_Data.csv")

p1_SOURCE_KEYS = plant_1.groupby("SOURCE_KEY").sum()
p1_SOURCE_KEYS = p1_SOURCE_KEYS.reset_index()
p1_SOURCE_KEYS = p1_SOURCE_KEYS["SOURCE_KEY"].tolist()
p1_number_of_panels = len(p1_SOURCE_KEYS)  

print(p1_SOURCE_KEYS)

p2_SOURCE_KEYS = plant_2.groupby("SOURCE_KEY").sum()
p2_SOURCE_KEYS = p2_SOURCE_KEYS.reset_index()
p2_SOURCE_KEYS = p2_SOURCE_KEYS["SOURCE_KEY"].tolist()
p2_number_of_panels = len(p2_SOURCE_KEYS)  

###-- Overall Plant Data --###
plant_1["DATE_TIME"] = plant_1["DATE_TIME"] + ":00"
plant_1["DATE_TIME"] = pd.to_datetime(plant_1["DATE_TIME"], format='%d-%m-%Y %H:%M:%S')
plant_1[["_DATE", "_TIME"]] = plant_1.DATE_TIME.astype(str).str.split(" ", expand=True)
plant_1["AC_POWER"] = plant_1["AC_POWER"] * 10
plant_1["AC_POWER"] = numpy.where(plant_1["AC_POWER"] > plant_1["DC_POWER"],
                                plant_1["AC_POWER"] * (100 - (((plant_1["AC_POWER"] / plant_1["DC_POWER"]) * 100) - 100)) / 100,
                                plant_1["AC_POWER"])
plant_1["VOLTAGE"] = [(random.uniform(21.8, 22.2) / p1_number_of_panels) for k in plant_1.index] 
plant_1["VOLTAGE"] = numpy.where(plant_1["DC_POWER"] == 0, 0, plant_1["VOLTAGE"])
plant_1["AMPERAGE"] = numpy.where(plant_1["VOLTAGE"] == 0, 0, (plant_1["DC_POWER"] / plant_1["VOLTAGE"]) / 1000)
plant_1["POWER_FACTOR"] = numpy.where(plant_1["DC_POWER"] == 0, 0, (plant_1["AC_POWER"] / plant_1["DC_POWER"]) * 100)
plant_1["REACTIVE_POWER"] = (plant_1["DC_POWER"] - plant_1["AC_POWER"]) / 1000
plant_1 = plant_1.round({"DC_POWER": 3, "AC_POWER": 3, "VOLTAGE": 3, "AMPERAGE": 3, "REACTIVE_POWER": 3, "POWER_FACTOR": 2, "DAILY_YIELD": 3})

plant_2[["_DATE", "_TIME"]] = plant_2.DATE_TIME.astype(str).str.split(" ", expand=True)
plant_2["AC_POWER"] = numpy.where(plant_2["AC_POWER"] > plant_2["DC_POWER"],
                                plant_2["AC_POWER"] * (100 - (((plant_2["AC_POWER"] / plant_2["DC_POWER"]) * 100) - 100)) / 100,
                                plant_2["AC_POWER"])
plant_2["VOLTAGE"] = [(random.uniform(21.8, 22.2) / p2_number_of_panels) for k in plant_2.index] 
plant_2["VOLTAGE"] = numpy.where(plant_2["DC_POWER"] == 0, 0, plant_2["VOLTAGE"])
plant_2["AMPERAGE"] = numpy.where(plant_2["VOLTAGE"] == 0, 0, (plant_2["DC_POWER"] / plant_2["VOLTAGE"]) / 1000)
plant_2["POWER_FACTOR"] = numpy.where(plant_2["DC_POWER"] == 0, 0, (plant_2["AC_POWER"] / plant_2["DC_POWER"]) * 100)
plant_2["REACTIVE_POWER"] = (plant_2["DC_POWER"] - plant_2["AC_POWER"]) / 1000
plant_2 = plant_2.round({"DC_POWER": 3, "AC_POWER": 3, "VOLTAGE": 3, "AMPERAGE": 3, "REACTIVE_POWER": 3, "POWER_FACTOR": 2, "DAILY_YIELD": 3})

# ###-- Overall Weather Sensor Data --###
weather_sensor_1 = weather_sensor_1.round({'AMBIENT_TEMPERATURE': 2, 'MODULE_TEMPERATURE': 2})
weather_sensor_1["DATE_TIME"] = weather_sensor_1["DATE_TIME"] + ":00"
weather_sensor_1["DATE_TIME"] = weather_sensor_1["DATE_TIME"].str.replace("/", "-")
weather_sensor_1["DATE_TIME"] = pd.to_datetime(weather_sensor_1["DATE_TIME"], format='%d-%m-%Y %H:%M:%S')
weather_sensor_1[["_DATE", "_TIME"]] = weather_sensor_1.DATE_TIME.astype(str).str.split(" ", expand=True)

weather_sensor_2 = weather_sensor_2.round({'AMBIENT_TEMPERATURE': 2, 'MODULE_TEMPERATURE': 2})
weather_sensor_2["DATE_TIME"] = weather_sensor_2["DATE_TIME"].str.replace("/", "-")
weather_sensor_2[["_DATE", "_TIME"]] = weather_sensor_2.DATE_TIME.astype(str).str.split(" ", expand=True)

print(weather_sensor_1)

# ###-- OPC Device Simulator Program --###

# plants = pd.concat([plant_1, plant_2])
# plants["DATE_TIME"] = plants["DATE_TIME"].astype(str)
# plants = plants.loc[plants["_DATE"] == '2020-05-15']

# columns = plants.drop(columns=['_TIME', 'PLANT_ID', 'SOURCE_KEY', '_DATE', 'TOTAL_YIELD']).columns
# SOURCE_KEYS = p1_SOURCE_KEYS.copy()
# SOURCE_KEYS.extend(p2_SOURCE_KEYS)
# rows = []

# for col in columns:
#     for key in SOURCE_KEYS:
#         SOURCE_KEY_DATA = plants.loc[plants["SOURCE_KEY"] == key]
#         value_source_list = SOURCE_KEY_DATA[col].tolist()
#         value_source = "list("
#         for index, val in enumerate(value_source_list):
#             if index == len(value_source_list) - 1:
#                 value_source += str(val) + ")"
#             else:
#                 value_source += str(val) + ", "
#         if key in p1_SOURCE_KEYS:
#             browse_path = "Plant1/" + key + "/" + col
#         else:
#             browse_path = "Plant2/" + key + "/" + col
#         time_interval = 0
#         data_type = ""
#         if col == "DATE_TIME":
#             data_type = "String"
#         else:
#             data_type = "Double"
#         row = {"Time Interval": time_interval, "Browse Path": browse_path, "Value Source": value_source, "Data Type": data_type}
#         rows.append(row)

# device = pd.DataFrame(rows, columns=["Time Interval", "Browse Path", "Value Source", "Data Type"])
# device.to_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\PlantSimulatorProgram.csv", index=False)

weather_sensor_1["DATE_TIME"] = weather_sensor_1["DATE_TIME"].astype(str)
weather_sensor_1 = weather_sensor_1.loc[weather_sensor_1["_DATE"] == '2020-05-15']

columns = weather_sensor_1.drop(columns=['_TIME', 'PLANT_ID', 'SOURCE_KEY', '_DATE']).columns
SOURCE_KEY = "HmiyD2TTLFNqkNe"

rows = []

for col in columns:
    value_source_list = weather_sensor_1[col].tolist()
    value_source = "list("
    for index, val in enumerate(value_source_list):
        if index == len(value_source_list) - 1:
            value_source += str(val) + ")"
        else:
            value_source += str(val) + ", "
    browse_path = "Plant1/" + SOURCE_KEY + "/" + col
    time_interval = 0
    data_type = ""
    if col == "DATE_TIME":
        data_type = "String"
    else:
        data_type = "Double"
    row = {"Time Interval": time_interval, "Browse Path": browse_path, "Value Source": value_source, "Data Type": data_type}
    rows.append(row)

device = pd.DataFrame(rows, columns=["Time Interval", "Browse Path", "Value Source", "Data Type"])
device.to_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\WeatherSensorSimulatorProgram.csv", index=False)


###--- Aggregates ---###

# Average Production in kW per time interval for each panel
# avg = plant_1[["SOURCE_KEY", "_TIME", "DC_POWER", "AC_POWER", "REACTIVE_POWER", "POWER_FACTOR"]].groupby(["SOURCE_KEY", "_TIME"]).mean()
# avg = avg.reset_index()
# avg = avg.round({"DC_POWER": 3, "AC_POWER": 3, "REACTIVE_POWER": 3, "POWER_FACTOR": 2})

# # Total Production in kW per day for each panel
# total_day = plant_1[["SOURCE_KEY", "_DATE", "DC_POWER", "AC_POWER", "REACTIVE_POWER", "VOLTAGE", "AMPERAGE"]].groupby(["SOURCE_KEY", "_DATE"]).sum()
# total_day = total_day.reset_index()
# total_day = total_day.round(3)

# # Total Production of plant_1 per time interval each day
# total_interval = plant_1[["DATE_TIME", "DC_POWER", "AC_POWER", "REACTIVE_POWER", "VOLTAGE", "AMPERAGE"]].groupby(["DATE_TIME"]).sum()
# total_interval["POWER_FACTOR"] = total_interval["AC_POWER"] / total_interval["DC_POWER"]
# total_interval = total_interval.reset_index()
# total_interval = total_interval.round({"DC_POWER": 3, "AC_POWER": 3, "REACTIVE_POWER": 3, "VOLTAGE": 3, "AMPERAGE": 3, "POWER_FACTOR": 2})


###-- SQL --###

# print("Executing SQL...")

# engine = sqla.create_engine("mssql+pymssql://Ignition:Ignition@FA-0411:1433/Ignition")
# con = engine.connect()

# create_tables = open(r"C:\Users\Jake.Herington\Documents\SQL Scripts\SolarDB\create_tables.sql")
# query = create_tables.read()
# con.execute(query)

# plant_1.to_sql('plant_1', con=engine, if_exists='append', chunksize=1000, index=False)
# avg.to_sql('avgs', con=engine, if_exists='append', chunksize=1000, index=False)
# total_day.to_sql('total_day', con=engine, if_exists='append', chunksize=1000, index=False)
# total_interval.to_sql('total_interval', con=engine, if_exists='append', chunksize=1000, index=False)
# weather_sensor_1.to_sql('weather_sensor_1', con=engine, if_exists='append', chunksize=1000, index=False)

# con.close()
# engine.dispose()

# print("...Complete")

###-- CSV --###

#plant_1.to_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_1_Generation_Data_new.csv")
#avg.to_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_1_Avg_Data.csv")
#total.to_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_1_Total_Data.csv")
#total_interval.to_csv(r"C:\Users\Jake.Herington\Documents\Solar Datasets\Plant_1_Total_Interval_Data.csv")


#---------------------------------------------------------------------------------------------------#