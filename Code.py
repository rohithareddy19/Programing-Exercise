# -*- coding: utf-8 -*-

# took 3.5 to 4 hours to finish

import pandas as pd
import time

start_time = time.time()

#Reading input data and converting it to datframe
input_data = pd.read_csv(r"C:\Users\Reddy Rohitha\Desktop\Quantlab\input.csv", header = None)

symbolList = []
timeList = []
volumeList = []
priceList = []
symbolShareList = []
MaxTimeGapList = []
VolumeList = []
WeightedAvgPriceList = []
MaxPriceList = []

#Function to find the max time gap
#this function subtracts consecutive elements and sorts the result in descending order
#and thus gives the max time gap
def MaxTimeGap(eachSymbolData):
    global timeGap, maxTimeGap
    timeDiffList = []
    timeList = eachSymbolData[0].tolist()#getting the timestamp column as a list
    listLength = len(timeList)#finding total number of elements 
    for i in range(listLength):
        if i+1 != listLength:
            timeGap = timeList[i+1] - timeList[i]
            timeDiffList.append(timeGap)
            timeDiffList.sort(reverse =True)
            maxTimeGap = timeDiffList[0]
    return maxTimeGap

#Function for total volume
def Volume(eachSymbolData):
    volume = eachSymbolData[2].sum()
    return volume

# Function for max trade price
def MaxTradePrice(eachSymbolData):
    maxTradePrice = eachSymbolData[3].max()
    return maxTradePrice

#Function for weighted average price
def WeightedAveragePrice(eachSymbolData):
    global sumPrice, sumVolume
    price = []
    priceList = eachSymbolData[3].tolist()
    volumeList = eachSymbolData[2].tolist()
    price = [a*b for a,b in zip(priceList,volumeList)]
    sumPrice = sum(price)
    sumVolume = sum(volumeList)
    weightedAveragePrice = sumPrice//sumVolume
    return weightedAveragePrice
    
#reads the share symbol and aggregates all the rows for same symbol into a dataframe
#each dataframe is further processed by separate functions for getting respective output
#and finally stored in lists 
for symbol in input_data[1]:
    if symbol  not in symbolList:
        eachSymbolData = input_data.loc[input_data[1] == symbol]
        maxTimeGap = MaxTimeGap(eachSymbolData)
        volume = Volume(eachSymbolData)
        maxTradePrice = MaxTradePrice(eachSymbolData)
        weightedAveragePrice = WeightedAveragePrice(eachSymbolData)
        symbolShareList.append(symbol)
        MaxTimeGapList.append(maxTimeGap)
        VolumeList.append(volume)
        WeightedAvgPriceList.append(weightedAveragePrice)
        MaxPriceList.append(maxTradePrice)
    symbolList.append(symbol)
    
#each list is being added as the column of output dataframe  
output = pd.DataFrame()
output['Symbol'] = symbolShareList
output['MaxTimeGap'] = MaxTimeGapList
output['Volume'] = VolumeList
output['WeightedAveragePrice'] = WeightedAvgPriceList
output['MaxPrice'] = MaxPriceList
outputSorted = output.sort_values(by = 'Symbol')


#output is stored in csv file
outputSorted.to_csv(r"C:\Users\Reddy Rohitha\Desktop\Quantlab\output.csv", sep=',', encoding='utf-8',index = False)

#printing the execution time
print("Total Execution Time %s seconds:" % (time.time() - start_time))
    


    
    
    
    
