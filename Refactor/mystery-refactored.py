from datetime import date

def main():
    # Start with getting the previous date data ...
    ypast = int(input("Enter the year of the past date: "))
    mpast = int(input("Enter the month of the past date (1-12): "))
    dpast = int(input("Enter the day of the past date: "))
    # ... and building the date object ...
    past_date = date(ypast, mpast, dpast)

    # .... then getting the current date data ...
    ycur = int(input("Enter the current year: "))
    mcur = int(input("Enter the current month (1-12): "))
    dcur = int(input("Enter the current day: "))
    # ... and building the date object ...
    cur_date = date(ycur, mcur, dcur)

    # ... then getting the weekday ...
    weekday = input("Enter the current day of the week: ")

    # ... the week num ...
    week_num = calc_past_weekday(past_date, cur_date, weekday)

    # ... then displaying the result.
    if week_num == 1:
        print("The past date was a Sunday.")
    elif week_num == 2:
        print("The past date was a Monday.")
    elif week_num == 3:
        print("The past date was a Tuesday.")
    elif week_num == 4:
        print("The past date was a Wednesday.")
    elif week_num == 5:
        print("The past date was a Thursday.")
    elif week_num == 6:
        print("The past date was a Friday.")
    else:
        print("The past date was a Saturday.")

def calc_past_weekday(past_date: date, cur_date: date, weekday: str) -> int:
    # To start with, get the days from the difference in years ...
    days = get_days_for_year_diff(past_date, cur_date)
    
    # ... then the days from the past month to the end of the past year ...
    days += get_days_for_month_to_month(past_date.year, past_date.month + 1, 12)
    # ... then the days for the past month minus the days already passed in the month ...
    days += get_days_for_month_to_month(0, past_date.month, past_date.month) - past_date.day

    # ... then the days from the start of the current year to the current month ...
    days += get_days_for_month_to_month(cur_date.year, 1, cur_date.month - 1)

    # ... then add the days in the current month ...
    days += cur_date.day

    # ... and if the years are the same ...
    if past_date.year == cur_date.year:
        # ... and it is a leap year ...
        if is_leap(cur_date.year):
            # ... subtract the days in the extra year we calculated ...
            days -= 366
        else:
            # ... subtract the days in the extra year we calculated ...
            days -= 365
    
    # ... then get a readable weekday string ...
    weekday = weekday.lower().strip()
    # ... and find the numerical day of the week for the current weekday ...
    if weekday == "sunday":
        week_num = 1
    elif weekday == "monday":
        week_num = 2
    elif weekday == "tuesday":
        week_num = 3
    elif weekday == "wednesday":
        week_num = 4
    elif weekday == "thursday":
        week_num = 5
    elif weekday == "friday":
        week_num = 6
    else:
        week_num = 7

    # ... then find the part of the week the the past date was on ...
    old_week_part =  days % 7
    # ... and find the exact number for the day of the week ...
    week_num = (week_num - old_week_part + 7) % 7

    # ... then return the day of the week.
    return week_num

def is_leap(year: int) -> bool:
    # If the year is divisible by four and not by 100, or it is divisible by 400,
    # then it is a leap year.
    return year % 4 == 0 \
        and year % 100 != 0 \
        or year % 400 == 0

def get_days_for_year_diff(start: date, end: date) -> int:
    # Create the days counter ...
    days = 0
    # ... set the start year ...
    year = start.year + 1
    # ... while the year is lower than the end year ...
    while year < end.year:
        # ... if the year is a leap year ...
        if is_leap(year):
            # ... add days ...
            days += 366
        else:
            # ... add days ...
            days += 365
        # ... increment the year ...
        year += 1
    # ... finally, return the total days.
    return days

def get_days_for_month_to_month(year: int, initial: int, ending: int) -> int:
    # Create the days counter ...
    days = 0
    # ... set the start month ...
    month = initial
    # ... while the start month is lower than or equal to the end month ...
    while month <= ending:
        # ... if the month is the second month in the year ...
        if month == 2:
            # ... add days ...
            days += 28
        # ... if the month is a 30 day month ...
        elif month == 4 or month == 6 or month == 9 or month == 11:
            # ... add days ...
            days += 30
        else:
            # ... otherwise, add 31 days ...
            days += 31
        # ... increment the month ...
        month += 1
    # ... and if this is a leap year, and the year value is not 0 ...
    if is_leap(year) and year != 0:
        # ... and the second month has passed ...
        if initial <= 2:
            # ... add the extra day ...
            days += 1
    # ... then return the elapsed days.
    return days

if __name__ == '__main__':
    # Run the program.
    main()