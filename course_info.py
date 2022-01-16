import time
from numpy import number
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setting up PATH for webdriver for selenium to use
PATH = ".\chromedriver.exe" # version 97.0.4692.71
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, service_log_path='ignore.txt', options=options)


# Global Variables and Constants
courseListTargets = []
WAIT = "Waiting"
THROWAWAYSTRS = ["Full ", "Restricted ", "Blocked ", "STT "]


# INPUT
final = []


targetTerm = input("Type in the desired school Term (1 or 2): ")
try:
    targetTerm = int(targetTerm)
except:
    print("An exception occurred: Type a valid number please")

targetCourses = input("Type in your courses that you want in this specific format \n (example: CPSC 213, COMM 101, WRDS 150): ")
targetCourses = targetCourses.split(", ")

# Parsing the input string into list of target courses
def getTargetCourses():
    for x in targetCourses: 
        course = x.split(" ")
        temp_item = {
            "Course": course[0],
            "Identifier": course[1]
        }
        courseListTargets.append(temp_item)

# Helper Functions
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
    targetStr = course[7]
    if ":" in targetStr:
        targetStr = targetStr.replace(":", "")
    elif "\n" in targetStr:
        targetStr = targetStr.replace("\n", "")
    return int(targetStr)

# plan: get first thing in the list, targetted course and identitfier -> web element then parse that text into list dictionary

def parseWebElements(elements):
    result = []
    for e in elements:
        result.append(e.text)
    
    return result

def parseText(tempList):
    noWaitList = []
    noFirstWordList = []
    strToList = []
    courseWithTargetTerm = []

    result = []

    # Removes wait list courses
    for str in tempList:
        if not (WAIT in str):
            noWaitList.append(str)


    # Removes the first word from the string from the word bank THROWAWAYSTRS
    temp_i = 0
    for str2 in noWaitList:
        for throw in THROWAWAYSTRS:
            if throw in str2:
                str2 = str2.replace(throw, "")
                noFirstWordList.append(str2)
                temp_i += 1
        if temp_i == 1:
            temp_i -= 1
        else:
            noFirstWordList.append(str2)

    # Splits the string into lists
    for str3 in noFirstWordList:
        item = str3.split(" ")
        strToList.append(item)
    

    # Only gets the courses within the targeted term
    for item in strToList:
        if targetTerm == int(item[4]):
            courseWithTargetTerm.append(item)

    # Parses the courses into the required dictionary format
    for course in courseWithTargetTerm:
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
    final.append(result)

def getFinalDictList():
    for targetCourse in courseListTargets:
        driver.get("https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=" 
                    + targetCourse["Course"] + "&" + "course=" + targetCourse["Identifier"])

        elements = driver.find_elements(By.CLASS_NAME, 'section1')
        tempList = parseWebElements(elements)
        parseText(tempList)

def print_course_info(info):
    print("### FOUND COURSE INFO ONLINE ###")
    for schedule in info:
        for course in schedule:
            print(course['course'].upper() + " " + course['section'], end = ", ")
            for day in course['days']:
                print(day, end = ", ")
            print("Start: " + str(course['start'])[:-2] + ":" + str(course['start'])[-2:] + ", End: " + str(course['end'])[:-2] + ":" + str(course['end'])[-2:])
        print()

def getCourseInfo():
    getTargetCourses()
    getFinalDictList()
    print_course_info(final)
    driver.close()
    return final