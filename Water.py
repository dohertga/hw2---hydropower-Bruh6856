# Program Filename: Water.py
# Author: Zachary Lehman
# Date: 4/25/2022
# Description: Reads datasheet to calculate various values
# of power usage in different years.
# Input: Year 1, Year 2, and the Power Type.
# Output: TWH Year 1, TWH Year 2, percentage increase,
# percent of world for Power Type Year 1, percent of world for Power Type Year 2.

import pandas as pa

# Assign inputs
spreadsheet = pa.read_csv('energy_use_terrawatthours.csv')
year1 = input("year 1 ")
year2 = input("year 2 ")
powerType = input("power type ")

# Makes list of tuples of power outputs for each selected year
year1PowList = []
year2PowList = []
for i in range(len(spreadsheet)):
    if  str(spreadsheet.at[i, 'year']) == str(year1):
        year1PowList.append((spreadsheet.at[i, 'generation_twh'], spreadsheet.at[i, 'variable']))
    if str(spreadsheet.at[i, 'year']) == str(year2):
        year2PowList.append((spreadsheet.at[i, 'generation_twh'], spreadsheet.at[i, 'variable']))
# Makes list from previous one only containing data from selected power type
year1PowTypeList = []
year2PowTypeList = []
for i in range(len(year1PowList)):
    if str(year1PowList[i][1]) == str(powerType):
        year1PowTypeList.append(year1PowList[i][0])
for i in range(len(year2PowList)):
    if str(year2PowList[i][1]) == str(powerType):
        year2PowTypeList.append(year2PowList[i][0])
# Makes sums from all the lists
year1PowTypeSum = 0
year2PowTypeSum = 0
year1PowSum = 0
year2PowSum = 0
for i in range(len(year1PowTypeList)):
    year1PowTypeSum += year1PowTypeList[i]
for i in range(len(year2PowTypeList)):
    year2PowTypeSum += year2PowTypeList[i]
for i in range(len(year1PowList)):
    year1PowSum += year1PowList[i][0]
for i in range(len(year2PowList)):
    year2PowSum += year2PowList[i][0]

# Difference between input years
yearDiff = int(year2) - int(year1)
# Calculates percentages for global power increase in percent between the two input years,
# and the percentage of world power generation the input power type took up in the input years
perInc = round(((year1PowSum/year2PowSum) * 100), 2)
perTypeYear1 = round(((year1PowTypeSum/year1PowSum) * 100), 2)
perTypeYear2 = round(((year2PowTypeSum/year2PowSum) * 100), 2)
print("The total world power consumption in", str(year1), "was", str(year1PowSum),
      "terawatt-hours and in", str(year2), "the consumption has increased to",
      str(year2PowSum), "terawatt-hours.", "That means world power generation has increased by"
      , str(perInc), "% over the past", str(yearDiff), "years.\n", "In year", str(year1),
      str(perTypeYear1), "% of world energy came from", str(powerType), ", and in", str(year2),
      str(perTypeYear2), "% of world energy came from", str(powerType), ".")