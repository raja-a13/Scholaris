from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)


class TeacherRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254,required=True)
    admin_id = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'admin_id'
        )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        admin_id = cleaned_data.get('admin_id')

        print('did clean run?')

        if password != confirm_password:
            print('are password not equal?')
            self.add_error('password', 'Password Did Not Match')

        if admin_id != '12345':
            print('Yes it is right')
            self.add_error('admin_id', 'Admin id does not match')


class StudentRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254,required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        print('did clean run?')

        if password != confirm_password:
            print('are password not equal?')
            self.add_error('password', 'Password Did Not Match')

