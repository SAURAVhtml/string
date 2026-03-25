class IOstring:
    def __init__(self):
        self.strl = ""
    def getstring(self):
        self.strl = input("enter the string: ")
    def printstring(self):
        print("Result is: ",self.strl.upper())
strl = IOstring()
strl.getstring()
strl.printstring()
