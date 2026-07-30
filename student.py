class Student: 
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):
        return self.grade >= 60
    class teacher:
        def __init__(self, name, subject):
            self.name = name
            self.subject = subject

        def get_info(self):
            return f"Teacher Name: {self.name}, Subject: {self.subject}"