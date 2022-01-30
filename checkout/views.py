from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KNTX0HEdllUJnJgj5OkEtA3B3yg0qQwMXzzjC7aR6ERmDAWORLnHmLsiETwQRnWkoWFnmPcRk7hEoRfvEau6Vu000nRa1Avz1',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
