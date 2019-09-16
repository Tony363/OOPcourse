class TimeStartWork:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def print_time(self):
        print('%.2d : %.2d' % self.hour, self.minute)

eliot = TimeStartWork( 9, 5)

eliot.print_time()
