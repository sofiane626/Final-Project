from django import forms
from .models import Contact, Reply


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
