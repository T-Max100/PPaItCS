# gpa.py
#    Program to find student with highest GPA


class Student:
    def __init__(self):
        #self.name = name
        self.hours = float(0)
        self.qpoints = float(0)
        self.credits = self.hours

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        self.hours += self.credits
        self.qpoints += (gradePoint * self.credits)
        return self.hours, self.qpoints


# def makeStudent():
#     name = input("Enter student name: ")
#     gradePoint = float("Enter student grade: ")
#     credits = float("Enter credit hours: ")
#     hours, qpoints = addGrade(gradePoint, credits)
#     return Student(name, hours, qpoints)


def main():
    print("Add a student.\n")
    eStudent = Student()
    eStudent.name = input("Enter student name: ")
    print("Currently {} has {} credits and {} quality points.\n".format(eStudent.name, eStudent.hours, eStudent.qpoints))
    print("Add grade point and credits to {}'s profile.\n")
    gradePoint = float(input("Enter student grade: "))
    credits = float(input("Enter credit hours: "))
    hours, qpoints = eStudent.addGrade(gradePoint, credits)
    GPA = gradePoint
    print("{}'s GPA is {}".format(eStudent.name, GPA))


if __name__ == '__main__':
    main()
