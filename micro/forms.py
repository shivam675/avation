from django import forms
from .models import Contact

# User profile form, skipping for now
# class ProfileForm(forms.ModelForm):
#     bio = forms.CharField(label ="", widget = forms.Textarea(
#     attrs ={
#         'class':'form-control',
#         'placeholder':'Write something about you',
#         'rows':4,
#         'cols':50
#     }))
#     # name = forms.CharField(label ="Username", widget = forms.Textarea(
#     # attrs ={
#     #     'class':'form-control',
#     #     'placeholder':'Confirm username !',
#     #     'rows':1,
#     #     'cols':5
#     # }))
#     email = forms.CharField(label ="", widget = forms.Textarea(
#     attrs ={
#         'class':'form-control',
#         'placeholder':'Your Email',
#         'rows':1,
#         'cols':5
#     }))
#
#     # profile_photo =  forms.ImageField(label="Profile Photo")
#
#     # url = forms.URLField()
#     class Meta:
#         model = UserProfile
#         fields = [
#         # 'name',
#         'email',
#         'bio',
#         # 'url',
#         'profile_photo',
#         'background',
#         ]


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(label ="  ", widget = forms.Textarea(
    attrs ={
        'class':'form-control title',
        'placeholder':'First Name',
        'rows':1,
        'cols':1
    }))
    last_name = forms.CharField(label ="  ", widget = forms.Textarea(
    attrs ={
        'class':'form-control title',
        'placeholder':'Last Name',
        'rows':1,
        'cols':1
    }))
    number = forms.CharField(label ="  ", widget = forms.Textarea(
    attrs ={
        'class':'form-control title',
        'placeholder':'Phone Number 10 digits only',
        'rows':1,
        'cols':1
    }))
    message = forms.CharField(label ="  ", widget = forms.Textarea(
    attrs ={
        'class':'form-control title',
        'placeholder':'Message',
        'rows':4,
        'cols':1
    }))
    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "number" ,"message"]
