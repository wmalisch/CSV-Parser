
## Computes the smallest value in a list of floats
# @param myList is a list of positive floats
# @return the smallest value in the list
def myMin(minList):
    smallest = minList[0]
    for i in range(1,len(minList)):
        if minList[i] < smallest:
            smallest = minList[i]
    return smallest

## Computes the largest value in a list of floats
# @param maxList is a list of positive floats
# @return the largest value in the list
def myMax(maxList):
    largest = maxList[0]
    for i in range(1,len(maxList)):
        if maxList[i] > largest:
            largest = maxList[i]
    return largest

## Computes the average of a list of floats
# @param avgList is a list of positive floats
# @return the average of the list
def myAverage(avgList):
    sum = 0.0
    for i in range(0,len(avgList)):
        sum = sum + avgList[i]
    avg = sum/len(avgList)
    return avg

## Sorts and computes the median of a list of floats
# @param medianLst is a list of positive floats
# @return the median of a sorted list
def myMedian(medianLst):
    length = len(medianLst)
    if length % 2 == 0:
        point1 = float(sorted(medianLst)[length//2])
        point2 = float(sorted(medianLst)[length//2-1])
        sum = point1 + point2
        median = sum/2
    else:
        median = sorted(medianLst)[length // 2]
    return median

## Computes the standard deviation of a list of floats
# @param stdList is a list of positive floats
# @return the standard deviation of a sorted list
def myStandardDeviation(stdList):
    # Calculate the average
    sum = 0
    for i in stdList:
        sum = sum + i
    avg = sum / len(stdList)

    # Calculate the sum of squares
    sumSqr = 0
    for i in stdList:
        sqr = (i - avg) ** 2
        sumSqr = sumSqr + sqr
    # Compute the standard deviation
    stdev = ((1/(len(stdList) - 1)) * sumSqr) ** (1/2)
    return stdev

## Counts the amount of data points in a list of floats that are within a given set of intervals
# @param data is a list of positive floats
# @param size is the size of each interval, inclusive of the lower bound
# @return a list for the count of data points within the interval
def myCountBins(data, size):
    # Find the largest possible number in the list
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]

    # Establish the number of bins to include all values in the list
    numberBins = round((largest / size)) + (largest % size > 0)
    print(numberBins)

    binLst = []
    # Set up a list that has all intervals of bins, in reverse because it is easier
    while numberBins >= 0:
        binLst.append(numberBins * size)
        numberBins = numberBins - 1

    # Reverse the list so it makes more sense in the next for loops
    for i in range(0, len(binLst) // 2):
        temp = binLst[i]
        binLst[i] = binLst[len(binLst) - 1 - i]
        binLst[len(binLst) - 1 - i] = temp

    # Go through each bin interval in the bin list, and count how many data points within the data list are in that bin
    # Create a new list, append the count for values in the bin, and start over
    countBin = []
    count = 0
    for i in range(0, len(binLst)):
        for j in data:
            if binLst[i] <= j < binLst[i + 1]:
                count = count + 1
        countBin.append(count)
        count = 0
    return countBin
