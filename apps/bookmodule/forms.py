from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']




from .models import Student, Address

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


from .models import Student2, Address2

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple
        }

from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'image']                
