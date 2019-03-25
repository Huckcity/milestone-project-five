from django.shortcuts import render

from .models import Ticket

def bugs(request):
    
    tickets = Ticket.objects.all()
    
    context = {
        'tickets': tickets
    }
    
    return render(request, 'tickets/bugs.html', context)
    
def features(request):
    return render(request, 'tickets/features.html')
    
def addticket(request):
    return render(request, 'tickets/addticket.html')