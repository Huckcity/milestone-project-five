"""
Views for accounts pages
Login/Logout
Register
Dashboard
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from accounts.forms import EditProfile
from tickets.models import Ticket, Contribution, Vote
from comments.models import Comment

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

@login_required
def logout(request):
    """
    View for handling logout functionality, clears session and redirects to index
    """

    if request.user.is_authenticated():

        auth.logout(request)
        messages.success(request, 'Logged out')

    return redirect('index')

@login_required
def dashboard(request):
    """
    View for dashboard display
    """

    users_bugs = Ticket.objects.all().filter(type='Bug', userid=request.user)
    users_features = Ticket.objects.all().filter(type='Feature', userid=request.user)
    users_comments = Comment.objects.all().filter(userid=request.user)

    for single_bug in users_bugs:

        single_bug.num_comments = Comment.objects.all().filter(ticketid=single_bug.pk).count()
        single_bug.num_votes = Vote.objects.all().filter(ticket=single_bug.pk).count()


    for single_feature in users_features:

        contributions = Contribution.objects.all().filter(ticket=single_feature)
        contrib_amount = Decimal(0.00)

        for contrib in contributions:
            contrib_amount += contrib.amount

        # Determine percentage of goal met, or 100% if over goal amount
        # backslash allows for line break within logic to fix line too long error(pylint)
        contrib_percent = (contrib_amount / single_feature.price) * 100 \
                            if contrib_amount < single_feature.price else 100

        single_feature.total_cost = single_feature.price
        single_feature.current_contribs = contrib_amount
        single_feature.contrib_percent = contrib_percent

    context = {
        'bugs': users_bugs,
        'features' : users_features,
        'comments' : users_comments,
        'new_comments' : users_comments,
    }

    return render(request, 'accounts/dashboard.html', context=context)

def editprofile(request):

    args = {}

    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('editprofile')
    else:
        form = EditProfile(instance=request.user)
        args['form'] = form

        return render(request, 'accounts/editprofile.html', args)

def changepassword(request):

    args = {}

    if request.method == "POST":

        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, 'Your password has been changed successfully.')
            return redirect('dashboard')

        messages.error(request, 'There was an error, please try again.')
        return render(request, 'accounts/changepassword.html')

    form = PasswordChangeForm(user=request.user)
    args['form'] = form

    return render(request, 'accounts/changepassword.html', args)
