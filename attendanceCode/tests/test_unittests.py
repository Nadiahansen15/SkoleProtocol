from django.test import TestCase, SimpleTestCase
from attendanceCode.models import AttendanceCode, AttendanceLog
from keaclass.models import Class as keaclasss
from course.models import Course
from school.models import School
from subject.models import Subject, StudentHasSubject
from teacher.models import Teacher
from student.models import Student
from django.urls import reverse
from django.test import Client
import attendanceCode.calls as func
from django.test import RequestFactory

# from django.contrib.auth import User 
from django.contrib.auth import get_user_model
User = get_user_model()
c = Client()
class TestForms(TestCase):
    def setUp(self):
       
        # Create user 
        test_user1 = User.objects.create_user(username='Andrea44', password='Mor12345')
        test_user1.save()

        self.test_school= School.objects.create(
            id=1,
            name="KEA",
            phone="20434565",
            adress="Guldbergsgade",
            lat=55.691510,
            long=12.555130
        )
        self.test_school.save()

        self.test_course1 = Course.objects.create(
            id=1,
            name="Software Development",
            department="Digital",
            location=self.test_school
        )
        self.test_course1.save()
        
        self.test_class = keaclasss.objects.create(
            name="SDi21",
            year_started="2021",
            Course_name=self.test_course1
        )
        self.test_class.save()
        
        self.test_teacher1 = Teacher.objects.create(
            username="Andera44",
            First_name="Andrea",
            Last_name="thomsen",
            Email="Andrea@test.dk",
            date_joined="2021-03-03"
        )
        self.test_teacher1.save()

        self.test_subject1 = Subject.objects.create(
            name="Testing",
            teacher=self.test_teacher1
        )
        self.test_subject1.save()

        self.test_attendanceCode = AttendanceCode.objects.create(
            code=111,
            keaclass=self.test_class,
            subject=self.test_subject1
        )
        self.test_attendanceCode.save()

        self.test_attendanceLog = AttendanceLog.objects.create(
            attendanceCode=111,
            username_fk="Nadi6548",
            keaclass=self.test_class,
            subject=self.test_subject1,
            lat=55.691510,
            long=12.555130
        )
        self.test_attendanceLog.save()

        self.test_student = Student.objects.create(
            username = "Nadi6548",
            First_name = "nadia",
            Last_name = "hansen",
            Email = "test",
            date_joined = "2021-01-20" ,
            Course = self.test_course1,
            Class = self.test_class,
        )
        self.test_student.save()

        self.StudentHasSubject = StudentHasSubject.objects.create(
            student_name = self.test_student,
            subject_name = self.test_subject1
        )
        self.StudentHasSubject.save()

    def test_user_log_in(self):
        c = Client()
        response = c.post('/accounts/login/', {'username': 'tester', 'password': 'testing1password1'})
        code = response.status_code
        self.assertEqual(code, 200)

    # IF/ELSE SEARCH
    def test_get_statstic(self):
        result = func.get_statstic("SDi21", "1")
        self.assertEqual(result[0],{'name': 'nadia hansen', 'countAttendance': 1, 'countLessons': 1})
    
    def test_get_statstic_with_wrong_input(self):
        result = func.get_statstic("SDi21", "2")
        self.assertEqual(result, [])
    
    def test_get_statstic_class(self):
        result = func.get_statstic_class("SDi21")
        self.assertEqual(result[0],{'name': 'nadia hansen', 'countAttendance': 1, 'countLessons': 1})
        
    def test_get_statstic_class_with_wrong_input(self):
        result = func.get_statstic_class("SDi21111")
        self.assertEqual(result, []) 
