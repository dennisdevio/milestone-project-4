from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

def checkout(request):
    stripe_public_key = 'pk_test_51KNTX0HEdllUJnJgj5OkEtA3B3yg0qQwMXzzjC7aR6ERmDAWORLnHmLsiETwQRnWkoWFnmPcRk7hEoRfvEau6Vu000nRa1Avz1'
    stripe_secret_key = 'sk_test_51KNTX0HEdllUJnJgyftecGRkFeZxkMmiudXGZD55rA5NVRm5pBIsqIYJwUjZYzuNlbUr42slrZTXN6KQdTIe03lj0083DcTpT6'

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    print(stripe_secret_key)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
