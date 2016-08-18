from django import forms
from .models import Cupcake, Comment

class CupcakeForm(forms.ModelForm):

    class Meta(object):
        model = Cupcake
        fields = ('name', 'rating', 'price', 'image')

class CommentForm(forms.ModelForm):

    class Meta(object):
        model = Comment
        fields = ('text',)
