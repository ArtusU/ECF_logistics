from cms.decorators import unauthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import Delivery_Address, Order, Recipient, Referrer
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only



@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='referrer')
            user.groups.add(group)

            messages.success(request, 'Account was created for '+ username)
            return redirect("cms:login")
    
    context = {'form': form}
    return render(request, 'cms/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("cms:home")
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'cms/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('cms:login')


login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    orders = Order.objects.all().order_by('-date_created')
    
    new_orders = Order.objects.exclude(delivery_day='*').count()
    monday_orders = Order.objects.filter(delivery_day='Monday').count()
    tuesday_orders = Order.objects.filter(delivery_day='Tuesday').count()
    wednesday_orders = Order.objects.filter(delivery_day='Wednesday').count()
    thursday_orders = Order.objects.filter(delivery_day='Thursday').count()
    friday_orders = Order.objects.filter(delivery_day='Friday').count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs.order_by('delivery_address__post_code')


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



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer', 'driver'])
def orderDetails(request, pk):
    order_details = Order.objects.get(id=pk)
    context = {
        'order_details': order_details
    }
    return render(request, 'cms/order_details.html', context)



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer'])
def referrerDashboard(request, pk):
    referrer = Referrer.objects.get(id=pk)
    orders = referrer.order_set.all()
    context = {
        'referrer': referrer,
        'orders': orders,
    }
    return render(request, 'cms/referrer_dashboard.html', context)

'''
@login_required(login_url='login')
@allowed_users(allowed_roles=['referrer'])
def referrerDashboard(request):
    referrer = request.user.get('username')
	orders = request.user.customer.order_set.all()

    context = {
        'referrer': referrer,
        'orders': orders,
    }
    return render(request, 'cms/referrer_dashboard.html', context)
'''



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer'])
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


login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer', 'driver'])
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



login_required(login_url='cms:login')
@allowed_users(allowed_roles=['admin', 'referrer', 'driver'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')
	context = {'item':order}
	return render(request, 'cms/delete.html', context)



