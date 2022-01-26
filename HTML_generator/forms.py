from cProfile import label
from dataclasses import field
from django import forms
from .models import Content
from ckeditor.widgets import CKEditorWidget


class ContentForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(), label="Text Editor")
    class Meta:
        model = Content
        fields = ('text',)