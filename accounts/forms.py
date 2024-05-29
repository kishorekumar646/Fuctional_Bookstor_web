from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class LoginForm(forms.Form):
    phone_regex = RegexValidator(
        regex=r'^[6-9]\d{9}$', message="Phone number is not valid")
    phone_number = forms.CharField(validators=[phone_regex], max_length=10, widget=forms.TextInput(
        attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter a password', 'class': 'mb-4'}))

    def clean(self, *args, **kwargs):

        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        user = authenticate(phone_number=phone_number, password=password)

        if user is None:
            raise forms.ValidationError(
                "Invalid username/password. Please try again!")

        return super(LoginForm, self).clean(*args, **kwargs)

    def login(self, request):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        user = authenticate(phone_number=phone_number, password=password)

        return user


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','phone_number', 'password1', 'password2', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name', 'class': 'mb-4'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name', 'class': 'mb-4'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter a password', 'class': 'mb-4'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter a confirm password', 'class': 'mb-4'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter a valid phone number', 'class': 'mb-4'}),
        }

    def clean(self, *args, **kwargs):
        
        return super(RegisterForm, self).clean(*args, **kwargs)

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
