from django import forms
from .models import Consultancy
from django.utils.translation import gettext_lazy as _


class ConsultancyForm(forms.ModelForm):
    class Meta:
        model = Consultancy
        fields = [
            "name",
            "company_email",
            "website",
            "address",
            "city",
            "state",
            "zip_code",
            "country",
            "phone",
            "whatsapp",
        ]
        labels = {
            "name": _("Name"),
            "company_email": _("Company Email"),
            "website": _("Website"),
            "address": _("Address"),
            "city": _("City"),
            "state": _("State"),
            "zip_code": _("Zip Code"),
            "country": _("Country"),
            "phone": _("Phone"),
            "whatsapp": _("WhatsApp"),
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "input__text"}),
            "company_email": forms.TextInput(attrs={"class": "input__text"}),
            "website": forms.URLInput(attrs={"class": "input__text"}),
            "address": forms.TextInput(attrs={"class": "input__text"}),
            "city": forms.TextInput(attrs={"class": "input__text"}),
            "state": forms.Select(attrs={"class": "input__text"}),
            "zip_code": forms.TextInput(attrs={"class": "input__text"}),
            "country": forms.TextInput(attrs={"class": "input__text"}),
            "phone": forms.TextInput(attrs={"class": "input__text"}),
            "whatsapp": forms.TextInput(attrs={"class": "input__text"}),
        }
