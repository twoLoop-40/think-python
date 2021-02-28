class Time:
    '''
    attr : hour, minute, second
    '''



def time_to_int(time):
    minutes = time.hour*60 + time.minutes
    seconds = minutes*60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour , time.minute = divmod(minutes, 60)
    return time

def mul_time(t, r):
    seconds = time_to_int(t) * r
    return int_to_time(seconds)

def avg_pace(ftime, distance):
    return mul_time(ftime, 1/distance)
