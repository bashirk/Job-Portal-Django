from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class EmployeeRegistrationForm(UserCreationForm):


    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['gender'].required = True        
        self.fields['first_name'].label = "First Name :"
        self.fields['last_name'].label = "Last Name :"

        self.fields['password1'].label = "Password :"
        self.fields['password1'].help_text = 'Password must contain at least 8 characters.'
        self.fields['password2'].label = "Confirm Password :"
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'
        
        self.fields['emp_salary'].label = "Rate (per task) :"
        self.fields['emp_salary'].help_text = 'Set your rate per each task you fulfill in Naira'

        self.fields['email'].label = "Email :"
        self.fields['gender'].label = "Gender :"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['emp_salary'].widget.attrs.update(
            {
                'placeholder': 'Enter Your Rate',
            }
        )

    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender', 'emp_salary']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employee"
        if commit:
            user.save()
        return user


class EmployerRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].label = "Business Name"
        self.fields['last_name'].label = "Your Address"
        self.fields['password1'].label = "Password :"
        self.fields['password1'].help_text = 'NOTE: The password MUST not be too similar to neither your first name nor your email. And must be 8 or more characters'
        self.fields['password2'].label = "Confirm Password :"
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Business Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Your Address',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
    class Meta:

        model=User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2',]


    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        user.role = "employer"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email =  forms.EmailField(
    widget=forms.EmailInput(attrs={ 'placeholder':'Email',})
) 
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={
        
        'placeholder':'Password',
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Passwords Do not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user



class EmployeeProfileEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['emp_salary'].widget.attrs.update(
            {
                'placeholder': 'Enter Your New Rate Per Task',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender", "emp_salary"]
