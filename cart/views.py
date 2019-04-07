from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from tickets.models import Ticket

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
            'id' : featureid,
            'contrib_amount' : request.POST['contribution_amount']
        }

    else:

        messages.error(request, 'You\'re already contributing to this feature.')
        return redirect('/tickets/feature/'+featureid)

    request.session['cart'] = cart

    return render(request, "cart/cart.html")

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
