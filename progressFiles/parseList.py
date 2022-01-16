testList = ['Full CPSC 110 101 Lecture 1 Online Tue Thu 11:00 12:30\n  Section Comments\nSee Section Comments', 
            'Full CPSC 110 102 Lecture 1 In-Person Tue Thu 14:00 15:30 Yes', 
            'Full CPSC 110 103 Lecture 1 In-Person Mon Wed Fri 15:00 16:00\n  Section Comments\nYes', 
            'Full CPSC 110 104 Lecture 1 In-Person Tue Thu 15:30 17:00\n  Section Comments\nYes', 
            'Blocked CPSC 110 1W1 Waiting List 1 Online Tue Thu 11:00 12:30\n  Section Comments\nSee Section Comments', 
            'Blocked CPSC 110 1W3 Waiting List 1 In-Person Mon Wed Fri 15:00 16:00', 
            'Full CPSC 110 201 Lecture 2 In-Person Tue Thu 12:30 14:00 Yes', 
            'Full CPSC 110 203 Lecture 2 In-Person Tue Thu 9:30 11:00 Yes', 
            'CPSC 110 2W1 Waiting List 2 In-Person Tue Thu 12:30 14:00 Yes', 
            'Restricted CPSC 110 V01 Lecture 2 In-Person Mon Wed Fri 11:00 12:00\n  Section Comments']

test = "Waiting"

throwAwayStr = ["Full", "Restricted", "Blocked", "Lecture", "Online", "In-Person", ""]

firstThrowAways = ["Full ", "Restricted ", "Blocked ", "STT "]

newList0 = []

newList = []

newList2 = []

newList3 = []

newList4 = []

result = []

term = 1

def findDates(course):
    result = []
    for x in course:
        if "Mon" in x:
            result.append("Mon")
        elif "Tue" in x:
            result.append("Tue")
        elif "Wed" in x:
            result.append("Wed")
        elif "Thu" in x:
            result.append("Thu")
        elif "Fri" in x:
            result.append("Fri")
    return result

def findStartTime(course):
    targetStr = course[6]
    if ":" in targetStr:
        targetStr = targetStr.replace(":", "")
    elif "\n" in targetStr:
        targetStr = targetStr.replace("\n", "")
    return int(targetStr)

def findEndTime(course):
    #7
    targetStr = course[7]
    if ":" in targetStr:
        targetStr = targetStr.replace(":", "")
    elif "\n" in targetStr:
        targetStr = targetStr.replace("\n", "")
    return int(targetStr)

#this function right here takes in a list of webelements? at the very beginning of this function

# This function parses the list and removes wait list courses
for str in testList:
    if not (test in str):
        newList.append(str)

# Removes the first word from the string
for str2 in newList:
    for throw in firstThrowAways:
        if throw in str2:
            str2 = str2.replace(throw, "")
            newList2.append(str2)

# Splits the string into lists
for str3 in newList2:
    item = str3.split(" ")
    newList3.append(item)

# Only gets the courses within the targeted term
for item in newList3:
    if term == int(item[4]):
        newList4.append(item)

# how the data structure looks like, [[Specific course #1], [Specific course #2], [Specific course #3]]
for course in newList4:
    courseName = course[0] + " " + course[1]
    sectionName = course[2]
    dates = findDates(course)
    for i in range(len(dates)):
        course.pop(0)
    startTime = findStartTime(course)
    endTime = findEndTime(course)

    courseResult = {
        "course": courseName,
        "section": sectionName,
        "days": dates,
        "start": startTime,
        "end": endTime
    }

    result.append(courseResult)


for x in result:
    print(x)
