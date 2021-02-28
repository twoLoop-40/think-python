import datetime as dt 

class Date:
    '''
    datetime obj as input
    '''
    def __init__(self, givendate):
        datelist = givendate.strftime('%c').split(' ')
        self.year = datelist[4]
        self.date = datelist[2]
        self.day = datelist[0]
        self.month = datelist[1]

    def month_to_int(self):
        monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = self.month
        for i in range(12):
            if monthlist[i] == month:
                return i+1
    
    def day_to_int(self):
        daylist = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        day = self.day
        for i in range(7):
            if daylist[i] == day:
                return i+1

def get_age(year, month, date):
    tdy = dt.datetime.today()
    curdate = Date(tdy)
    birthday = Date(dt.datetime(year, month, date))
    return int(curdate.year) - int(birthday.year)

def left_days(year, month, date):
    now = dt.datetime.now()
    nextyear = now.year + 1
    birthday = dt.datetime(nextyear, month, date)
    delta = birthday - now
    days = delta.days
    seconds = delta.seconds
    hours = days*24 + seconds //3600
    mins = hours* 60 + seconds // 60
    return days, hours, mins, mins* 60 + seconds

def double_day(birth1, birth2):
    if birth1 == birth2:
        raise('Always same age!')
    elif birth1 > birth2:
        return birth1 + (birth1 - birth2)
    else:
        return birth2 + (birth2- birth1)





if __name__ == '__main__':
    tdy = dt.datetime.today()
    curdate = Date(tdy)
    print(curdate.day, '이주의 %d번째 날' % (curdate.day_to_int()))

    birthday_date = 1978, 6, 12
    print(get_age(*birthday_date))
    print(left_days(*birthday_date))




    
            

        



