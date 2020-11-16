from cms.models import Order
from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Recipient, Referrer



def admin(request):
    orders = Order.objects.all()

    new_orders = Order.objects.exclude(delivery_day='*').count()
    monday_orders = Order.objects.filter(delivery_day='Monday').count()
    tuesday_orders = Order.objects.filter(delivery_day='Tuesday').count()
    wednesday_orders = Order.objects.filter(delivery_day='Wednesday').count()
    thursday_orders = Order.objects.filter(delivery_day='Thursday').count()
    friday_orders = Order.objects.filter(delivery_day='Friday').count()

    
    context = {
        'new_orders': new_orders,
        'orders': orders,
        'monday_orders': monday_orders,
        'tuesday_orders': tuesday_orders,
        'wednesday_orders': wednesday_orders,
        'thursday_orders': thursday_orders,
        'friday_orders': friday_orders,
    }
    return render(request, 'cms/admin_pan.html', context)


def mondayDelivery(request):


    return render(request, 'cms/delivery_day.html')


def run(request):
    return render(request, 'cms/run.html')



def orderDetails(request, pk):
    order_details = Order.objects.get(id=pk)
    context = {
        'order_details': order_details
    }
    return render(request, 'cms/order_details.html', context)


def referrerDashboard(request, pk):
    referrer = Referrer.objects.get(id=pk)
    orders = referrer.order_set.all()

    context = {
        'referrer': referrer,
        'orders': orders,
    }

    return render(request, 'cms/referrer_dashboard.html', context)
