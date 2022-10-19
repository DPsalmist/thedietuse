from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from apps.home.models import User, Teacher
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'account_type', 'password1', 'password2')


class UserRegistrationForm(forms.ModelForm):
    '''
    password1 = forms.CharField(label='Password', 
                                widget=forms.PasswordInput)

    password2 = forms.CharField(label='Repeat password',
     
                                widget=forms.PasswordInput)

    '''                            
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))

    account_type = forms.Select(
        attrs={
            "placeholder": "Select Account Type",
            "class": "form-control"
        })

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            }
        ))
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'account_type', 'email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('your passwords don\'t match!')
        return cd['password2']


class TeacherRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', 
                                widget=forms.PasswordInput)

    password2 = forms.CharField(label='Repeat password',
     
                                widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ('username', 'first_name', 'last_name','teacher_name', 'subjects', 'what_class', 'department', 'school_type')

