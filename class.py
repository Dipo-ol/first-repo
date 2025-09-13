class School:
    def __init__(self, name: str, grade: str):
        self.name = name
        self.grade = grade
        self.is_enrolled = False

    def enroll(self):
        if self.is_enrolled:
            print(f"student is already enrolled to {self.name}")
        else:
            self.is_enrolled = True
            print(f"the student is now enrolled to {self.name}")

    def not_enroll(self):
        if self.is_enrolled:
            self.is_enrolled = False
            print(f"student is now unenrolled")

        else:
            print("the student is already unenrolled")

    def learn(self, student: str):
        if self.is_enrolled:
            print(f"{student} is learning in {self.name}")
        else:
            print("you should probably enroll first")


ttc: School = School("ttc", "A")
stee: School = School("stee", "A")
ttc.enroll()
ttc.enroll()
ttc.learn("dipo")
ttc.not_enroll()
ttc.learn("bro")
print(stee.name)
print(stee.grade)
stee.learn("bro")
stee.enroll()
stee.learn("nelly")
