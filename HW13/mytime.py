class MyTime(object):
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        elif len(args) == 1 and isinstance(args[0], str):
            if len(args[0].split(':')) == 3:
                self.hours, self.minutes, self.seconds = map(int, args[0].split(':'))
            else:
                print('Set time in format (1:2:3)')
        elif len(args) == 1 and isinstance(args[0], MyTime):
            self.hours, self.minutes, self.seconds = args[0].hours, args[0].minutes, args[0].seconds
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours < other.hours:
            return False
        else:
            if self.minutes > other.minutes:
                return True
            elif self.minutes < other.minutes:
                return False
            else:
                if self.seconds > other.seconds:
                    return True
                else:
                    return False

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            if self.minutes < other.minutes:
                return True
            elif self.minutes > other.minutes:
                return False
            else:
                if self.seconds < other.seconds:
                    return True
                else:
                    return False

    def __ge__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours < other.hours:
            return False
        else:
            if self.minutes > other.minutes:
                return True
            elif self.minutes < other.minutes:
                return False
            else:
                if self.seconds >= other.seconds:
                    return True
                else:
                    return False

    def __le__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            if self.minutes < other.minutes:
                return True
            elif self.minutes > other.minutes:
                return False
            else:
                if self.seconds <= other.seconds:
                    return True
                else:
                    return False

    def __ne__(self, other):
        equality = self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds
        if equality is True:
            return False
        else:
            return True

    def __add__(self, other):
        return f'{self.hours + other.hours}:{self.minutes + other.minutes}:{self.seconds + other.seconds}'

    def __sub__(self, other):
        return f'{self.hours - other.hours}:{self.minutes - other.minutes}:{self.seconds - other.seconds}'

    def __mul__(self, other):
        return f'{self.hours * other.hours}:{self.minutes * other.minutes}:{self.seconds * other.seconds}'

    def normalize_time(self):
        if self.seconds >= 60:
            minutes_addition = self.seconds // 60
            self.minutes += minutes_addition
            self.seconds -= minutes_addition * 60
        if self.minutes >= 60:
            hours_addition = self.minutes // 60
            self.hours += hours_addition
            self.minutes -= hours_addition * 60
        if self.hours >= 24:
            self.hours -= 24


if __name__ == '__main__':
    my_time = MyTime('23:01:30')
    my_time2 = MyTime('22:59:150')
    my_time2.normalize_time()
    print(my_time == my_time2)
