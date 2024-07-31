from django import forms

from contacts.models import Contact
from courses.models import CourseSignUp


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class CourseSignUpForm(forms.ModelForm):
    class Meta:
        model = CourseSignUp
        fields = ['full_name', 'email', 'select_a_course']
