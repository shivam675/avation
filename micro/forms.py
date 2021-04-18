from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Write something about you',
        'rows':4,
        'cols':50
    }))
    # name = forms.CharField(label ="Username", widget = forms.Textarea(
    # attrs ={
    #     'class':'form-control',
    #     'placeholder':'Confirm username !',
    #     'rows':1,
    #     'cols':5
    # }))
    email = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Your Email',
        'rows':1,
        'cols':5
    }))

    # profile_photo =  forms.ImageField(label="Profile Photo")

    # url = forms.URLField()
    class Meta:
        model = UserProfile
        fields = [
        # 'name',
        'email',
        'bio',
        # 'url',
        'profile_photo',
        'background',
        ]
