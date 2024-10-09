from django import forms
from .models import Profile
from django.utils.translation import gettext_lazy as _


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user"]

        labels = {
            "phone_number": _("Phone Number"),
            "date_of_birth": _("Date of Birth"),
            "gender": _("Gender"),
            "marital_status": _("Marital Status"),
            "temporary_address": _("Temporary Address"),
            "temporary_city": _("Temporary City"),
            "temporary_state": _("Temporary State"),
            "temporary_country": _("Temporary Country"),
            "temporary_zip_code": _("Temporary Zip Code"),
            "permanent_address": _("Permanent Address"),
            "permanent_city": _("Permanent City"),
            "permanent_state": _("Permanent State"),
            "permanent_country": _("Permanent Country"),
            "permanent_zip_code": _("Permanent Zip Code"),
            "passport_number": _("Passport Number"),
            "issue_date": _("Issue Date"),
            "expiry_date": _("Expiry Date"),
            "issue_country": _("Issue Country"),
            "city_of_birth": _("City of Birth"),
            "country_of_birth": _("Country of Birth"),
            "nationality": _("Nationality"),
            "citizenship": _("Citizenship"),
            "emergency_contact_relationship": _("Emergency Contact Relationship"),
            "emergency_contact_phone": _("Emergency Contact Phone"),
            "emergency_contact_email": _("Emergency Contact Email"),
            "emergency_contact_name": _("Emergency Contact Name"),
        }
        widgets = {
            "phone_number": forms.TextInput(attrs={"class": "input__text"}),
            "date_of_birth": forms.DateInput(
                attrs={"class": "input__text", "placeholder": "YYYY-MM-DD"}
            ),
            "gender": forms.Select(attrs={"class": "input__text"}),
            "marital_status": forms.Select(attrs={"class": "input__text"}),
            "temporary_address": forms.TextInput(attrs={"class": "input__text"}),
            "temporary_city": forms.TextInput(attrs={"class": "input__text"}),
            "temporary_state": forms.TextInput(attrs={"class": "input__text"}),
            "temporary_country": forms.TextInput(attrs={"class": "input__text"}),
            "temporary_zip_code": forms.TextInput(attrs={"class": "input__text"}),
            "permanent_address": forms.TextInput(attrs={"class": "input__text"}),
            "permanent_city": forms.TextInput(attrs={"class": "input__text"}),
            "permanent_state": forms.TextInput(attrs={"class": "input__text"}),
            "permanent_country": forms.TextInput(attrs={"class": "input__text"}),
            "permanent_zip_code": forms.TextInput(attrs={"class": "input__text"}),
            "passport_number": forms.TextInput(attrs={"class": "input__text"}),
            "issue_date": forms.DateInput(
                attrs={"class": "input__text", "placeholder": "YYYY-MM-DD"}
            ),
            "expiry_date": forms.DateInput(
                attrs={"class": "input__text", "placeholder": "YYYY-MM-DD"}
            ),
            "issue_country": forms.TextInput(attrs={"class": "input__text"}),
            "city_of_birth": forms.TextInput(attrs={"class": "input__text"}),
            "country_of_birth": forms.TextInput(attrs={"class": "input__text"}),
            "nationality": forms.TextInput(attrs={"class": "input__text"}),
            "citizenship": forms.TextInput(attrs={"class": "input__text"}),
            "emergency_contact_relationship": forms.TextInput(
                attrs={"class": "input__text"}
            ),
            "emergency_contact_phone": forms.TextInput(attrs={"class": "input__text"}),
            "emergency_contact_email": forms.TextInput(attrs={"class": "input__text"}),
            "emergency_contact_name": forms.TextInput(attrs={"class": "input__text"}),
        }
