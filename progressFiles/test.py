course = ['CPSC', '110', '101', 'Lecture', '1', 'Online', 'Tue', 'Thu', '11:00', '12:30\n', '', 'Section', 'Comments\nSee', 'Section', 'Comments']

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

print(findDates(course))