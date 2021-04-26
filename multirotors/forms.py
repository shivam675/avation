from django import forms
from .models import mRotorsComment

class CommentForm(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = mRotorsComment
        fields =['content']
        # fields ="__all__"
