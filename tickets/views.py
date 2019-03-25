from django.shortcuts import render, redirect, get_object_or_404
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
    
    if request.method == "POST":
        
        userid = request.user
        comment = request.POST['comment']
        ticket = get_object_or_404(Ticket, pk=bugid)
        
        comment = Comment(userid = userid, comment=comment, ticketid=ticket)
        comment.save()
        
        messages.success(request, 'Thanks for your comment.')
        return redirect('/tickets/bug/'+bugid)
        
    else:
    
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