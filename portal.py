#entities student, course, teacher, clubs, student_government_member

class Student(object):
    def __init__(self, first_name, last_name, courses, nensei, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses
        self.nensei = nensei
        self.student_id = student_id

    def complete_homework(self, assignment_name):
       print('homework is complete and handed in.\n good job!')


class Teacher(object):
    def __init__(self, courses, first_name, last_name, email, school_id):
        self.courses = courses
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.school_id = school_id

    def lesson_planning(self, for_day):
        print(f"make sure that the plans for {for_day} are ready to go.")
        

class Course(object):
    def __init__(self, course_name, course_number, major, teacher):
        self.course_name = course_name
        self.course_number = course_number
        self.major = major
        self.teacher = teacher


class Club(object):
    def __init__(self, name, time, day):
        self.name = name
        self.time = time
        self.day = day

    def announcments(self, message):
        print(f"To everyone: {message}")

    def next_meeting(self, date, time):
        print(f"The next meeting is on {date}, at {time}")

class StudentGovernmentMember(Student):
    def __init__(self, first_name, last_name, courses, nensei, student_id, government_position):
        super(StudentGovernmentMember, self).__init__(first_name, last_name, courses, nensei, student_id)
        self.government_position = government_position

    def discussion_topics(self):
        print('You currently want to talk about important things at the meeting') 

    def add_discussion_topic(self, topic):
        discussion_topics.append(topic)


Anthony = Student('Anthony', 'McMellen', ['CSET','small business', 'CIS'], '1st', '60908')
Anthony.complete_homework('python classes practice')

Fedor = Teacher('CSET', 'Zach', 'Fedor', 'Fedor@thaddeusstevens.edu', 'Unknown')
Fedor.lesson_planning('Friday')

c160 = Course('CSET-160', '--', 'CSET', 'Professor Fedor')


DnD = Club('DnD', '7pm', 'Thursdays')
DnD.announcments('Today we are having session 0. Make sure you bring your completed character sheets in.')

Tyler = StudentGovernmentMember('Tyler', 'Scotten', ['HVAC'], '2nd', '12345', 'president')
Tyler.discussion_topics()


















