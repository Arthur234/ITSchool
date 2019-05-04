import datetime
from calendar import monthrange

class Student:
    
    def get_name(self):
	"""
	Return name in format <Full Name> <Initials>
	"""

	full_name = self.raw_data[0].split(' ')
	return '{0} {1}.{2}'.format(full_name[0], full_name[1][0], full_name[2][0])
    
    def get_age(self):
	"""
	Calculate student's age in days,months and years
	"""

        age = self.raw_data[1].split('/')
        day = int(age[0])
        month = int(age[1])
	year = int(age[2])
	
	current_date = datetime.datetime.now()
	curr_day = current_date.day
	curr_month = current_date.month
	curr_year = current_date.year
	
	year = curr_year - year	

	if curr_month - month >= 0 and curr_day - day >= 0:
	    month = curr_month - month
	    day = curr_day - day
	elif curr_month - month < 0 and curr_day - day < 0:
	    year -= 1
            month = 12 - (month - curr_month)-1
	    day = monthrange(year, month)[1] - (day - curr_day)
	elif curr_month - month < 0 and curr_day - day >= 0:
	    year -= 1
	    month = 12 - (month - curr_month)
	    day = curr_day - day
	elif curr_month - month >= 0 and curr_day - day < 0:
	    month = month-curr_month-1
            if month < 0:
		year -= 1
		month = 12
	    day = monthrange(year, month)[1] - (day - curr_day)

	return '{0}/{1}/{2}'.format(day, month, year)

    def get_time(self):
	time = self.raw_data[2].split('-')
	time = [i.split(':') for i in time]
	start_time = int(time[0][0])*60 + int(time[0][1])
	end_time = int(time[1][0])*60 + int(time[1][1])

	if start_time > end_time:
	    time = (24 * 60 - start_time) + end_time
	else:
	    time = end_time - start_time
	
	return '{0}:{1}'.format(time//60, time%60)

    def __init__(self, raw_data):
	self.raw_data = raw_data.split(',')
	self.name = self.get_name()
	self.age = self.get_age()
	self.time = self.get_time()	

	print(('{0}, {1}, {2}').format(self.name, self.age, self.time))

if __name__ == '__main__':
    test1 = 'Yatsun Arthur Aaaa, 05/09/2000, 19:43-03:01, 180'
    sample = Student(test1)    
	
