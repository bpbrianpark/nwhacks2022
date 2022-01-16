from course_info import getCourseInfo
import itertools

# courses_ex = [
#     [
#         {
#             "name": "comm 204",
#             "section":"101",
#             "days":['Mon', 'Wed'],
#             "start":1430,
#             "end":1600
#         },
#         {
#             "name": "comm 204",
#             "section":"102",
#             "days":['Mon', 'Wed'],
#             "start":1600,
#             "end":1730
#         }
#     ],
#     [
#         {
#             "name": "comm 205",
#             "section":"101",
#             "days":['Mon', 'Wed', 'Fri'],
#             "start":1000,
#             "end":1100
#         },
#         {
#             "name": "comm 205",
#             "section":"102",
#             "days":['Mon', 'Wed', 'Fri'],
#             "start":1400,
#             "end":1500
#         },
#         {
#             "name": "comm 205",
#             "section":"103",
#             "days":['Tue', 'Thu'],
#             "start":1200,
#             "end":1330
#         }
#     ],
#     [
#         {
#             "name": "cpsc 221",
#             "section":"101",
#             "days":['Mon', 'Wed', 'Fri'],
#             "start":1200,
#             "end":1300
#         },
#         {
#             "name": "cpsc 221",
#             "section":"102",
#             "days":['Mon', 'Wed', 'Fri'],
#             "start":930,
#             "end":1030
#         },
#     ],
#     [
#         {
#             "name": "cpsc 213",
#             "section":"101",
#             "days":['Tue', 'Thu'],
#             "start":1500,
#             "end":1630
#         },
#         {
#             "name": "cpsc 213",
#             "section":"102",
#             "days":['Mon', 'Wed'],
#             "start":1630,
#             "end":1800
#         }
#     ],
#     [
#         {
#             "name": "comm 101",
#             "section":"101",
#             "days":['Mon', 'Wed', 'Fri'],
#             "start":1400,
#             "end":1500
#         },
#         {
#             "name": "comm 101",
#             "section":"102",
#             "days":['Mon', 'Wed', 'Fri'],
#             "start":1600,
#             "end":1700
#         },
#         {
#             "name": "comm 101",
#             "section":"103",
#             "days":['Mon', 'Wed', 'Fri'],
#             "start":1130,
#             "end":1230
#         },
#         {
#             "name": "comm 101",
#             "section":"104",
#             "days":['Tue', 'Thu'],
#             "start":1200,
#             "end":1330
#         }
#     ]
# ]

courses_ex = [
    [
        {
            "course":"comm 204",
            "section":"101",
            "days":["Mon","Wed"],
            "start":1430,
            "end":1600
        },
        {
            "course":"comm 204",
            "section":"102",
            "days":["Mon","Wed"],
            "start":1600,
            "end":1730
        }
    ],
    [
        {
            "course":"comm 205",
            "section":"101",
            "days":["Mon","Wed","Fri"],
            "start":1000,
            "end":1100
        },
        {
            "course":"comm 205",
            "section":"102",
            "days":["Mon","Wed","Fri"],
            "start":1400,
            "end":1500
        },
        {
            "course":"comm 205",
            "section":"103",
            "days":["Tue","Thu"],
            "start":1200,
            "end":1330
        }
    ],
    [
        {
            "course":"cpsc 221",
            "section":"101",
            "days":["Mon","Wed","Fri"],
            "start":1200,
            "end":1300
        },
        {
            "course":"cpsc 221",
            "section":"102",
            "days":["Mon","Wed","Fri"],
            "start":930,
            "end":1030
        },
    ],
    [
        {
            "course":"cpsc 213",
            "section":"101",
            "days":["Tue","Thu"],
            "start":1500,
            "end":1630
        },
        {
            "course":"cpsc 213",
            "section":"102",
            "days":["Mon","Wed"],
            "start":1630,
            "end":1800
        }
    ],
    [
        {
            "course":"comm 101",
            "section":"101",
            "days":["Mon","Wed","Fri"],
            "start":1400,
            "end":1500
        },
        {
            "course":"comm 101",
            "section":"102",
            "days":["Mon","Wed","Fri"],
            "start":1600,
            "end":1700
        },
        {
            "course":"comm 101",
            "section":"103",
            "days":["Mon","Wed","Fri"],
            "start":1130,
            "end":1230
        },
        {
            "course":"comm 101",
            "section":"104",
            "days":["Tue","Thu"],
            "start":1200,
            "end":1330
        }
    ]
]

def has_overlap(combo):
    times_mon = [False] * 26
    times_tue = [False] * 26
    times_wed = [False] * 26
    times_thu = [False] * 26
    times_fri = [False] * 26

    for course in combo:
        for day in course['days']:
            start_index = int(((int(course["start"] / 100)) - 8) * 2 + (course["start"] % 100) / 30)
            end_index = int(((int(course["end"] / 100)) - 8) * 2 + (course["end"] % 100) / 30)
            for i in range(start_index, end_index):
                if day == "Mon":
                    if times_mon[i]:
                        return True
                    times_mon[i] = True
                elif day == "Tue":
                    if times_tue[i]:
                        return True
                    times_tue[i] = True
                elif day == "Wed":
                    if times_wed[i]:
                        return True
                    times_wed[i] = True
                elif day == "Thu":
                    if times_thu[i]:
                        return True
                    times_thu[i] = True
                elif day == "Fri":
                    if times_fri[i]:
                        return True
                    times_fri[i] = True
    return False

def get_possible_schedules(courses):
    combos = itertools.product(*courses)
    possible_schedules = []
    for combo in combos:
        if not has_overlap(combo):
            schedule = []
            for course in combo:
                schedule.append(course)
            possible_schedules.append(schedule)
    return possible_schedules

def print_schedule(schedule):
    for course in schedule:
        print(course['course'].upper() + " " + course['section'], end = ", ")
        for day in course['days']:
            print(day, end = ", ")
        print("Start: " + str(course['start'])[:-2] + ":" + str(course['start'])[-2:] + ", End: " + str(course['end'])[:-2] + ":" + str(course['end'])[-2:])
    print()

def print_schedule_with_scores(schedule):
    for i in range(len(schedule)-1):
        print(schedule[i]['course'].upper() + " " + schedule[i]['section'], end = ", ")
        for day in schedule[i]['days']:
            print(day, end = ", ")
        print("Start: " + str(schedule[i]['start'])[:-2] + ":" + str(schedule[i]['start'])[-2:] + ", End: " + str(schedule[i]['end'])[:-2] + ":" + str(schedule[i]['end'])[-2:])
    print("Score - " + str(schedule[-1]))
    print()

def score_schedules(schedules, target_start, target_end):
    def get_schedule_score(schedule):
        score = 0
        for course in schedule:
            # if target_start > course['start'] : score += target_start - course['start'] 
            # if target_end < course['end'] : score += course['end'] - target_end
            if target_start > course['start']:
                if (target_start - course['start']) % 100 == 30:
                    score += target_start - course['start'] + 20
                elif (target_start - course['start']) % 100 == 70:
                    score += target_start - course['start'] - 20
                else:
                    score += target_start - course['start'] 
            if target_end < course['end']:
                if (course['end'] - target_end % 100) == 30:
                    score += course['end'] - target_end + 20
                elif (course['end'] - target_end % 100) == 70:
                    score += course['end'] - target_end - 20
                else:
                    score += course['end'] - target_end
        return score

    for schedule in schedules:
        schedule.append(get_schedule_score(schedule))
    schedules.sort(key=lambda x:x[-1])
    return schedules

def get_nth_schedule(n, course_info, target_start, target_end):
    return score_schedules(get_possible_schedules(course_info),target_start,target_end)[n-1]

def get_scored_schedules(course_info, target_start, target_end):
    return score_schedules(get_possible_schedules(course_info),target_start,target_end)

### MAIN CODE ###

print("\n### GETTING YOUR COURSE INFO ###")
course_info = getCourseInfo()
print("### COLLECTING INPUTS ###")
start_target_input = input("What is your preferred start time? (Format - HH:MM. Ex: 1pm = 13:00)\nStart time = ")
end_target_input = input("What is your preferred end time? (Format - HH:MM. Ex: 1pm = 13:00)\nEnd time = ")
start_target = int(start_target_input[0:2])*100 + int(start_target_input[3:len(start_target_input)])
end_target = int(end_target_input[0:2])*100 + int(end_target_input[3:len(end_target_input)])
print("\n### CALCULATING POSSIBLE SCHEDULES AND SCORING THEM ###")
scored_schedules = get_scored_schedules(course_info,start_target,end_target)
for i in range(min(5, len(scored_schedules))):
    print_schedule_with_scores(scored_schedules[i])
print("... hiding rest\n")
print("### RESULTS ### (Lower score is better)")
print("Your BEST schedule within the specified timeframe of " + start_target_input + " to " + end_target_input + ":")
print_schedule_with_scores(get_nth_schedule(1, course_info, start_target, end_target))
print("Alternate schedules:")
for i in range(1, min(4, len(scored_schedules))):
    print(str(i) + ".")
    print_schedule_with_scores(get_nth_schedule(i+1, course_info, start_target, end_target))