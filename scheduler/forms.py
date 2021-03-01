from django.forms import ModelForm
from. models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'r_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'empId',
            'name',
            'total_load'
        ]


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'pid',
            'time',
            'day'
        ]
        widgets = {
            'pid': forms.TextInput(),
            'time': forms.Select(),
            'day': forms.Select(),
        }


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['subject_code', 'subject_name','subject_abv','semester','theory_load','max_numb_students', 'instructors']


class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        fields = ['sem_name', 'courses']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'semester', 'num_class_in_week']

class DivisionForm(ModelForm):
    class Meta:
        model = Division
        fields = ['section_id','num_class_in_week', 'semester']

class editloadtableforms(forms.ModelForm):
    class Meta:
        model = edit_load_table
        fields = ['subject_abv','subject_load','subject_type']

class labforms(forms.ModelForm):
    class Meta:
        model = lab_load
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']