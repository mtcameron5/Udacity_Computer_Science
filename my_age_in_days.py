def days_in_year(month, day):

	daysofMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	total_days = 0
	total_days += day

	while month >= 2:
		total_days += daysofMonth[month - 2]
		month -= 1
	return total_days 	

def leap_years(current_month, current_day, current_year, birth_month, birth_day, birth_year, days):

	counter = 0
	counter_to_add = 1
	birth_counter_year = birth_year
	how_many_leap_years = 0

	while current_year >= birth_counter_year: 
		if birth_counter_year % 4.0 == 0:
			counter_to_add = 4
		if birth_counter_year % 4.0 == 0 and (birth_counter_year % 100.0 != 0 or birth_counter_year % 400.0 == 0):
			days += 1
			how_many_leap_years += 1
		birth_counter_year += counter_to_add

	# Check if birth year was a leap year but February had already occurred (i.e. leap day had passed before birth)
	if birth_year % 4 == 0 and (birth_year % 100.0 != 0 or birth_year % 400.0 == 0):
		if birth_month < 2:
			return days
		else:
			return days - 1

	# Check if current year is a leap year but February has not ended (i.e. leap day has not yet occurred)
	if current_year % 4 == 0 and (birth_year % 100.0 != 0 or birth_year % 400.0 == 0):
		if birth_month > 2:
			return days 
		else:
			return days - 1

	return days

def check_if_birthdate_is_before(current_month, current_day, current_year, birth_month, birth_day, birth_year):
	if current_year < birth_year:
		return False 
	elif current_year == birth_year:
		if birth_month > current_month:
			return False 
		elif birth_month == current_month:
			if birth_day > current_day:
				return False
	return True


def age_in_days(current_month, current_day, current_year, birth_month, birth_day, birth_year):

	if check_if_birthdate_is_before(current_month, current_day, current_year, birth_month, birth_day, birth_year):
		days = 0

		if birth_month > current_month:
			days -= days_in_year(birth_month, birth_day) - days_in_year(current_month, current_day)
		elif birth_month < current_month:
			days += days_in_year(current_month, current_day) - days_in_year(birth_month, birth_day)
		elif birth_month == current_month:
			if birth_day > current_day:
				days -= birth_day - current_day
			else:
				days += current_day - birth_day
		days += (current_year - birth_year) * 365

		days = leap_years(current_month, current_day, current_year, birth_month, birth_day, birth_year, days)

		return days
	else:
		return "The birthday comes before the current day"

birth_day = 1
birth_month = 1
birth_year = 2013 
current_day = 31
current_month = 12
current_year = 1999
print age_in_days(current_month, current_day, current_year, birth_month, birth_day, birth_year)


# print leap_years(9, 21, 2018, 11, 24, 1992, 0)



