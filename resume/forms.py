from django import forms
from .models import messageInsert

def validator(value):
    if value:
        raise forms.ValidationError('Field is not empty')

class messageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'placeholder':'message...'}))

    validator = forms.CharField(required=False, widget=forms.HiddenInput, label="leave empty", validators=[validator])

    class Meta:
        model = messageInsert
        fields = ['name', 'email', 'message']