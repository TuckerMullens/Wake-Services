import pandas as pd
import pandasql as ps


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
taken = makeHasTaken("csvFiles/Class Database - HasTaken.csv")
required = makeRequiredCourses("csvFiles/Class Database - RequiredCourses.csv")
currentSchedule = makeCurrentlyRegistered(availableClasses)
print(availableClasses)

def getFulfilledDivisionals():
    q1 = "select Division, sum(Hours) as totalHours from taken group by Division"
    print(ps.sqldf(q1))
    return ps.sqldf(q1)

def getMissingDivisionals():
    df = getFulfilledDivisionals()
    listFulfilled = list(df['Division'])
    missing = []
    for i in range(1,6):
        if not (str(i) in listFulfilled):
            missing.append(i)
    if not('CSC' in listFulfilled):
        missing.append('CSC')
    if not('LANG' in listFulfilled):
        missing.append('LANG')
    if not('HES' in listFulfilled):
        missing.append('HES')
    return missing

missingDivisionals = getMissingDivisionals()
print(missingDivisionals)