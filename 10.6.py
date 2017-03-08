# gpa.py
#    Program to find student with highest GPA


class Student:
    def __init__(self):
        self.name = ""
        self.hours = float(0)
        self.qpoints = float(0)
        self.credits = self.hours
        self.gradePoint = float(0)
        self.letterGrade = ""

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
        self.qpoints += (self.gradePoint * self.credits)
        return self.hours, self.qpoints

    def addLetterGrade(self, letterGrade, credits):
        #import pdb; pdb.set_trace()
        gradePoint = float(0)
        if letterGrade == "A":
            gradePoint = 4.0
        elif letterGrade == "A-":
            gradePoint = 3.7
        elif letterGrade == "B+":
            gradePoint = 3.3
        elif letterGrade == "B":
            gradePoint = 3.0
        elif letterGrade == "C+":
            gradePoint = 2.3
        elif letterGrade == "C":
            gradePoint = 2.0
        elif letterGrade == "C-":
            gradePoint = 1.7
        elif letterGrade == "D+":
            gradePoint = 1.3
        elif letterGrade == "D":
            gradePoint = 1.0
        elif letterGrade == "D-":
            gradePoint = 0.7
        elif letterGrade == "F":
            gradePoint = 0.0

        self.credits = credits
        self.gradePoint = gradePoint
        self.hours += self.credits
        self.qpoints += (self.gradePoint * self.credits)
        return self.hours, self.qpoints


def main():
    print("Add a student.\n")
    eStudent = Student()
    eStudent.name = input("Enter student name: ")
    print("Currently {} has {} credits and {} quality points.\n".format(eStudent.name, eStudent.hours, eStudent.qpoints))
    print("Add grade point and credits to {}'s profile.\n".format(eStudent.name))
    letterGrade = input("Enter student grade: ")
    credits = float(input("Enter credit hours: "))
    hours, qpoints = eStudent.addLetterGrade(letterGrade, credits)
    GPA = qpoints / hours
    print("{}'s GPA is {}".format(eStudent.name, GPA))


if __name__ == '__main__':
    main()
