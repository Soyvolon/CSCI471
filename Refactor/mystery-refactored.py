from datetime import date

def main():
    ypast = int(input("Enter the year of the past date: "))
    mpast = int(input("Enter the month of the past date (1-12): "))
    dpast = int(input("Enter the day of the past date: "))
    past_date = date(ypast, mpast, dpast)

    ycur = int(input("Enter the current year: "))
    mcur = int(input("Enter the current month (1-12): "))
    dcur = int(input("Enter the current day: "))
    cur_date = date(ycur, mcur, dcur)

    weekday = input("Enter the current day of the week: ")

    week_num = calc_past_weekday(past_date, cur_date, weekday)

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
    days = get_days_for_year_diff(past_date, cur_date)
    
    days += get_days_for_month_to_month(past_date.year, past_date.month + 1, 12)
    # 112
    days += get_days_for_month_to_month(0, past_date.month, past_date.month) - past_date.day

    # 132
    days += get_days_for_month_to_month(cur_date.year, 1, cur_date.month - 1)

    # 436
    days += cur_date.day

    # 454
    if past_date.year == cur_date.year:
        if is_leap(cur_date.year):
            days -= 366
        else:
            days -= 365
    
    weekday = weekday.lower().strip()
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

    old_week_part =  days % 7
    week_num = (week_num - old_week_part + 7) % 7

    return week_num

def is_leap(year: int) -> bool:
    return year % 4 == 0 \
        and year % 100 != 0 \
        or year % 400 == 0

def get_days_for_year_diff(start: date, end: date) -> int:
    days = 0
    year = start.year + 1
    while year < end.year:
        if is_leap(year):
            days += 366
        else:
            days += 365
        year += 1
    return days

def get_days_for_month_to_month(year: int, initial: int, ending: int) -> int:
    days = 0
    month = initial
    while month <= ending:
        if month == 2:
            days += 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            days += 30
        else:
            days += 31
        month += 1
    if is_leap(year) and year != 0:
        if initial <= 2:
            days += 1
    return days

if __name__ == '__main__':
    main()