from django import forms
from blog.models import Comment



# django mpdel form
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['post','name','email','subject','message']    

