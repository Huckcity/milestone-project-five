"""
Views for accounts pages
Login/Logout
Register
Dashboard
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from tickets.models import Ticket

def login(request):
    """
    View for displaying login page and handling login form
    """

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
    """
    View for registration page and handling registration form
    """

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
    """
    View for handling logout functionality, clears session and redirects to index
    """

    if request.user.is_authenticated():

        auth.logout(request)
        messages.success(request, 'Logged out')

    return redirect('index')

def dashboard(request):
    """
    View for dashboard display
    """

    bugs = Ticket.objects.all().filter(type='Bug', userid=request.user)
    features = Ticket.objects.all().filter(type='Feature', userid=request.user)

    context = {
        'bugs': bugs,
        'features' : features,
    }

    return render(request, 'accounts/dashboard.html', context=context)
