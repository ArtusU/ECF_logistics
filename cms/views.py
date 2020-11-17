from cms.models import Order
from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Delivery_Address, Order, Recipient, Referrer
from .forms import OrderForm
from .filters import OrderFilter



def admin(request):
    orders = Order.objects.all().order_by('-date_created')
    

    new_orders = Order.objects.exclude(delivery_day='*').count()
    monday_orders = Order.objects.filter(delivery_day='Monday').count()
    tuesday_orders = Order.objects.filter(delivery_day='Tuesday').count()
    wednesday_orders = Order.objects.filter(delivery_day='Wednesday').count()
    thursday_orders = Order.objects.filter(delivery_day='Thursday').count()
    friday_orders = Order.objects.filter(delivery_day='Friday').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs


    context = {
        'new_orders': new_orders,
        'orders': orders,
        'monday_orders': monday_orders,
        'tuesday_orders': tuesday_orders,
        'wednesday_orders': wednesday_orders,
        'thursday_orders': thursday_orders,
        'friday_orders': friday_orders,
        'myFilter': myFilter,
    }
    return render(request, 'cms/admin_pan.html', context)


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


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'cms/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'cms/order_form.html', context)


def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')
	context = {'item':order}
	return render(request, 'cms/delete.html', context)



