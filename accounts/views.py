# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def login(request):
    
    if request.method == "POST":
        
        # Check if user exists and log them in
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            
            auth.login(request, user)
            messages.success(request, 'You have been logged in.')
            
            return redirect('dashboard')
        
        else:
            
            messages.error(request, 'Invalid username/password')
            return redirect('login')
        
    else:
        
        return render(request, 'accounts/login.html')
    
def register(request):
    
    if request.method == "POST":
        
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            
            if User.objects.filter(email=email).exists():
                
                messages.error(request, 'That email address is already registered')
                return redirect('register')
                
            elif User.objects.filter(username=username).exists():
                
                messages.error(request, 'That username is already registered')
                return redirect('register')
                
            else:
                
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'You have successfully registered, you may now log in.')
                return redirect('login')
                
        else:
            
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
    else:
        
        return render(request, 'accounts/register.html')
    
def logout(request):
    
    if request.method == "POST":
        
        auth.logout(request)
        messages.success(request, 'Logged out')
    
        return redirect('index')
    
def dashboard(request):
    
    # bugs = Ticket.objects.all().filter(type='Bug')
    
    # context = {
    #     'bugs': bugs
    # }
    
    
    return render(request, 'accounts/dashboard.html')