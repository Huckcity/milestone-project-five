from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.contrib import messages
from tickets.models import Ticket


def cart_contents(request):
    """
    Context for cross site cart rendering
    """

    cart = request.session.get('cart', {})

    cart_items = set()
    total = 0

    for ticket_id in cart.keys():
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        ticket.contrib_amount = Decimal(cart[ticket_id]['contrib_amount'])
        total += ticket.contrib_amount
        cart_items.add(ticket)

    return {'cart_items': cart_items, 'total': total, 'total_in_cents':total*100}
