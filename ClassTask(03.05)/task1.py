from datetime import datetime, timedelta


class Student:

    def __init__(self, raw_data):
        self.raw_data = raw_data.split(',')
	self.name = self.get_name()
	self.age = self.get_age()
	self.time = self.get_time()	

    def get_name_and_initials(self):
	full_name = self.raw_data[0].split(' ')
	return '{0} {1}.{2}'.format(full_name[0], full_name[1][0],
                                    full_name[2][0])
    
    def get_age(self):
        age = self.raw_data[1]
	current_date = datetime.today()
        
        age_in_days = current_date - datetime.strptime(age, '%d/%m/%Y')
        age = age_in_days.days // 365

	return age

    def get_duration_time(self):
	time = self.raw_data[2].split('-')
	time = [i.split(':') for i in time]
	start_time = int(time[0][0]) * 60 + int(time[0][1])
	end_time = int(time[1][0]) * 60 + int(time[1][1])

	if start_time > end_time:
	    time = (24 * 60 - start_time) + end_time
	else:
	    time = end_time - start_time
	
	return '{0}:{1}'.format(time // 60, time % 60)


if __name__ == '__main__':
    test1 = 'Yatsun Arthur Aaaa,5/09/2000, 19:43-03:01, 180'
    sample = Student(test1)    
	
    print(('{0}, {1}, {2}').format(sample.name, sample.age, sample.time))
