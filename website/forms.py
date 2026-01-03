from django import forms
from website.models import Contact, NewsLetter
from captcha.fields import CaptchaField


# django form
class NameForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    messaeg=forms.CharField(widget=forms.Textarea)

# django mpdel form
class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=Contact
        fields='__all__'    
        # fields=['name','email'] #only name and email
        # exclude=['name'] #all expect name

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model=NewsLetter
        fields='__all__'    