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
#print(availableClasses)

def getFulfilledDivisionals():
    q1 = "select Division, sum(Hours) as totalHours from taken group by Division"
    #print(ps.sqldf(q1))
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
    #print(course)
    newSchedule = schedule.append(course)
    return newSchedule


def getCSCRequirementsLeft(df):
    """
    This function returns the CSC requirements left for a student to take when
    you input the dataframe of the classes the student has taken into the
    function.
    """
    csc_requirements = pd.read_csv("csvFiles/CSC BS Requirements/Class Database - CSCRequirements.csv")
    csc_electives = pd.read_csv("csvFiles/CSC BS Requirements/Class Database - CSCElectives.csv")
    mst_requirements = pd.read_csv("csvFiles/CSC BS Requirements/Class Database - MSTRequirements.csv")
    csc_requirements = csc_requirements.sort_values(
        by="Course",
        axis=0
    )
    csc_electives = csc_electives.sort_values(
        by="Course",
        axis=0
    )
    mst_requirements = mst_requirements.sort_values(
        by="Course",
        axis=0
    )

    csc_taken = df[df["Subject"] == "CSC"]
    csc300_count = 0

    for course_taken in csc_taken["Course"].to_numpy():
        if ((course_taken > 300) and (course_taken in csc_electives["Course"].to_numpy())):
            csc300_count += 1
            csc_electives = csc_electives.drop(
                index=csc_electives.loc[csc_electives["Course"] == course_taken].index
            )
        if (course_taken in csc_requirements["Course"].to_numpy()):
            csc_requirements = csc_requirements.drop(
                index=csc_requirements.loc[csc_requirements["Course"] == course_taken].index
            )

    mst_taken = df[df["Subject"] == "MST"]

    for course_taken in mst_taken["Course"].to_numpy():
        if (course_taken in mst_requirements["Course"].to_numpy()):
            mst_requirements = mst_requirements.drop(
                index=mst_requirements.loc[mst_requirements["Course"] == course_taken].index
            )
            if course_taken in [121, 205, 206]:
                for required_course in [121, 205, 206]:
                    if required_course != course_taken:
                        mst_requirements = mst_requirements.drop(
                            index=mst_requirements.loc[mst_requirements["Course"] == required_course].index
                        )

    csc_requirements = pd.concat([csc_requirements, csc_electives], axis=0)
    csc_requirements = pd.concat([csc_requirements, mst_requirements], axis=0)
    csc_requirements = csc_requirements.sort_values(
        by="Course",
        axis=0
    )

    return csc_requirements


#instantiates dataframes from excel file
availableClasses = makeAvailableClasses("csvFiles/Class Database - AvailableClasses.csv")
taken = makeHasTaken("csvFiles/Class Database - HasTaken.csv")
required = makeRequiredCourses("csvFiles/Class Database - RequiredCourses.csv")

#just to put identical columns
currentSchedule = makeCurrentlyRegistered(availableClasses)
#print(availableClasses)


missingDivisionals = getMissingDivisionals()
#print(missingDivisionals)

currentSchedule = registerCourse('Introduction ',availableClasses,currentSchedule)
#print(currentSchedule)

toFulfill3 = getClassesThatFulfill(missingDivisionals[0],availableClasses)
#print(toFulfill3)

toFulfillAll = getClassesThatFulfill(missingDivisionals,availableClasses)
#print(toFulfillAll)

getCSCRequirementsLeft(taken)
