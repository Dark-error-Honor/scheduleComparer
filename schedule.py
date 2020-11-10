
def MeetingFinder(schedule_1, schedule_2, minTime):
    convertedSchedule_1 = timeToMinutes(schedule_1)
    convertedSchedule_2 = timeToMinutes(schedule_2)

    mergedSchedules = mergeSchedules(convertedSchedule_1, convertedSchedule_2)
    print(mergedSchedules)
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
    print(f'schedule1: {schedule_1} | schedule2: {schedule_2}')
    pointer1 = 0
    pointer2 = 0
    mergedSchedule = []
    while pointer1 < len(schedule_1) and pointer2 < len(schedule_2):
        begin1 = schedule_1[pointer1][0]
        end1 = schedule_1[pointer1][1]
        begin2 = schedule_2[pointer2][0]
        end2 = schedule_2[pointer2][1]

        if begin1 <= begin2:
            if end1 >= begin2 and end1 >= end2:
                print(f'{begin1} is smaller then {begin2}')
                mergedSchedule.append([begin1, end1])

            elif begin2 >= begin1 and end2 >= end1:
                print(
                    f'{begin1} is smaller then {begin2} || {end2} is bigger then {end1}')
                mergedSchedule.append([begin1, end2])

            else:
                print(f'none of the top if statement')
                mergedSchedule.append(schedule_1[pointer1])
                mergedSchedule.append(schedule_2[pointer2])
        elif begin1 >= begin2:
            print(f'begin | {begin1} is bigger then {begin2}')
            if end1 >= end2:
                print(f'end | {end1} is bigger then {end2}')
                mergedSchedule.append([begin2, end1])

        pointer1 += 1
        pointer2 += 1

    return mergedSchedule


def calcFreeSpaces(mergedSchedule, minTime):
    count = 0
    freeSpaces = []
    while count <= len(mergedSchedule) - 2:
        end1 = mergedSchedule[count][1]
        begin2 = mergedSchedule[count + 1][0]
        minutes = begin2 - end1
        print(minutes)
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


schedule_1 = [['8:00', '9:30'], ['10:30', '11:30'],
              ['13:00', '13:30'], ['15:00', '15:30']]
schedule_2 = [['8:00', '9:00'], ['10:00', '11:30'],
              ['13:00', '14:00'], ['18:00', '20:30']]

spaces = MeetingFinder(schedule_1, schedule_2, 30)
print(spaces)
