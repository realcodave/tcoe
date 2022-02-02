from django import forms

from .models import Testimony, Newsletter


class CreateTestimonyForm(forms.ModelForm):

    class Meta:
        model = Testimony
        fields = ['name', 'email', 'subject', 'message']


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ['email']