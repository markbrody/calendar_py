import datetime
import time


class Calendar(object):
    def __init__(self, year, month):
        self.year = int(year)
        self.month = int(month)
        self.unixtime = self.get_unixtime()
        self.num_days = self.get_num_days()
        self.start_day = int(self.date(self.unixtime, '%w'))
        self.today = self.get_today()
        self.title = self.date(self.unixtime, '%b %Y')
        self.offset = '1'
        self.days = self.build()

    def get_num_days(self):
        if self.month == 2:
            if self.year % 4 == 0:
                days = 29
            else:
                days = 28
        elif self.month in [4, 6, 9, 11]:
            days = 30
        else:
            days = 31
        return days

    def get_today(self):
        now = int(time.time())
        if self.date(now, '%Y%m') == self.date(self.unixtime, '%Y%m'):
            today = self.date(now, '%d')
        else:
            today = 0
        return today

    def get_unixtime(self):
        datestring = '%s/01/%s' % (self.month, self.year)
        return int(time.mktime(time.strptime(datestring, '%m/%d/%Y')))

    def date(self, unixtime, format='%Y-%m-%d'):
        d = datetime.datetime.fromtimestamp(unixtime)
        return d.strftime(format)
        
    def build(self):
        calendar = []
        for i in range(self.start_day):
            calendar.append(None)
        for i in range(self.num_days):
            calendar.append(i + 1)
        return calendar

    def __str__(self):
        return "year: %s, month: %s" % (self.year, self.month)


class Custody:
    START_DATE = '2015-07-30'

    def offset():
        if 1 == 1:
            return True

    @staticmethod
    def classname(offset):
        modulo = offset % 4
        return {
            0: 'arrive',
            1: 'home',
            2: 'depart',
            3: 'away',
        }.get(modulo, '')

