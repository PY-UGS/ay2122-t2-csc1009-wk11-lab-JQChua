class Calculator:
    def __init__(self, input1, input2):
        self.input1 = int(input1)
        self.input2 = int(input2)
    def adder(self):
        add = self.input1 + self.input2
        return add
    def subtractor(self):
        sub = self.input1 - self.input2
        return sub
    def multiplier(self):
        mul = self.input1 * self.input2
        return mul
    def divider(self):
        div = self.input1 / self.input2
        return div
    def clear(self):
        self.input1 = 0
        self.input2 = 0

print("Please input first number")
input1 = input()
print("Please input second number")
input2 = input()
Cal = Calculator(input1,input2)
print("adder:")
print(Cal.adder())
print("subtractor:")
print(Cal.subtractor())
print("multiplier:")
print(Cal.multiplier())
print("divider:")
print(Cal.divider())
print("CLEAR")
Cal.clear()
print(Cal.input1)
print(Cal.input2)
