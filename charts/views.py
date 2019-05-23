from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from django.db.models.functions import TruncDate
from django.db.models import Sum, Count

from tickets.models import Ticket, Contribution
from comments.models import Comment

# Create your views here.
def charts(request):
    return render(request, 'charts/charts.html')

def get_data(request):

    data = Ticket.objects.all() \
        .annotate(day=TruncDate('created_on')) \
        .values("day") \
        .annotate(count_items=Count('id')) \
        .order_by('day')

    return JsonResponse(list(data), safe=False)

def type_data_url(request):

    num_bugs = Ticket.objects.filter(ticket_type="Bug").count()
    num_features = Ticket.objects.filter(ticket_type="Feature").count()

    data = [
        {
            'type': 'Bug',
            'count': num_bugs
        },
        {
            'type': 'Feature',
            'count': num_features
        }
    ]
        
    return JsonResponse(list(data), safe=False)

def average_feature_progress(request):

    running_percent = 0

    features = Ticket.objects.filter(ticket_type="Feature")

    for feature in features:

        running_percent += feature.percent_complete

    average_contrib_percent = running_percent / len(features) \
                              if len(features) > 1 else running_percent

    return JsonResponse(average_contrib_percent, safe=False)
    
def get_comment_data(request):

    data = Comment.objects.all() \
        .annotate(day=TruncDate('posted_on')) \
        .values("day") \
        .annotate(count_items=Count('id')) \
        .order_by('day')

    return JsonResponse(list(data), safe=False)

def get_tickets_by_status(request):

    pending = 0
    in_progress = 0
    complete = 0

    tickets = Ticket.objects.all()
    for ticket in tickets:
        if ticket.status == "Pending":
            pending += 1
        if ticket.status == "In Progress":
            in_progress += 1
        if ticket.status == "Complete":
            complete += 1

    data = [pending, in_progress, complete]

    return JsonResponse(list(data), safe=False)