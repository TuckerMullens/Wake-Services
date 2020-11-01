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
            missing.append(str(i))
    if not('CSC' in listFulfilled):
        missing.append('CSC')
    if not('LANG' in listFulfilled):
        missing.append('LANG')
    if not('HES' in listFulfilled):
        missing.append('HES')
    return missing


def getClassesThatFulfill(division, available):
    if isinstance(division, str):
        fulfillments = available.loc[available['Division'] == division]
        return fulfillments
    elif isinstance(division,list):
        allFulfillments = pd.DataFrame()
        for i in range(len(division)):
            allFulfillments = allFulfillments.append(available.loc[available['Division'] == division[i]])

        return allFulfillments



def registerCourse(courseName, available, schedule):
    course = available.loc[available['Title'] == courseName]
    print(course)
    newSchedule = schedule.append(course)
    return newSchedule


#instantiates dataframes from excel file
availableClasses = makeAvailableClasses("csvFiles/Class Database - AvailableClasses.csv")
taken = makeHasTaken("csvFiles/Class Database - HasTaken.csv")
required = makeRequiredCourses("csvFiles/Class Database - RequiredCourses.csv")

#just to put identical columns
currentSchedule = makeCurrentlyRegistered(availableClasses)
print(availableClasses)


missingDivisionals = getMissingDivisionals()
print(missingDivisionals)

currentSchedule = registerCourse('Introduction ',availableClasses,currentSchedule)
print(currentSchedule)

toFulfill3 = getClassesThatFulfill(missingDivisionals[0],availableClasses)
print(toFulfill3)

toFulfillAll = getClassesThatFulfill(missingDivisionals,availableClasses)
print(toFulfillAll)


