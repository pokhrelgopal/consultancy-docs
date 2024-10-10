from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Profile, Education, LanguageTest, Document


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
            "temporary_address": _("Address"),
            "temporary_city": _("City"),
            "temporary_state": _("State"),
            "temporary_country": _("Country"),
            "temporary_zip_code": _("Zip Code"),
            "permanent_address": _("Address"),
            "permanent_city": _("City"),
            "permanent_state": _("State"),
            "permanent_country": _("Country"),
            "permanent_zip_code": _("Zip Code"),
            "passport_number": _("Passport Number"),
            "issue_date": _("Issue Date"),
            "expiry_date": _("Expiry Date"),
            "issue_country": _("Issue Country"),
            "city_of_birth": _("City of Birth"),
            "country_of_birth": _("Country of Birth"),
            "nationality": _("Nationality"),
            "citizenship": _("Citizenship"),
            "emergency_contact_relationship": _("Contact Relationship"),
            "emergency_contact_phone": _("Contact Phone"),
            "emergency_contact_email": _("Contact Email"),
            "emergency_contact_name": _("Contact Name"),
        }
        widgets = {
            "phone_number": forms.TextInput(attrs={"class": "input__text"}),
            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "input__text",
                    "placeholder": "YYYY-MM-DD",
                    "type": "date",
                }
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
                attrs={
                    "class": "input__text",
                    "placeholder": "YYYY-MM-DD",
                    "type": "date",
                }
            ),
            "expiry_date": forms.DateInput(
                attrs={
                    "class": "input__text",
                    "placeholder": "YYYY-MM-DD",
                    "type": "date",
                }
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


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
        exclude = ["user", "created_at", "updated_at"]
        labels = {
            "country": _("Country"),
            "city": _("City"),
            "state": _("State"),
            "level": _("Level"),
            "university_name": _("University Name"),
            "qualification_achieved": _("Qualification Achieved"),
            "gpa_system": _("GPA System"),
            "score": _("Score"),
            "backlogs": _("Backlogs"),
            "language": _("Language"),
            "start_date": _("Start Date"),
            "end_date": _("End Date"),
        }
        widgets = {
            "country": forms.TextInput(attrs={"class": "input__text"}),
            "city": forms.TextInput(attrs={"class": "input__text"}),
            "state": forms.TextInput(attrs={"class": "input__text"}),
            "level": forms.Select(attrs={"class": "input__text"}),
            "university_name": forms.TextInput(attrs={"class": "input__text"}),
            "qualification_achieved": forms.TextInput(attrs={"class": "input__text"}),
            "gpa_system": forms.Select(attrs={"class": "input__text"}),
            "score": forms.NumberInput(attrs={"class": "input__text"}),
            "backlogs": forms.NumberInput(attrs={"class": "input__text"}),
            "language": forms.TextInput(attrs={"class": "input__text"}),
            "start_date": forms.DateInput(
                attrs={"class": "input__text", "type": "date"}
            ),
            "end_date": forms.DateInput(attrs={"class": "input__text", "type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        gpa_system = cleaned_data.get("gpa_system")
        score = cleaned_data.get("score")

        if start_date and end_date and end_date <= start_date:
            raise ValidationError(_("End date must be after start date."))

        if gpa_system and score is not None:
            self.validate_gpa_score(gpa_system, score)

        return cleaned_data

    def validate_gpa_score(self, gpa_system, score):
        gpa_ranges = {
            "4.0": (0, 4.0),
            "5.0": (0, 5.0),
            "7.0": (0, 7.0),
            "10.0": (0, 10.0),
            "100": (0, 100),
        }

        if gpa_system in gpa_ranges:
            min_score, max_score = gpa_ranges[gpa_system]
            if score < min_score or score > max_score:
                raise ValidationError(
                    _(
                        f"Score must be between {min_score} and {max_score} for the selected GPA system."
                    )
                )
        else:
            raise ValidationError(_("Invalid GPA system selected."))


class LanguageTestForm(forms.ModelForm):
    class Meta:
        model = LanguageTest
        fields = "__all__"
        exclude = ["user", "created_at", "updated_at"]
        labels = {
            "test": _("Test"),
            "score": _("Score"),
            "test_document": _("Test Document"),
        }
        widgets = {
            "test": forms.Select(attrs={"class": "input__text"}),
            "score": forms.NumberInput(attrs={"class": "input__text"}),
            "test_document": forms.FileInput(attrs={"class": "input__text"}),
        }


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            "document",
            "document_file",
        ]
        labels = {
            "document": _("Document"),
            "document_file": _("Document File"),
        }
        widgets = {
            "document": forms.Select(attrs={"class": "input__text"}),
            "document_file": forms.FileInput(attrs={"class": "input__file"}),
        }
