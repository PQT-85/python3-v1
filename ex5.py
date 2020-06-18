class InandOut:

    def getString(self):
        self.string = input("Enter your text: ")  # use the variable

    def printString(self):
        print(self.string.upper())  # call upper string method


strObj = InandOut()
strObj.getString()
strObj.printString()
