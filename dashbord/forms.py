from django import forms

BIRTH_YEAR_CHOICES = ["2022", "2023", "2024"]
FORMAT_CHOICES = (
    ('xls', 'xls'),
    ("csv", "csv"),
    ("json", "json"),
)


class ForrmatForm(forms.Form):
    format = forms.ChoiceField(choices=FORMAT_CHOICES, widget=forms.Select(attrs={"class": "form-select"}))


class FormGetDate(forms.Form):
    date1 = forms.DateField(
        label='start Date',
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "mt-2", "id": "From_Date"})
    )
    date2 = forms.DateField(
        label='end Date',
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={"class": "mt-2", "id": "To_Date"})
    )
