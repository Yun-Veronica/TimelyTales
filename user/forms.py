from django.contrib.auth.models import User
from django import forms
from django import forms
from .models import UserModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'username', 'email', 'hashed_password', 'profile_picture']

        widgets = {
            'hashed_password': forms.PasswordInput(),
        }

    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data.get('hashed_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password