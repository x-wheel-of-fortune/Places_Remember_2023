from django import forms
from myApplication.models import Memory

class MemoryForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Memory
        fields = ['place_name', 'comment', 'latitude', 'longitude']
        widgets = {
            'place_name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px; margin-bottom: 5px;'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 500px; height: 400px; margin-bottom: 20px;'}),
        }

