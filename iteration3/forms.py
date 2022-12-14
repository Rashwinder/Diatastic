from django import forms

from django import forms
from .models import Diary_Menu
import datetime as dt

class DiaryForm(forms.ModelForm):
    # Miscellaneous fields.
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date',
                                                           'max': dt.datetime.today().date()}))
    time = forms.TimeField(widget=forms.NumberInput(attrs={'type': 'time'}))

    blood_sugar_level = forms.DecimalField()
    comment = forms.CharField(max_length=1280, widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)

    class Meta:
        model = Diary_Menu
        fields = '__all__'
        exclude = ('diary', 'carbohydrates')
        widgets = {
            'category': forms.Select()
        }

class UserForm(forms.Form):
    username = forms.CharField(label="user", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class DateForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)


class EmailForm(forms.Form):
    to = forms.EmailField()
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)