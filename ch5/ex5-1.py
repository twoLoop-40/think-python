import time
one_minute = 60
one_hour = 60 * one_minute
one_day = 24*one_hour
normal_year = one_day * 365
full_year = one_day * 366

start_year = 1970

def find_year(time):
    return int(start_year + time//normal_year)

def find_full_year(time):
    year_now = find_year(time) 
    
    count = 0
    for year in range(start_year, year_now):
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            count = count + 1
    
    return count

def find_hour(time):
    return int(time // one_hour + 9) % 24 

def find_min(time):
    return int(time // one_minute) % 60

def find_sec(time):
    return int(time % one_minute)

def daysForThisYear(time):
        totalDays = time // one_day
        daysLeft = totalDays - (find_year(time) - start_year) * 365 - find_full_year(time)
        return int(daysLeft)

def month_for_now(time):
    def isFullYear(time):
        this_year = find_year(time)
        if this_year % 4 == 0 and this_year % 100 != 0 or this_year % 400 == 0:
            return True
        else:
            return False
    
    month_list_f = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_list_n = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def daysForThisYear(time):
        totalDays = time // one_day
        daysLeft = totalDays - (find_year(time) - start_year) * 365 - find_full_year(time)
        return int(daysLeft)
    



if __name__ == '__main__':
    now = time.time()
    full_year = str(daysForThisYear(now))
    now_hour = str(find_hour(now))
    now_min = str(find_min(now))
    now_sec = str(find_sec(now))
    print("지금 시각은 "+now_hour+"시"+now_min+"분"+now_sec+"초 입니다.\n")
    print("현재까지 윤년의 갯수는 "+ full_year + " 입니다.\n")




        

