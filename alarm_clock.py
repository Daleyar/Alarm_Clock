class Alarm_Clock:
    def __init__(self):
        self.current_time = ''
        self.status = False
        self.alarm_set = ''

    def time_set(self, time):
        self.current_time = time
        print('The current time is ' + self.current_time)

    def alarm_switch(self):
        if (self.status == False):
            self.status = True
        else:
            self.status = False
    
    def alarm_time(self,time):
        self.alarm_set = time
        print('Your alarm is set to go off at ' + self.alarm_set)