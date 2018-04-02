import pandas
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    # read the data as a Pandas dataframe called 'baseball'
    baseball = pandas.read_csv(filename)
    
    # calculate the average weight using numpy.mean() in the 'weight' column of 'baseball'
    avg_weight = numpy.mean(baseball['weight'])
    
    # replace any NAs in the 'weight' column with the average weight
    baseball['weight'] = baseball['weight'].fillna(avg_weight)
    
    return baseball
