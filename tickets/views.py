from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Ticket
from comments.models import Comment


def bugs(request):
    
    bugs = Ticket.objects.all().filter(type='Bug')
    
    context = {
        'bugs': bugs
    }
    
    return render(request, 'tickets/bugs.html', context)
    
def bug(request, bugid):
    
    bug = get_object_or_404(Ticket, pk=bugid)
    # user = User.objects.get(id=bug.userid.id)
    comments = Comment.objects.all().filter(ticketid=bugid)
    
    context = {
        'bug': bug,
        'comments': comments
    }
    
    return render(request, 'tickets/bug.html', context)
    
def features(request):
    return render(request, 'tickets/features.html')
    
def addticket(request):
    return render(request, 'tickets/addticket.html')