
def MeetingFinder(schedule_1, schedule_2, minTime):
    convertedSchedule_1 = timeToMinutes(schedule_1)
    convertedSchedule_2 = timeToMinutes(schedule_2)

    mergedSchedules = mergeSchedules(convertedSchedule_1, convertedSchedule_2)
    freeSpace = calcFreeSpaces(mergedSchedules, minTime)

    return freeSpace


def timeToMinutes(schedule):
    newSchedule = []
    for i in range(0, len(schedule)):
        single_meeting = []
        for j in range(0, 2):
            time = schedule[i][j]
            hours, minutes = time.split(':')
            hours, minutes = int(hours), int(minutes)
            hours *= 60  # convert hours to minutes
            result = hours + minutes
            single_meeting.append(result)

        newSchedule.append(single_meeting)
    return(newSchedule)


def mergeSchedules(schedule_1, schedule_2):
    schedule = schedule_1 + schedule_2
    schedule.sort(key=lambda x: x[0])
    mergedStack = []
    start = -10000
    end = -100000
    for i in range(len(schedule)):
        item = schedule[i]
        if item[0] > end:
            if i != 0:
                mergedStack.append([start, end])
            end = item[1]
            start = item[0]
        else:
            if item[1] >= end:
                end = item[1]

    if end != -100000 and [start, end] not in mergedStack:
        mergedStack.append([start, end])

    return mergedStack


def calcFreeSpaces(mergedSchedule, minTime):
    count = 0
    freeSpaces = []
    while count <= len(mergedSchedule) - 2:
        end1 = mergedSchedule[count][1]
        begin2 = mergedSchedule[count + 1][0]
        minutes = begin2 - end1
        if minutes >= minTime:
            freeSpaces.append({
                'from': convertMinutesToTime(end1),
                'to': convertMinutesToTime(begin2),
                'time': minutes
            })

        count += 1
    return freeSpaces


def convertMinutesToTime(minutes):

    return '%d:%02d' % (divmod(minutes, 60))


schedule_1 = [['7:00', '8:00'], ['10:00', '12:00'],
              ['13:30', '14:30'], ['18:00', '20:00']]
schedule_2 = [['10:00', '12:00'], ['13:00', '14:00'], ['16:00', '17:00']]

spaces = MeetingFinder(schedule_1, schedule_2, 30)
print(spaces)
