# accounts/forms.py
from django import forms
from django.forms import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from zxcvbn_password import zxcvbn
from zxcvbn_password.widgets import PasswordStrengthInput
from zxcvbn_password.fields import PasswordField, PasswordConfirmationField


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        widget=forms.TextInput(attrs={'size': 50}),
        help_text=_('Required. Enter an existing email address.'))
    password1 = PasswordField(
        label='Password',
        help_text=password_validation.password_validators_help_text_html(),
        widget=PasswordStrengthInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        }))

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'size': 50}),
        }
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))
        return email


class ChangePasswordForm(PasswordChangeForm):
    new_password1 = PasswordField(
        label='New password',
        help_text=password_validation.password_validators_help_text_html(),
        widget=PasswordStrengthInput(attrs={
            "class": "form-control",
            "placeholder": "New Password"
        }))
