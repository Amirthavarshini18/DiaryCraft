from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title (optional)'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your diary entry here...'}),
        }
