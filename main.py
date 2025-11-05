class Student:
    def __init__(self, score):
        self.score = score

    @property
    def grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"

    @grade.setter
    def grade(self, value):
        grades = {"A": 95, "B": 85, "C": 75, "D": 65, "F": 50}
        self.score = grades.get(value.upper(), 0)


st = Student(88)
print(st.grade)
st.grade = "A"
print(st.score)
