import itertools
from course_info import getCourseInfo

# print(int((int(1130 / 100) - 8) * 2 + ((1130 % 100) / 30)))

# print(has_overlap(({'name': 'comm 204', 'section': '101', 'days': ['Mon', 'Wed'], 'start': 1430, 'end': 1600}, {'name': 'comm 205', 'section': '101', 'days': ['Mon', 'Wed', 'Fri'], 'start': 1430, 'end': 1530}, {'name': 'cpsc 221', 'section': '101', 'days': ['Mon', 'Wed', 'Fri'], 'start': 1200, 'end': 1300}, {'name': 'cpsc 213', 'section': '101', 'days': ['Tue', 'Thu'], 'start': 1500, 'end': 1600}, {'name': 'comm 101', 'section': '101', 'days': ['Mon', 'Wed', 'Fri'], 'start': 900, 'end': 1000})))

courses_ex = [
    [
        {
            "course":"comm 204",
            "section":"101",
            "days":"MW",
            "start":1430,
            "end":1600
        },
        {
            "course":"comm 204",
            "section":"102",
            "days":"MW",
            "start":1600,
            "end":1730
        }
    ],
    [
        {
            "course":"comm 205",
            "section":"101",
            "days":"MWF",
            "start":1000,
            "end":1100
        },
        {
            "course":"comm 205",
            "section":"102",
            "days":"MWF",
            "start":1400,
            "end":1500
        },
        {
            "course":"comm 205",
            "section":"103",
            "days":"TuTh",
            "start":1200,
            "end":1330
        }
    ],
    [
        {
            "course":"cpsc 221",
            "section":"101",
            "days":"MWF",
            "start":1200,
            "end":1300
        },
        {
            "course":"cpsc 221",
            "section":"102",
            "days":"MWF",
            "start":930,
            "end":1030
        },
    ],
    [
        {
            "course":"cpsc 213",
            "section":"101",
            "days":"TuTh",
            "start":1500,
            "end":1630
        },
        {
            "course":"cpsc 213",
            "section":"102",
            "days":"MW",
            "start":1630,
            "end":1800
        }
    ],
    [
        {
            "course":"comm 101",
            "section":"101",
            "days":"MWF",
            "start":1400,
            "end":1500
        },
        {
            "course":"comm 101",
            "section":"102",
            "days":"MWF",
            "start":1600,
            "end":1700
        },
        {
            "course":"comm 101",
            "section":"103",
            "days":"MWF",
            "start":1130,
            "end":1230
        },
        {
            "course":"comm 101",
            "section":"104",
            "days":"TuTh",
            "start":1200,
            "end":1330
        }
    ]
]

courses_ex_1 = {
    "comm 204":[
        {
            "section":"101",
            "days":"MW",
            "start":1430,
            "end":1600
        },
        {
            "section":"102",
            "days":"MW",
            "start":1600,
            "end":1730
        }
    ],
    "comm 205":[
        {
            "section":"101",
            "days":"MWF",
            "start":1000,
            "end":1100
        },
        {
            "section":"102",
            "days":"MWF",
            "start":1400,
            "end":1500
        },
        {
            "section":"103",
            "days":"TT",
            "start":1200,
            "end":1330
        }
    ],
    "cpsc 221":[
        {
            "section":"101",
            "days":"MWF",
            "start":1200,
            "end":1300
        },
        {
            "section":"102",
            "days":"MWF",
            "start":930,
            "end":1030
        },
    ],
    "cpsc 213":[
        {
            "section":"101",
            "days":"TT",
            "start":1500,
            "end":1630
        },
        {
            "section":"102",
            "days":"MW",
            "start":1630,
            "end":1800
        }
    ],
    "comm 101":[
        {
            "section":"101",
            "days":"MWF",
            "start":1400,
            "end":1500
        },
        {
            "section":"102",
            "days":"MWF",
            "start":1600,
            "end":1700
        },
        {
            "section":"103",
            "days":"MWF",
            "start":1130,
            "end":1230
        },
        {
            "section":"104",
            "days":"TT",
            "start":1200,
            "end":1330
        }
    ]
}

##############################

courses_ex1 = {
    "comm 204":[
        {
            "section":"101",
            "days":"MW",
            "start":1430,
            "end":1600
        },
        {
            "section":"102",
            "days":"MW",
            "start":1600,
            "end":1730
        }
    ],
    "comm 205":[
        {
            "section":"101",
            "days":"MWF",
            "start":1000,
            "end":1100
        },
        {
            "section":"102",
            "days":"MWF",
            "start":1400,
            "end":1500
        },
        {
            "section":"103",
            "days":"TT",
            "start":1200,
            "end":1330
        }
    ]
}

# start_target = 1200
# end_target = 1700

# def dfs(courses, schedule, schedule_sofar = []):
    

# def get_all_schedules(courses): 
#     schedule = []
        
#     dfs(courses, schedule)

#     return schedule

##################################

courses_ex2 = [
    [
        {
            "name": "comm 204",
            "section":"101",
            "days":"MW",
            "start":1430,
            "end":1600
        },
        {
            "name": "comm 204",
            "section":"102",
            "days":"MW",
            "start":1600,
            "end":1730
        }
    ],
    [
        {
            "name": "comm 205",
            "section":"101",
            "days":"MWF",
            "start":1000,
            "end":1100
        },
        {
            "name": "comm 205",
            "section":"102",
            "days":"MWF",
            "start":1400,
            "end":1500
        },
        {
            "name": "comm 205",
            "section":"103",
            "days":"TuTh",
            "start":1200,
            "end":1330
        }
    ]
]

def does_interfere(time, times): # (time = (start, end), times = [time1, time2, time3])
    start = time[0]
    end = time[1]
    for t in times:
        # t[0] is next start time
        # t[1] is next end time
        #       end inside                                          all inside                          start inside                                all outside (bigger)
        if (start <= t[0] and end < t[1] and end > t[0]) or (start >= t[0] and end <= t[1]) or (start < t[1] and start > t[0] and end >= t[1]) or (start < t[0] and end > t[1]):
            return True
    return False

def has_overlap(courses):
    times = {
        "M":[],
        "Tu":[],
        "W":[],
        "Th":[],
        "F":[]
    }
    for course in courses:
        # for section in course:
            # print(section)
        time = (course['start'], course['end'])
        days = course['days']
        i = 0
        while i < len(days):
            if days[i] in "MWF":
                day = days[i]
                i += 1
            else:
                day = days[i:i+2]
                i += 2
            if does_interfere(time, times[day]):
                return True
            times[day].append(time)
    return False
    

def get_possible_schedules(courses):
    combos = itertools.product(*courses)
    possible_schedules = []
    for combo in combos:
        if not has_overlap(combo):
            possible_schedules.append(combo)
    
    i = 1
    for schedule in possible_schedules:
        for sections in schedule:
            print(sections)
        print(str(i) + "----------------")
        i += 1

get_possible_schedules(courses_ex)


def generate_schedule(courses):
    # will generate a tuple of all combinations
    new_list = itertools.product(*courses)
    for elt in new_list:
        for i in elt:
            print(i)
        print("----------------------------")