from decimal import Decimal
from django.shortcuts import get_object_or_404

from tickets.models import Ticket, Contribution


def cart_contents(request):
    """
    Context for cross site cart rendering
    """

    cart = request.session.get('cart', {})

    num_contribs = Contribution.objects.filter(userid=request.user.id).count()
    discount = Decimal(num_contribs * 1.5) if Decimal(num_contribs * 1.5) <= 30 else Decimal(30)

    cart_items = set()
    total = 0

    for ticket_id in cart.keys():
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        ticket.contrib_amount = Decimal(cart[ticket_id]['contrib_amount'])
        total += ticket.contrib_amount
        cart_items.add(ticket)

    total_in_cents = total*100
    total_after_discount = total_in_cents - (total_in_cents*(discount/100))

    return {'cart_items': cart_items, 'total': total, 'total_in_cents':total_after_discount}
