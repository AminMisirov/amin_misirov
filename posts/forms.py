from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(label="Your Message", widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))
