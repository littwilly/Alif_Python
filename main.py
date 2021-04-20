class ReaderWriter:
    def __init__(self, fileName, operationType):
        self.fileName = fileName
        self.operationType = operationType

    def Operation(self):
        f = open(self.fileName)

        result_positive = []
        result_negative = []

        for i in f:
            a, b = [int(j) for j in i.split()]

            if self.operationType == "+":
                if a + b < 0:
                    result_negative.append(a + b)
                elif a + b > 0:
                    result_positive.append(a + b)

            if self.operationType == "-":
                if a - b < 0:
                    result_negative.append(a - b)
                elif a - b > 0:
                    result_positive.append(a - b)

            if self.operationType == "*":
                if a * b < 0:
                    result_negative.append(a * b)
                elif a * b > 0:
                    result_positive.append(a * b)

            if self.operationType == "/":
                if a / b < 0:
                    result_negative.append(a / b)
                elif a / b > 0:
                    result_positive.append(a / b)
        
        p = open("result_positive.txt", "w")
        n = open("result_negative.txt", "w")
        
        for i in result_positive:
            p.write(str(i))
            p.write("\n")
        p.close()

        for i in result_negative:
            n.write(str(i))
            n.write("\n")
        n.close()

fileNameFromUser = input("Enter Name of File: ")
operationTypeFromUser = input("Enter Operation Type: ")

aliftask = ReaderWriter(fileNameFromUser, operationTypeFromUser)
aliftask.Operation()
