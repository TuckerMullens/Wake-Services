import pandas as pd

def makeAvailableClasses(fileName):
    df = pd.read_csv(fileName)
    return df

def makeHasTaken(fileName):
    df = pd.read_csv(fileName)
    return df

def makeRequiredCourses(fileName):
    df = pd.read_csv(fileName)
    return df

#PARAM: the already-instantiated availableClasses dataframe to get the correct columnn names
#RETURN: empty dataframe
def makeCurrentlyRegistered(availableClasses):
    df = pd.DataFrame(columns=availableClasses.columns)
    return df


availableClasses = makeAvailableClasses("csvFiles/Class Database - AvailableClasses.csv")
makeHasTaken("csvFiles/Class Database - HasTaken.csv")
makeRequiredCourses("csvFiles/Class Database - RequiredCourses.csv")
makeCurrentlyRegistered(availableClasses)
