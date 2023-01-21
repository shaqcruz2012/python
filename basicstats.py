# For this project, you will `import` the **statistics** module.

# Write a class called Student that has two **private** data members - the student's name and grade.  It should have an init method that takes two values and uses them to initialize the data members. It should have a `get_grade` method.

# Write a separate function (not part of the Student class) called `basic_stats` that takes as a parameter a list of Student objects and returns a tuple containing the mean, median, and mode of all the grades.  To do this, use the mean, median and mode functions in the [statistics module](https://docs.python.org/3/library/statistics.html). Your `basic_stats` function should return those three values as a tuple, in the exact order given above.

# As an example, your code could be called as follows by the grader:

# s1 = Student("Kyoungmin", 73)
# s2 = Student("Mercedes", 74)
# s3 = Student("Avanika", 78)
# s4 = Student("Marta", 74)

# student_list = [s1, s2, s3, s4]
# print(basic_stats(student_list))  # should print a tuple of three values

import statistics
#classes have self and other params
class student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade
    
    def get_grade(self):
        return self.__grade

def basic_stats(list_student_objects):
    # using 'list comprehension' to extract grades
    # [expression for item in iterable]
    # expression is student.get_grade() calls the item, student in list_student_objects iterable
    grades = [student.get_grade() for student in list_student_objects]
    # metric = statistics.method(grades)
    mean = statistics.mean(grades)
    median = statistics.median(grades)
    mode = statistics.mode(grades)
    return (mean,median,mode)