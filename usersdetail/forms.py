from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('type_user', 'first_name', 'last_name', 'profile_picture', 'username',
                  'email_id', 'password1', 'password2', 'address_line1', 'state', 'city', 'pincode')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_picture', 'username',
                  'email_id', 'address_line1', 'state', 'city', 'pincode')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username')
