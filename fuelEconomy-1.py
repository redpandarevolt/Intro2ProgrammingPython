# fuelEconomy.py
# Marcela Gomez

# This program takes a text file opens it and calculates the  number of cars,
# average city and highway mpg and counts the number of gas guzzlers.

from math import*

def convertData(filename):
    infile = open(filename,"r")
    dataList = infile.readlines()
    
    for i in range(len(dataList)): # scrolls through positions
        dataList[i]=float(dataList[i])
    vehicleCount = len(dataList)
    return dataList

    
def averageMPG(dataList):
    total = 0
    for value in dataList: #scrolls through the values themselves
        total = total + value
    average = total/len(dataList)
    return average
    

def countGasGuzzlers(list1, list2):
    GasGuzzlers = 0
    for i in range(len(list1)):
            if list1[i] < 22 or list2[i] < 27:
                GasGuzzlers = GasGuzzlers + 1
    return GasGuzzlers


def outputResults(cityAverage, hwyAverage, gasGuzzlers,vehicleCount):
    print("The total number of cars tested is " + str(vehicleCount) +".")
    print("The average mpg in the city is {0:0.2f}.".format(cityAverage))
    print("The hwy average mpg is {0:0.2f},".format(hwyAverage))
    print("Total gas guzzlers is "+ str(gasGuzzlers) + ".")


def main():
    cityList = convertData("carModelData_city.txt")
    hwyList = convertData("carModelData_hwy.txt")
    cityAverage = averageMPG(cityList)
    hwyAverage = averageMPG(hwyList)
    gasGuzzlers = countGasGuzzlers(cityList,hwyList)
    outputResults(cityAverage, hwyAverage, gasGuzzlers,vehicleCount = 35463)
    

main()
    
