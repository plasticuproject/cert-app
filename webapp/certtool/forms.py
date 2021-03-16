from django import forms
from .models import Certs


class CertForm(forms.ModelForm):
    class Meta:
        model = Certs
        bools = {0: 'No', 1: 'Yes'}
        widgets = {
            'id':
            forms.TextInput(attrs={
                'size': 45,
                'class': 'form-control'
            }),
            'date_added':
            forms.TextInput(attrs={
                'size': 22,
                'class': 'form-control'
            }),
            'applied':
            forms.Select(choices=[('0', 'No'), ('1', 'Yes')],
                         attrs={"class": "form-select"}),
            'date_applied':
            forms.TextInput(attrs={
                'size': 22,
                'class': 'form-control'
            }),
            'banned':
            forms.Select(choices=[('0', 'No'), ('1', 'Yes')],
                         attrs={"class": "form-select"}),
            'banned_date':
            forms.TextInput(attrs={
                'size': 22,
                'class': 'form-control'
            }),
            'required_activation':
            forms.Select(choices=[('0', 'No'), ('1', 'Yes')],
                         attrs={"class": "form-select"}),
            'currently_used':
            forms.Select(choices=[('0', 'No'), ('1', 'Yes')],
                         attrs={"class": "form-select"}),
        }
        fields = [
            'id', 'date_added', 'applied', 'date_applied', 'banned',
            'banned_date', 'required_activation', 'currently_used'
        ]


class CertIdsForm(forms.Form):
    ids = [(cert.id, cert.id.split('-')[0]) for cert in Certs.objects.all()]  # pylint: disable=no-member # noqa: E501
    cert_name = forms.CharField(
        label='Certificate Address',
        widget=forms.Select(choices=ids,
                            attrs={
                                "class":
                                "form-button button margin-b id-select",
                            }),
    )
