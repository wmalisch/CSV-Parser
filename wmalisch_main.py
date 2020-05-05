##
# A program for parsing CSV files.
# Student Name: Will Malisch
# Student ID: wmalisch
# Student Number: 250846447

## Define mmain function
# @param/return no paramter or return, just run the instructions inside the function
def main():
    # Import all the functions created in the myStatistics.py file
    from myStatistics import myCountBins
    from myStatistics import myMin
    from myStatistics import myMedian
    from myStatistics import myMax
    from myStatistics import myAverage
    from myStatistics import myStandardDeviation
    # Prompt user for input file name
    fileName = input("Enter the name of the text file, including the .txt: ")

    # Use the try/excpet to make sure that the file name entered is correct. If the program cannot find the file locally, the program is terminated
    try:
        # Open the input file and output file for reading and writing
        infile = open(fileName, "r")
        outfile1 = open("trial1-data-analysis.txt", "w")
        outfile2 = open("trial2-data-analysis.txt", "w")
        outfile3 = open("trial3-data-analysis.txt", "w")
        outfile4 = open("trial4-data-analysis.txt", "w")

        # Set up the lists that will contain all the float values, once extracted from the csv file
        trial1 = []
        trial2 = []
        trial3 = []
        trial4 = []
        missingTrials = []

        # Process the lines by first stripping the "\n" values off the ends
        # Then splitting the trial and record values to separate lines
        # Use a missing trials just in our partner left any unusual data points
        for line in infile:
            line = line.rstrip()
            temp = line.split()
            temp[1] = float(temp[1])
            if temp[0] == "trial1":
                trial1.append(temp[1])
            elif temp[0] == "trial2":
                trial2.append(temp[1])
            elif temp[0] == "trial3":
                trial3.append(temp[1])
            elif temp[0] == "trial4":
                trial4.append(temp[1])
            else:
                missingTrials.append(temp[0])

        # Create a trial dictionary using trials/trial number as the key
        trials = {"trial1": trial1, "trial2": trial2, "trial3": trial3, "trial4": trial4}

        # Run all the statistical analysis on trial1, by calling the functions created to the list in the trial dictionary
        trial1Min = round(myMin(trials["trial1"]), 5)
        trial1Max = round(myMax(trials["trial1"]), 5)
        trial1Average = round(myAverage(trials["trial1"]), 5)
        trial1Median = round(myMedian(trials["trial1"]), 5)
        trial1Stdev = round(myStandardDeviation(trials["trial1"]), 5)
        trial1Bins = myCountBins(trials["trial1"], 25)

        # Run all the statistical analysis on trial2, by calling the functions created to the list in the trial dictionary
        trial2Min = round(myMin(trials["trial2"]), 5)
        trial2Max = round(myMax(trials["trial2"]), 5)
        trial2Average = round(myAverage(trials["trial2"]), 5)
        trial2Median = round(myMedian(trials["trial2"]), 5)
        trial2Stdev = round(myStandardDeviation(trials["trial2"]), 5)
        trial2Bins = myCountBins(trials["trial2"], 25)

        # Run all the statistical analysis on trial3, by calling the functions created to the list in the trial dictionary
        trial3Min = round(myMin(trials["trial3"]), 5)
        trial3Max = round(myMax(trials["trial3"]), 5)
        trial3Average = round(myAverage(trials["trial3"]), 5)
        trial3Median = round(myMedian(trials["trial3"]), 5)
        trial3Stdev = round(myStandardDeviation(trials["trial3"]), 5)
        trial3Bins = myCountBins(trials["trial3"], 25)

        # Run all the statistical analysis on trial4, by calling the functions created to the list in the trial dictionary
        trial4Min = round(myMin(trials["trial4"]), 5)
        trial4Max = round(myMax(trials["trial4"]), 5)
        trial4Average = round(myAverage(trials["trial4"]), 5)
        trial4Median = round(myMedian(trials["trial4"]), 5)
        trial4Stdev = round(myStandardDeviation(trials["trial4"]), 5)
        trial4Bins = myCountBins(trials["trial4"], 25)

        # Establish strings for the output, so it is quicker when writing contents to the output files
        min = "minimum  :"
        max = "maximum  :"
        avg = "average  :"
        median = "median   :"
        stddev = "std_dev  :"
        bin_count = "bin_count:"

        # Write the statistical analysis to the respective files for each trial, to 5 decimal places
        outfile1.write("%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %s" % (min, trial1Min, max, trial1Max, avg, trial1Average, median, trial1Median, stddev, trial1Stdev, bin_count,trial1Bins))
        outfile2.write("%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %s" % (min, trial2Min, max, trial2Max, avg, trial2Average, median, trial2Median, stddev, trial2Stdev, bin_count,trial2Bins))
        outfile3.write("%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %s" % (min, trial3Min, max, trial3Max, avg, trial3Average, median, trial3Median, stddev, trial3Stdev, bin_count,trial3Bins))
        outfile4.write("%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %.5f\n%s %s" % (min, trial4Min, max, trial4Max, avg, trial4Average, median, trial4Median, stddev, trial4Stdev, bin_count,trial4Bins))

        # Close all the input and output files
        infile.close()
        outfile1.close()
        outfile2.close()
        outfile3.close()
        outfile4.close()

    # Terminate the program if file name is entered incorrectly
    except IOError:
        print("Sorry, the file %s is not available" % fileName)

# Run the program
main()

