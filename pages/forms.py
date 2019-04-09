from django import forms

class ContactForm(forms.Form):

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class' : 'form-control'}), required=True)
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class' : 'form-control'}), required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class' : 'form-control'}), required=True)
