from numpy import number
import os

# not sure if this is needed
numberCourses = input("How many courses are you looking for: ")


targetCourses = input("Type in your courses that you want in this specific format \n (example: CPSC 213, COMM 101, WRDS 150): ")

#need to check for edge cases

try: 
    numberCourses = int(numberCourses)
except:
    print("You did not enter a number for how many courses you are looking for")

try:
    listCourses = targetCourses.split(", ")
except:
    print("An exception occurred")


#parsing the list into a list of dictionaries
listDict = []

for x in listCourses: 
    course = x.split(" ")
    temp_item = {
        "Course": course[0],
        "Identifier": course[1]
    }
    listDict.append(temp_item)

print(listDict)