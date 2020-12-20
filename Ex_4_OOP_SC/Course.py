class Course():
    def __init__(self):
        # hard-coding
        """
        For hard-coded values:
            - it will be a unit test: Course (Entity-Model)
        For Data persistance (if there are data files --> .json, .txt, .csv, etc..):
            - it will be an integration test: Because Course <-will import-> the .json data file 
            via the DAO (Db_Handler objectt) 
        """
        self.course_info = [
            {
                "s_name": "Ahmed",  # A
                "mid1": 8.5,
                "mid2": 9.5
            },
            {
                "s_name": "Mohamed",  # B
                "mid1": 9.5,
                "mid2": 6.5
            },
            {
                "s_name": "Gamal",  # C
                "mid1": 5.5,
                "mid2": 7.5
            },
            {
                "s_name": "Kareem",  # D
                "mid1": 5.5,
                "mid2": 4.5
            },
            {
                "s_name": "Haidy",  # F
                "mid1": 1,
                "mid2": 1
            }

        ]

    def search_student(self, studentObj):  # dynamicly typed (duck typing) --> behaviour
        # testing the logic :
        # name IN DB --> returns a student dict
        # name NOT IN DB --> returns None
        for student in self.course_info:
            if student["s_name"] == studentObj.name:
                return student
        return None

    def calc_avg(self, studentObj):
        student = self.search_student(studentObj)
        if not student:
            raise KeyError("[INAVLID_NAME] This student does not exist.")

        return (student["mid1"] + student["mid2"])/2
