from decimal import Decimal
import stripe

from django.conf import settings
from django.db.models import Sum
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tickets.models import Contribution
from tickets.views import Ticket

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def view_cart(request):

    num_contribs = Contribution.objects.filter(userid=request.user.id).count()
    discount = Decimal(
        num_contribs * 1.5) if Decimal(num_contribs * 1.5) <= 30 else Decimal(30)

    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY,
        'num_contribs': num_contribs,
        'discount': discount
    }

    return render(request, "cart/cart.html", context)


@login_required
def addtocart(request, featureid):
    """
    Add an amount to the cart for contributions to check out at a later time
    """
    if not request.POST['contribution_amount'] or request.POST['contribution_amount'] == '' or int(request.POST['contribution_amount']) < 1:
        messages.error(
            request, 'You must submit a valid contribution amount.')
        return redirect('/tickets/feature/'+featureid)

    cart = request.session.get('cart', {})
    if featureid not in cart:

        cart[featureid] = {
            'id': featureid,
            'contrib_amount': request.POST['contribution_amount']
        }

    else:

        messages.error(
            request, 'You\'re already contributing to this feature.')
        return redirect('/tickets/feature/'+featureid)

    request.session['cart'] = cart

    return redirect("cart")


@login_required
def removefromcart(request, featureid):
    """
    Delete a feature contribution from the cart
    """
    cart = request.session.get('cart', {})

    if featureid in cart:

        del cart[featureid]
        messages.success(request, "Feature removed")

    request.session['cart'] = cart

    return redirect(reverse('cart'))


@login_required
def checkout(request):

    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY
    }

    return render(request, "cart/checkout.html", context)


@login_required
def charge(request):

    if request.method == 'POST':

        num_contribs = Contribution.objects.filter(
            userid=request.user.id).count()
        discount = Decimal(
            num_contribs * 1.5) if Decimal(num_contribs * 1.5) <= 30 else Decimal(30)
        print('discount = ', discount)

        cart = request.session.get('cart', {})
        total_charge = 0

        for item in cart.keys():

            amount = cart[item]['contrib_amount']
            total_charge += Decimal(amount)

        print('total charge = ', total_charge)
        discount_amount = (total_charge/100) * \
            discount if discount > 0 else total_charge
        print('discount_amount = ', discount_amount)

        amount_owed_after_discount = total_charge - discount_amount
        print('amount_owed_after_discount = ', amount_owed_after_discount)

        try:

            payment = stripe.Charge.create(
                amount=int(amount_owed_after_discount * 100),
                currency='eur',
                description='UA Feature Contribution',
                source=request.POST['stripeToken']
            )

            if payment.paid:

                for item in cart.keys():

                    user = request.user
                    ticket = get_object_or_404(Ticket, pk=item)
                    amount = cart[item]['contrib_amount']

                    contribution = Contribution(
                        userid=user,
                        ticket=ticket,
                        amount=amount_owed_after_discount)

                    contribution.save()

                    all_contribs = Contribution.objects.filter(
                        ticket=ticket).annotate(total_paid=Sum('amount'))

                    all_contribs = all_contribs[0].total_paid

                    ticket_percent_complete = (
                        all_contribs / ticket.price) * 100
                    ticket.percent_complete = ticket_percent_complete
                    ticket.save()

                messages.success(
                    request,
                    'Thank you for your contribution, \
                    keep an eye on the Features page to see \
                    when they will begin development.')

                request.session['cart'] = {}
                return redirect(reverse('dashboard'))

            else:

                messages.error(
                    request, 'The payment gateway declined your card.')

        except stripe.error.CardError:
            messages.error(
                request, 'There was an error processing your payment.')

        return redirect('dashboard')


@login_required
def updatecart(request, featureid):
    """
    Update a a feature contribution amount
    """
    cart = request.session.get('cart', {})

    if not request.POST['contribution_amount'] or request.POST['contribution_amount'] == '' or int(request.POST['contribution_amount']) < 1:
        messages.error(
            request, 'You must submit a valid contribution amount.')
        return redirect(reverse('cart'))

    if featureid in cart:

        cart[featureid]['contrib_amount'] = request.POST['contribution_amount']
        messages.success(request, "Cart Updated!")

    request.session['cart'] = cart

    return redirect(reverse('cart'))
