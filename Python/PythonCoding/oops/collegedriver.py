from oops.college import College
from oops.student import Student
from oops.studentgrade import StudentGrade
from oops.teacher import Teacher

cc = int(input('C code: '))
cn = input('C name: ')
ci = input('C city: ')
rno = int(input('Roll No: '))
sn = (input('Student Name: '))
m1 = int(input('Mark1: '))
m2 = int(input('Mark2: '))
m3 = int(input('Mark3: '))
eid = int(input('Eid: '))
tn = input('Teacher name: ')
de = input('Dept Name: ')
bp = float(input('Bp: '))

'''project = College(ccode=cc, cname=cn, ccity=ci)

project.welcome_message()
project.display_college_details()'''

project = StudentGrade(ccode=cc, cname=cn, ccity=ci, rno=rno,sname=sn,m1=m1, m2=m2, m3=m3)
project.welcome_message()
project.display_college_details()
print(f'Roll No: {project.rollno} \t Name: {project.stuname} \nTotal: {project.calcu_total()} \nAverage: {project.calc_average()}')
project.calculate_grade()
print(f'Result: {project.result} \t Grade: {project.grade}')

teach = Teacher(ccode=cc, cname=cn, ccity=ci, eid=eid, tn=tn, de=de, bp=bp)
print(f'Eid: {teach.empid} \t Name: {teach.tname} \t Dept: {teach.dept}')
print(f'Salary: {teach.calculate_salary()}')