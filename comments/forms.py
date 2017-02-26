from .models import Comment
from django import forms


class TreeForm(forms.ModelForm):

    name = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'rows': "3"}))

    class Meta:
        model = Comment
        fields = ('name', 'parent')
