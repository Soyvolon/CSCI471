class Util():
    @staticmethod
    def sum_numbers(n):
        sum = 0
        for k in range(n):
            sum += k
        return sum

    @staticmethod
    def leap_year(year):
        if year % 100 == 0 and year % 400 == 0:
            s = "leap year"
        elif year % 4 == 0 and year % 100 != 0:
            s = "leap year"
        else:
            s = "not a leap year"
        # print(s)
        # modified this for testing.
        return s

    @staticmethod
    def find_largest(a,b,c):
        largest = a
        if b> largest:
            largest = b
        if c > largest:
            largest = c
        return largest