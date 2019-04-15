from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from tickets.models import Ticket

def charts(request):
    return render(request, 'charts/charts.html')

def get_data(request):

    data = Ticket.objects.all() \
        .extra(select={'day': connections[Ticket.objects.db] \
        .ops.date_trunc_sql('day', 'created_on')}) \
        .values('day') \
        .annotate(count_items=Count('id'))

    return JsonResponse(list(data), safe=False)

def type_data_url(request):

    num_bugs = Ticket.objects.filter(type="Bug").count()
    num_features = Ticket.objects.filter(type="Feature").count()

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
