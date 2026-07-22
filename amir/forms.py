from django import forms
from amir.models import Post, Contact, NewsLetter


class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'