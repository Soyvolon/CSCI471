

yp = int(input("Enter the year of the past date: "))
mp = int(input("Enter the month of the past date (1-12): "))
dp = int(input("Enter the day of the past date: "))
yc = int(input("Enter the current year: "))
mc = int(input("Enter the current month (1-12): "))
dc = int(input("Enter the current day: "))
w = input("Enter the current day of the week: ")
db = 0

y = yp + 1
while y < yc:
    if y%4 == 0 and y%100 != 0 or y%400 == 0:
        db += 366
    else:
        db += 365
    y += 1

m = mp + 1
while m <= 12:
    if m == 2:
        db += 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        db += 30
    else:
        db += 31
    m += 1
if yp%4 == 0 and yp%100 != 0 or yp%400 == 0:
    if mp <= 2:
        db += 1

if mp == 2:
    db += (28-dp)
elif mp == 4 or mp == 6 or mp == 9 or mp == 11:
    db += (30-dp)
else:
    db += (31-dp)
if yp%4 == 0 and yp%100 != 0 or yp%400 == 0:
    if mp == 2:
        db += 1

m = 1
while m < mc:
    if m == 2:
        db += 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        db += 30
    else:
        db += 31
    m += 1
if yc%4 == 0 and yc%100 != 0 or yc%400 == 0:
    if mc > 2:
        db += 1

db += dc

if yp == yc:
    if yc%4 == 0 and yc%100 != 0 or yc%400 == 0:
        db -= 366
    else:
        db -= 365

dd = db % 7
if w == "Sunday":
    wn = 1
elif w == "Monday":
    wn = 2
elif w == "Tuesday":
    wn = 3
elif w == "Wednesday":
    wn = 4
elif w == "Thursday":
    wn = 5
elif w == "Friday":
    wn = 6
else:
    wn = 7
wn = (wn - dd + 7) % 7
if wn == 1:
    print("The past date was a Sunday.")
elif wn == 2:
    print("The past date was a Monday.")
elif wn == 3:
    print("The past date was a Tuesday.")
elif wn == 4:
    print("The past date was a Wednesday.")
elif wn == 5:
    print("The past date was a Thursday.")
elif wn == 6:
    print("The past date was a Friday.")
else:
    print("The past date was a Saturday.")
