import logging

class StudentProcessor:
    def __init__(self):
        self.students = []
        self.logger = logging.getLogger('LOG')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())
    def add_student(self, student):
        self.students.append(student)
        self.logger.info(f'{student} був доданий до списку students')
    def remove_student(self, student):
        try:
            self.students.remove(student)
            self.logger.info(f'{student} був видалений з списку students')
        except:
            print(f'{student} не був знайдений в списку students')
    def process_students(self):
        for student in self.students:
            self.logger.info(f'{student} є студентом школи')
student1 = 'Masha'
student2 = 'Oleg'
student3 = 'Dmytro'

student4 = 'Pavlo'
s = StudentProcessor()
s.students = [student1, student2, student3]

s.add_student(student4)
s.remove_student(student2)

s.process_students()