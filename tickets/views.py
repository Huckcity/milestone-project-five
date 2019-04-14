"""
Views for Tickets App

Single Bug/Feature
Bugs/Features Lists
Add Bug/Feature
"""
from decimal import Decimal
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from comments.models import Comment

from .models import Ticket, Contribution, Vote
from .forms import AddBug, AddFeature


def bugs(request):
    """
    View for bug listsing page
    """
    bug_set = Ticket.objects.all().filter(type='Bug')

    for single_bug in bug_set:

        single_bug.num_comments = Comment.objects.all().filter(ticketid=single_bug.pk).count()
        single_bug.num_votes = Vote.objects.all().filter(ticket=single_bug.pk).count()

    paginator = Paginator(bug_set, 5)

    page = request.GET.get('page', 1)

    all_bugs = paginator.page(page)

    context = {
        'bugs': all_bugs
    }

    return render(request, 'tickets/bugs.html', context)

def features(request):
    """
    View for feature listsing page
    """
    all_features = Ticket.objects.all().filter(type='Feature')

    for single_feature in all_features:

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
        votes = Vote.objects.all().filter(ticket=bugid).count()

        context = {
            'bug': current_bug,
            'comments': comments,
            'votes' : votes
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
        comments = Comment.objects.all().filter(ticketid=featureid)
        contributions = Contribution.objects.all().filter(ticket=featureid)
        contrib_amount = Decimal(0.00)

        for contrib in contributions:
            contrib_amount += contrib.amount

        # Determine percentage of goal met, or 100% if over goal amount
        # backslash allows for line break within logic to fix line too long error(pylint)
        contrib_percent = (contrib_amount / current_feature.price) * 100 \
                           if contrib_amount < current_feature.price else 100



        current_feature.total_cost = current_feature.price
        current_feature.current_contribs = contrib_amount
        current_feature.contrib_percent = contrib_percent

        context = {
            'feature': current_feature,
            'comments': comments,
        }

        return render(request, 'tickets/feature.html', context)

@login_required
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

@login_required
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

@login_required
def addvote(request, bugid):
    """
    Upvote handler, to be called asynchronously
    """
    if request.method == "POST":

        user = request.user
        ticket = get_object_or_404(Ticket, pk=bugid)

        existing_vote = Vote.objects.all().filter(user=user, ticket=ticket).count()
        print(existing_vote)

        if existing_vote > 0:
            messages.error(request, 'You have already upvoted this bug!')
            return redirect('/tickets/bug/'+bugid)
        else:
            vote = Vote(user=user, ticket=ticket)
            vote.save()

            messages.success(request, 'Thanks for your vote.')
            return redirect('/tickets/bug/'+bugid)

@login_required
def editbug(request, ticketid):

    ticket = get_object_or_404(Ticket, pk=ticketid)

    form = AddBug(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()

        messages.success(request, 'Changes saved!')
        return redirect('bug', ticketid)

    return render(request, 'tickets/editbug.html', {'form':form, 'ticketid':ticketid})

@login_required
def editfeature(request, ticketid):

    ticket = get_object_or_404(Ticket, pk=ticketid)

    form = AddFeature(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()

        messages.success(request, 'Changes saved!')
        return redirect('feature', ticketid)

    return render(request, 'tickets/editfeature.html', {'form':form, 'ticketid':ticketid})
