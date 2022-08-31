def dayOfWeek(days):      
    if days == 1:
        return '(next day)'
    elif days > 1:
        return f'({days} days later)'
    return ""

def add_time(start, duration,weekday=False):
    t = start.split()
    time = t[0]
    ampm = t[1]
    hr = 0
    min = 0 
    week = [ 'monday', 'tuesday',
        'wednesday', 'thursday',
        'friday', 'saturday',
        'sunday']
    # Separating hours and minutes from start
    if len(time) == 5 and time[2] == ':':
        hr = int(time[0]+time[1])
        min = int(time[3]+time[4])
    if len(time) == 4 and time[1] == ':':
        hr = int(time[0])
        min = int(time[2]+time[3])
    # Separating hours and minutes from duration
    sumHr = 0
    sumMin = 0
    if len(duration) == 6 and duration[3] == ':':
        sumHr = int(duration[0]+duration[1]+duration[2]) 
        sumMin = int(duration[4]+duration[5])
    if len(duration) == 5 and duration[2] == ':':
        sumHr = int(duration[0]+duration[1]) 
        sumMin = int(duration[3]+duration[4])
    if len(duration) == 4 and duration[1] == ':':
        sumHr = int(duration[0])
        sumMin = int(duration[2]+duration[3])

    hour = hr + sumHr
    minute = min + sumMin
    days = 0
    # Min to Hr
    while True:
        if minute >= 60:
            minute -= 60
            hour += 1
        else:
            break
    # AM to PM
    while True:
        if hour > 12:
            hour -= 12
            if ampm == 'AM':
                ampm = 'PM'
            elif ampm == 'PM':
                ampm = 'AM'
                days +=1
        else:
            break
    
    if hour == 12 and ampm == 'PM':
        days += 1
        ampm = 'AM'
    if hour == 12 and ampm == 'AM':
        ampm = 'PM'
    if sumHr >= 24 and hour == 12 and ampm == 'PM':
        ampm = 'AM'
    
    new_time = f'{hour}:{minute:02} {ampm.upper()}'
    
    if weekday: # add day of the week
        weekdays = weekday.strip().lower()
        selected_day = int((week.index(weekdays) + days) % 7)
        today = week[selected_day]
        if days == 0:
            new_time += f', {today.title()}'
        else:
            new_time += f', {today.title()} {dayOfWeek(days)}'

    elif days >= 1:
        new_time = " ".join((new_time, dayOfWeek(days)))
        
    return new_time