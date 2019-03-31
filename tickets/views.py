"""
Views for Tickets App

Single Bug/Feature
Bugs/Features Lists
Add Bug/Feature
"""
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from comments.models import Comment

from .models import Ticket, Contribution
from .forms import AddBug, AddFeature


def bugs(request):
    """
    View for bug listsing page
    """
    all_bugs = Ticket.objects.all().filter(type='Bug')

    context = {
        'bugs': all_bugs
    }

    return render(request, 'tickets/bugs.html', context)

def features(request):
    """
    View for feature listsing page
    """
    all_features = Ticket.objects.all().filter(type='Feature')

    context = {
        'features': all_features
    }

    return render(request, 'tickets/features.html', context)

def bug(request, bugid):
    """
    View for single bug, also handles adding comments to bug
    """
    if request.method == "POST":

        userid = request.user
        comment = request.POST['comment']
        ticket = get_object_or_404(Ticket, pk=bugid)

        comment = Comment(userid=userid, comment=comment, ticketid=ticket)
        comment.save()

        messages.success(request, 'Thanks for your comment.')
        return redirect('/tickets/bug/'+bugid)

    else:

        current_bug = get_object_or_404(Ticket, pk=bugid)
        comments = Comment.objects.all().filter(ticketid=bugid)

        context = {
            'bug': current_bug,
            'comments': comments
        }

        return render(request, 'tickets/bug.html', context)

def feature(request, featureid):
    """
    View for single feature, also handles adding comments to feature
    """
    if request.method == "POST":

        userid = request.user
        comment = request.POST['comment']
        ticket = get_object_or_404(Ticket, pk=featureid)

        comment = Comment(userid=userid, comment=comment, ticketid=ticket)
        comment.save()

        messages.success(request, 'Thanks for your comment.')
        return redirect('/tickets/feature/'+featureid)

    else:

        current_feature = get_object_or_404(Ticket, pk=featureid)
        contributions = Contribution.objects.all().filter(ticket=featureid)
        comments = Comment.objects.all().filter(ticketid=featureid)
        contrib_amount = Decimal(0.00)

        for contrib in contributions:
            contrib_amount += contrib.amount
            print(contrib_amount)

        contrib_percent = (contrib_amount / current_feature.price) * 100 if contrib_amount < current_feature.price else 100

        contribution_stats = {
            'total_cost' : current_feature.price,
            'current_contribs' : contrib_amount,
            'contrib_percent' : contrib_percent
        }

        context = {
            'feature': current_feature,
            'contributions': contribution_stats,
            'comments': comments,
        }

        return render(request, 'tickets/feature.html', context)

def addbug(request):
    """
    View for adding a bug
    """
    if request.method == "POST":

        form = AddBug(request.POST)
        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.userid = request.user
            ticket.type = "Bug"
            ticket.save()

            messages.success(request, 'Your bug has been logged successfully.')
            return redirect('bug', bugid=ticket.pk)

    else:

        form = AddBug()

    return render(request, 'tickets/addbug.html', {'form':form})

def addfeature(request):
    """
    View for adding a feature
    """
    if request.method == "POST":

        form = AddFeature(request.POST)
        if form.is_valid():

            ticket = form.save(commit=False)
            ticket.userid = request.user
            ticket.type = "Feature"
            ticket.save()

            messages.success(request, 'Your feature request has been logged successfully.')
            return redirect('feature', featureid=ticket.pk)

    else:

        form = AddFeature()

    return render(request, 'tickets/addfeature.html', {'form':form})
