# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError


def index(request):
    
    form = ContactForm()
    
    return render(request, "index.html", {'form': form})
    
def about(request):
    return render(request, 'about.html')

def contact(request):
    
    if request.method == "POST":
        
        form = ContactForm(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['adam.p.gibbons@gmail.com'])
                messages.success(request, 'Thanks for your enquiry, we\'ll get back to you soon!')
            except BadHeaderError:
                messages.error(request, 'Thanks for your enquiry!')
            return redirect('index')
            
    else:
            
        return redirect('index')

    
def login(request):
    return render(request, 'login.html')
    
    
class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}), required=True)