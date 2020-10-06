from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process_purchase(request):
    if request.POST:
        item = Product.objects.get(id=request.POST['product_id'])
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(item.price)
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')

def checkout(request):
    all_orders = Order.objects.all()
    total_spent = 0.00
    total_items = 0
    for order in all_orders:
        total_spent+= float(order.total_price)
        total_items += int(order.quantity_ordered)
    context = {
        'order': Order.objects.order_by('-id')[0],
        'total_spent': total_spent,
        'total_items': total_items
    }
    return render(request, "store/checkout.html", context)