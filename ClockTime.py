class ClockTime:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    def setHours(self, hours):
        self.hours = hours
    def setMinutes(self, minutes):
        self.minutes = minutes
    def setSeconds(self, seconds):
        self.seconds = seconds
    def setTime(self,hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def showTime(self):
        print(self.hours+":"+self.minutes+":"+self.seconds)

print("Please input hours")
input1 = input()
print("Please input minutes")
input2 = input()
print("Please input seconds")
input3 = input()
CT = ClockTime()
CT.setTime(input1,input2,input3)
CT.showTime()




