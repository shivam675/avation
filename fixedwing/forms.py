from django import forms
from .models import FixedWingComment

class CommentFormFixedwing(forms.ModelForm):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = FixedWingComment
        fields =['content']
        # fields ="__all__"
