from person import Person

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.score = '0'
        self.courses = []

    def __str__(self):
        return super().__str__() + f"\nscore: {self.score}" + f"\ncourses: {self.courses}"

