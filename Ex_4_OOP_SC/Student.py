class Student():
    def __init__(self, courseObj):
        self.name = None
        self.courseObj = courseObj

    def set_name(self, name):
        self.name = name

    def get_avg(self):
        return self.courseObj.calc_avg(self)

    def get_avg_v2(self):
        avg = self.courseObj.calc_avg(self)

        if avg >= 8.5:
            grade = "A"
        elif avg >= 7.5:
            grade = "B"
        elif avg >= 6.5:
            grade = "C"
        elif avg >= 5:
            grade = "D"
        else:
            grade = "F"
        return grade
