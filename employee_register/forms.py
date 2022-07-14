from django import forms
from .models import Employee, Etudiant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname','mobile','emp_code','position')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP. Code',
        }

    def __init__(self, *args, **kwargs):
            super(EmployeeForm,self).__init__(*args, **kwargs)
            self.fields['position'].empty_label = "Select"

class EtudiantForm(forms.ModelForm):

    class Meta:
        model = Etudiant
        fields = ('fullname','mobile','etu_code','niveau')
        labels = {
            'fullname':'Full Name',
            'etu_code':'ETU. Code',
        }

    def __init__(self, *args, **kwargs):
            super(EtudiantForm,self).__init__(*args, **kwargs)
            self.fields['niveau'].empty_label = "Select"
           
class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        ]