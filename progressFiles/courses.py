import time
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe" #using the version 97.0.4692.71
driver = webdriver.Chrome(PATH)

# targetSubject = input("Type in your Subject Code")
# targetCourses = input("Type in your courses that you want (example: CPSC 213, COMM 101, WRDS 150")

# test subject
driver.get("https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=CPSC&course=110")
time.sleep(2)
elements = driver.find_elements(By.CLASS_NAME, 'section1')

tempList = []

for e in elements:
    tempList.append(e.text)

print(tempList)
driver.close()