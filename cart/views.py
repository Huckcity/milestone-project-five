import stripe

from django.conf import settings

from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def view_cart(request):

    return render(request, 'cart/cart.html')


def addtocart(request, featureid):
    """
    Add an amount to the cart for contributions to check out at a later time
    """

    cart = request.session.get('cart', {})
    if featureid not in cart:

        print(request.POST['contribution_amount'])

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


def checkout(request):

    context = {
        'key': settings.STRIPE_PUBLISHABLE_KEY
    }

    return render(request, "cart/checkout.html", context)


def charge(request):

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=request.POST['data-amount'],
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
